import os
from subprocess import Popen, PIPE
import subprocess
import verbalManagementLogging


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
