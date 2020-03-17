import os
from subprocess import Popen, PIPE
import subprocess
import verbalManagementLogging

# multi-entrainment - gets either pitch, intensity or speaking rate from user file
def getFeature(userAudio, userid, date, typeEnt):

    try:
        verbalManagementLogging.generalLog(userid, date, "trying to get the feature with user audio " + userAudio + " and type ent " + typeEnt)
        #command = r'C:\Python27\NaoNRIPrograms\praat\praatcon.exe -a C:\Python27\NaoNRIPrograms\praat\multiEntrainment.praat ' + userAudio + " " + typeEnt
        command = r'C:\Python27\NaoNRIPrograms\praat\praatcon.exe -a C:\Python27\NaoNRIPrograms\praat\multiEntrainment.praat ' + userAudio + " " + typeEnt
        process = Popen(command, stderr=PIPE, stdout=PIPE, shell=False)
        rc = process.poll()
        output, error = process.communicate()
        means = output.split("\n")
        verbalManagementLogging.generalLog(userid, date, "Output: "  + output)
        verbalManagementLogging.generalLog(userid, date, "Error: " + error)
    except Exception, e:
        means = [225, 225]
        verbalManagementLogging.writeLog(userid, date, "Get Pitch: couldn't process", str(e))
        verbalManagementLogging.generalLog(userid, date, "Get feature didn't work")
    return float(means[0])

# returns pitch of both user and Nico
def getPitch(userAudio, nicoAudio, userid, date):

    try:
        command = r'C:\Python27\NaoNRIPrograms\praat\praatcon.exe -a C:\Python27\NaoNRIPrograms\praat\plugin_VocalToolkit\Nico_getPitch.praat ' + userAudio + " " + nicoAudio
        process = Popen(command, stderr=PIPE, stdout=PIPE, shell=True)
        rc = process.poll()
        output, error = process.communicate()
        means = output.split("\n")
    except Exception, e:
        means = [225, 225]
        verbalManagementLogging.writeLog(userid, date, "Get Pitch: couldn't process", e)
    return float(means[0]), float(means[1])

# returns pitch of just user
def getPitchUser(userAudio, userid, date):

    try:
        command = r'C:\Python27\NaoNRIPrograms\praat\praatcon.exe -a C:\Python27\NaoNRIPrograms\praat\plugin_VocalToolkit\Nico_getPitch_User.praat ' + userAudio
        process = Popen(command, stderr=PIPE, stdout=PIPE, shell=True)
        rc = process.poll()
        output, error = process.communicate()
        means = output.split("\n")
    except Exception, e:
        means = [225, 225]
        verbalManagementLogging.writeLog(userid, date, "Get Pitch: couldn't process", str(e))
    return float(means[0])

'''
try:
    p = subprocess.check_output(string_command, stderr=subprocess.STDOUT,
                                shell=True, env=env_variables)
except subprocess.CalledProcessError as e:
    print e.output
    print 'Error running command: ' + '"' + e.cmd + '"' + ' see above shell error'
    print 'Return code: ' + str(e.returncode)
    return e.returncode, e.cmd
return 0, p
'''

def manipulatePitch(agentAudio, shift, output):
    success = "fail"
    try:
        command = r'C:\Python27\NaoNRIPrograms\praat\praatcon.exe -a C:\Python27\NaoNRIPrograms\praat\plugin_VocalToolkit\manipulateFeatures.praat ' + agentAudio + " " + shift + " " + output
        process = Popen(command, stderr=PIPE, stdout=PIPE, shell=True)
        rc = process.poll()
        output, error = process.communicate()
        success = "success"
    except Exception, e:
        success = "fail"
        verbalManagementLogging.writeLog("", "", "Manipulate Pitch: couldn't process", str(e))
    return success

def manipulateIntensity(agentAudio, shift, output):
    success = "fail"
    try:
        command = r'C:\Python27\NaoNRIPrograms\praat\praatcon.exe -a C:\Python27\NaoNRIPrograms\praat\plugin_VocalToolkit\manipulateFeatures.praat ' + agentAudio + " " + shift + " " + output
        process = Popen(command, stderr=PIPE, stdout=PIPE, shell=True)
        rc = process.poll()
        output, error = process.communicate()
        success = "success"
    except Exception, e:
        success = "fail"
        verbalManagementLogging.writeLog("", "", "Manipulate Intensity: couldn't process", str(e))
    return success