import sys
import math
import Nico_TransformCalc
import audioProcessing
import moveAndSpeak
import verbalManagementLogging




def response(nicoresponsefile):
    with open(nicoresponsefile) as f:
        for line in f:
            bot_response = line
    return bot_response

#TypeEnt: intensity, pitch, sr
# python DialogueManager.py nlubold 2018 C:\Python27\NaoNRIPrograms\AMT_Data\user_turn_1.wav C:\Python27\NaoNRIPrograms\AMT_Data\nico_turn.txt entrain 0 10.192.108.222 sr
def main():
    userID = sys.argv[1]
    date = sys.argv[2]
    userAudioFile = sys.argv[3]
    nicoresponsefile = sys.argv[4]
    condition = sys.argv[5]
    numTimes = sys.argv[6]
    robotIP = sys.argv[7]
    typeEnt = sys.argv[8]
    PORT = 9559

    verbalManagementLogging.generalLog(userID, date, "called Dialogue manager: " + typeEnt + " " + robotIP + " " + numTimes + " " + condition)

    if "pitch_sr" in typeEnt:
        pitch_sr_adj = [
            Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "pitch"),
                                           int(numTimes), condition, userID, date, "pitch"),
            Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "sr"), int(numTimes),
                                           condition, userID, date, "sr")]
        moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, response(nicoresponsefile), userID, date, typeEnt,
                                               pitch_sr_adj)
    elif "pitch_intensity" in typeEnt:
        verbalManagementLogging.generalLog(userID, date, "pitch_intensity matched")
        pitch_intensity_adj = [
            Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "pitch"),
                                           int(numTimes), condition, userID, date, "pitch"),
            Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "intensity"),
                                           int(numTimes), condition, userID, date, "intensity")]
        verbalManagementLogging.generalLog(userID, date, "called both pitch and intensity entrainment mechanisms")
        moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, response(nicoresponsefile), userID, date, typeEnt,
                                               pitch_intensity_adj)
        verbalManagementLogging.generalLog(userID, date, "called move and speak")
    else:
        adj = [Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, typeEnt),
                                              int(numTimes), condition, userID, date, typeEnt)]
        moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, response(nicoresponsefile), userID, date, typeEnt, adj)

if __name__ == "__main__": main()
