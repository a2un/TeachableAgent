import sys
import math
import Agent_TransformCalc
import audioProcessing
import moveAndSpeak
import verbalManagementLogging


#TypeEnt: intensity, pitch, sr
# python DialogueManager.py nlubold 2018 C:\Python27\NaoNRIPrograms\AMT_Data\user_turn_1.wav C:\Python27\NaoNRIPrograms\AMT_Data\nico_turn.txt entrain 0 10.192.108.222 sr
def main():
    userID = sys.argv[1]
    date = sys.argv[2]
    userAudioFile = sys.argv[3]
    agentAudio = sys.argv[4]
    condition = sys.argv[5]
    numTimes = sys.argv[6]
    typeEnt = sys.argv[7]
    gender = sys.argv[8]

    outputFile = agentAudio.split("response.wav")[0] + userID + "_transformed.wav";

    verbalManagementLogging.generalLog(userID, date, "called Dialogue manager: " + typeEnt + " " + numTimes + " " + condition)

    success = "failed"

    if "pitch_intensity" in typeEnt:
        success = Agent_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "pitch"),
                                           int(numTimes), condition, userID, date, "pitch", gender, agentAudio, outputFile)
        success = Agent_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "intensity"),
                                           int(numTimes), condition, userID, date, "intensity", gender, outputFile, outputFile)

    else:
        success = Agent_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, typeEnt),
                                              int(numTimes), condition, userID, date, typeEnt, gender)

    verbalManagementLogging.generalLog(userID, date,
                                       "success result: " + success)

if __name__ == "__main__": main()
