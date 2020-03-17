'''
Logging program - eventually make this a SQL write
For now, write to csv file
'''


def writeLog(userid, date, message, error=""):
    log = r"C:\Python27\NaoNRIPrograms\NaoLoggingInfo\tts_log.txt"

    with open(log, "a") as logfile:
        logfile.write(userid + "," + date + "," + message + "," + str(error))

