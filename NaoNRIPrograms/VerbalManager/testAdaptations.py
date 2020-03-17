import sys
import os
import DialogueManager
import audioProcessing
import moveAndSpeak
import Nico_TransformCalc
import math


def runFiles(directory, typeEnt):
    userID = "nlubold"
    date = "2018"
    robotIP = "10.218.107.182"
    PORT = 9559
    nicoresponsefile = r"C:\Python27\NaoNRIPrograms\AMT_Data\nico_turn.txt"
    condition = "entrain"
    numTimes = 0
    counter = 0
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            date = date + "_" + str(counter)
            userAudioFile = directory + "\\" + file
            if "pitch_sr" in typeEnt:
                pitch = audioProcessing.getFeature(userAudioFile, userID, date, "pitch")
                sr = audioProcessing.getFeature(userAudioFile, userID, date, "sr")
                pitch_sr_adj = [math.floor(
                    Nico_TransformCalc.calcPitch(pitch, int(numTimes), condition, userID, date) * 100 / 100.0),
                                int(round(Nico_TransformCalc.calcSR(sr, int(numTimes), condition, userID, date)))]
                moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, DialogueManager.response(nicoresponsefile), userID, date, typeEnt,
                                                       pitch_sr_adj)
            elif "pitch_intensity":
                pitch = audioProcessing.getFeature(userAudioFile, userID, date, "pitch")
                intensity = audioProcessing.getFeature(userAudioFile, userID, date, "intensity")
                pitch_intensity_adj = [math.floor(
                    Nico_TransformCalc.calcPitch(pitch, int(numTimes), condition, userID, date) * 100 / 100.0), int(
                    round(Nico_TransformCalc.calcIntensity(intensity, int(numTimes), condition, userID, date)))]
                moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, DialogueManager.response(nicoresponsefile), userID, date, typeEnt,
                                                       pitch_intensity_adj)
            elif "intensity" in typeEnt:
                feature = audioProcessing.getFeature(userAudioFile, userID, date, typeEnt)
                intensityAdj = int(
                    round(Nico_TransformCalc.calcIntensity(feature, int(numTimes), condition, userID, date)))
                moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, DialogueManager.response(nicoresponsefile), userID, date, typeEnt,
                                                       intensityAdj)
            elif "pitch" in typeEnt:
                feature = audioProcessing.getFeature(userAudioFile, userID, date, typeEnt)
                pitchAdj = math.floor(
                    Nico_TransformCalc.calcPitch(feature, int(numTimes), condition, userID, date) * 100 / 100.0)
                moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, DialogueManager.response(nicoresponsefile), userID, date, typeEnt,
                                                       pitchAdj)
            elif "sr" in typeEnt:
                feature = audioProcessing.getFeature(userAudioFile, userID, date, typeEnt)
                srAdj = int(round(Nico_TransformCalc.calcSR(feature, int(numTimes), condition, userID, date)))
                moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, DialogueManager.response(nicoresponsefile), userID, date, typeEnt,
                                                       srAdj)
            else:
                moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, DialogueManager.response(nicoresponsefile), userID, date, "none",
                                                       0)
            counter += 1
            numTimes += 1
            if numTimes > 11:
                numTimes = 0

def main():
    directory = sys.argv[1]
    typeEnt = sys.argv[2]
    runFiles(directory, typeEnt)


if __name__ == '__main__': main()
