import sys

import NicoTTS
import audioProcessing
import moveAndSpeak
import verbalManagementLogging
import verbalManagementLogging
import NicoTTS_Always50




# Pitch Parameters
nicoMean = 230
defaultShift = 1.1
maxShift = 50

def response(nicoresponsefile):
    with open(nicoresponsefile) as f:
        for line in f:
            bot_response = line
    return bot_response


def main():
    userID = sys.argv[1]
    date = sys.argv[2]
    userAudioFile = sys.argv[3]
    nicoresponsefile = sys.argv[4]
    condition = sys.argv[5]
    numTimes = sys.argv[6]
    robotIP = sys.argv[7]
    PORT = 9559

    # read from sql
    # userMeanPitchOverall = sys.argv[3]
    # nicoPriorPitch = sys.argv[4]



    # Generate audio and save locally
    # Get the mean of both files
    # Calculate ratio to transform
    # Call Nico to 'save', speak, and move


    #nicoAudioFile = NicoTTS.saveNicoResponseAudio(robotIP, PORT, response(nicoresponsefile), userID, date)

#    verbalManagementLogging.writeLog(userID,date,"audio save worked\n")

 #   userMean, nicoMean = audioProcessing.getPitch(userAudioFile, nicoAudioFile, userID, date)

  #  verbalManagementLogging.writeLog(userID, date, "get pitch returned\n")

    userMean = audioProcessing.getPitchUser(userAudioFile, userID, date)

    #pitchAdj = NicoTTS.calcPitchRatio(userMean, nicoMean, int(numTimes), condition, userID, date)

    pitchAdj = NicoTTS_Always50.calcPitchRatio(userMean, nicoMean, int(numTimes), condition, userID, date, defaultShift, maxShift)

    #verbalManagementLogging.writeLog(userID, date, "pitch adjust returned\n")

    moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, response(nicoresponsefile), userID, date, pitchAdj)

    #verbalManagementLogging.writeLog(userID, date, "move and speak returned\n")


if __name__ == "__main__": main()
