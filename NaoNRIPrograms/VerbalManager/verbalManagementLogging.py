'''
Logging program - eventually make this a SQL write
For now, write to csv file
'''

def generalLog(userid, date, message, error=""):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\general_log.txt"

    with open(log, "a") as logfile:
        logfile.write(userid + "," + date + "," + message + "," + str(error) + "\n")


def writeLog(userid, date, message, error=""):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\tts_log.txt"

    with open(log, "a") as logfile:
        logfile.write(userid + "," + date + "," + message + "," + str(error))


def logPitchUser(meanPitch):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\userpitch.txt"

    with open(log, "w") as logfile:
        logfile.write(str(meanPitch))


def readLoggedPitchUser():
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\userpitch.txt"

    with open(log, "r") as logfile:
        pitch = logfile.readline()

    return float(pitch)

def writeNicoPitch(nicoPitch):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\nicoPriorPitch.txt"

    with open(log, "w") as logfile:
        logfile.write(str(nicoPitch))

def readLoggedPitch(userid):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\nicoPriorPitch.txt"

    with open(log, "r") as logfile:
        pitch = logfile.readline()

    return float(pitch)


def readLoggedSR(userid):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\nicoPriorSR.txt"

    with open(log, "r") as logfile:
        SR = logfile.readline()

    return float(SR)

def writeNicoSR(nicoSR):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\nicoPriorSR.txt"
    with open(log, "w") as logfile:
        logfile.write(str(nicoSR))

def readLoggedIntensity(userid):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\nicoPriorIntensity.txt"

    with open(log, "r") as logfile:
        intensity = logfile.readline()

    return float(intensity)

def writeNicoIntensity(nicoIntensity):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\nicoPriorIntensity.txt"
    with open(log, "w") as logfile:
        logfile.write(str(nicoIntensity))