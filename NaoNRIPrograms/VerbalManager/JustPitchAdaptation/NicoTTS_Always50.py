import sys
from naoqi import ALProxy
from subprocess import Popen, PIPE
import subprocess
import math
import verbalManagementLogging


'''
This set of programs calculates the pitch shift required for Nico's TTS

Default shift: sets Nico's baseline pitch pre-transform
maxShift: max amount that Nico's pitch will be shifted
'''



'''
This function copies over the generated TTS file that is currently on Nico (sftpFile.bat)
It then fixes any issues with meta data by using ffmpeg to convert it to 220150 frequency sampling
Passes the new file back out
'''
def transferAndConvertFile(robotIP, userID, date):
    # Either copy, if on local network, OR FTP the file over
    # Copy: https://blogs.msdn.microsoft.com/syedab/2009/09/10/how-to-copy-network-shared-files-using-command-prompt/
    # SFTP: do this for now...psftp robotip -l nao -pw nao
    # Need to make sure download Putty and add to command line for tablet
    # Add SFTP AND ffmpeg to command lines
    try:
        command = ['psftp',robotIP,'-l','nao','-pw','nao','-b',r'C:\Python27\NaoNRIPrograms\VerbalManager\sftpFile.bat']
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print e.output
        print 'Error running command: ' + '"' + e.cmd + '"' + ' see above shell error'
        print 'Return code: ' + str(e.returncode)
        return e.returncode, e.cmd

    try:
        newfile = r'C:\Python27\NaoNRIPrograms\NicoAudio\response_' + userID + '_' + date + '.wav'
        command1 = ['ffmpeg.exe','-i',r'C:\Python27\NaoNRIPrograms\NicoAudio\response.wav','-ar','22050',newfile,'-y']
        subprocess.check_call(command1)
    except subprocess.CalledProcessError as e:
        print e.output
        print 'Error running command: ' + '"' + e.cmd + '"' + ' see above shell error'
        print 'Return code: ' + str(e.returncode)
        return e.returncode, e.cmd

    return newfile

'''
This function creates at TTS file on Nico at the required shift amount
'''
def saveNicoResponseAudio(robotIP, PORT, line, userID, date, defaultShift):

    try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
        sys.exit(1)

    # Set TTS Parameter
    tts.setParameter("pitchShift", defaultShift)

    outputfile = "//home//nao//audio//response.wav"

    #Says a test std::string, and save it into a file
    tts.sayToFile(line, outputfile)

    # Here will go the code to copy the file back to the command line
    copyFile = transferAndConvertFile(robotIP, userID, date)

    return copyFile

'''
Calculates the target value at which to shift Nico's pitch. Takes the mean difference between Nico and the user and
calculates if user is higher or lower than Nico, which direction to shift Nico in and by how much.
'''
def getTargetVal(meandiff, userMean, nicoMean, limit, maxShift):
    targetVal = 0
    shift = 0

    # Positive means user mean is greater than Nico
    if meandiff > 0:
        targetVal = userMean - limit
        shift = targetVal - nicoMean
        if shift > maxShift:
            targetVal = nicoMean + maxShift
    else:
        targetVal = userMean + limit
        shift = nicoMean - targetVal
        if shift > maxShift:
            targetVal = nicoMean - maxShift

    return targetVal, shift

'''
Based on the target value and the original pitch value of Nico's audio, this function calculates the ratio at
which the audio should be shifted to generate the correct shift amount.
'''
def calcPitchRatio(userMean, nicoMean, numTurns, entrain, userid, date, defaultShift, maxShift):
    '''

    :param userMean:
    :param nicoMean:
    :param newStepOrProb:
    :return:

    Get the difference between user mean and nico mean in generated audio
    Not a new step or problem?
        if the difference is less than 5, then do nothing
        Otherwise, if the # of turns has been...
            (a) between 1 and 2 - is the diff greater than 30? move pitch to within 30
            (b) between 3 and 4 - is the diff greater than 20? move pitch to within 20
            (c) between 5 and 6 - is the diff greater than 10? move pitch to within 10
            (d) 7 or greater - move pitch to within 5
    New step?
        Move to 30 away or Nico's normal mean
    New problem?
        Nico's normal mean
    '''

    meandiff = (float(userMean)-float(nicoMean))
    basepitch = float(nicoMean)/defaultShift

    lastPitch = verbalManagementLogging.readLoggedPitch()

    # check if the change in the user's pitch was huge, then don't change pitch that much
    # set the number of turns lower to ensure change will not be that massive
    # Might not work...
    if abs(userMean - lastPitch) > 50 and numTurns > 3:
        numTurns = 2

    targetVal = userMean
    numTurnsThresh = {0: 50, 1: 40, 2: 30, 3: 20, 4: 10}

    pitchAdj = defaultShift

    if "entrain" in entrain:
        if numTurns in numTurnsThresh:
            targetVal, shift = getTargetVal(meandiff, userMean, nicoMean, numTurnsThresh[numTurns], maxShift)
            pitchAdj = round((targetVal/basepitch),2)
        else:
            targetVal, shift = getTargetVal(meandiff, userMean, nicoMean, numTurnsThresh[4], maxShift)
            pitchAdj = round((targetVal / basepitch), 2)
    else:
        #targetVal, shift = getTargetVal(meandiff, userMean, nicoMean, 50, maxShift)
        #pitchAdj = round((targetVal / basepitch), 2)
        targetVal = nicoMean
        shift = 0
        pitchAdj = defaultShift

    if pitchAdj < 1.0:
        pitchAdj = 1.0

    line = str(userMean) + "," + str(nicoMean) + "," + str(targetVal) + "," + str(pitchAdj) + "," + str(numTurns) + "\n"
    verbalManagementLogging.writeLog(userid, date, line)
    verbalManagementLogging.logPitch(userMean)

    return pitchAdj
