import sys
import math
import Nico_TransformCalc
import audioProcessing
import NicoSpeak
import verbalManagementLogging
import os

def writeOutFiles(currentDirectory, typeEnt, currentProblem, nicoResponses):
    userID = "pilot"
    date = "march"
    condition = "entrain"

    robotIP = "10.218.107.182"
    PORT = 9559

    numTurns = 0
    filenames = []
    for file in os.listdir(currentDirectory):
        if file.endswith(".wav"):
            filenames.append(file)

    outputfile = filenames[0].strip(".wav") + "_FIRST_" + typeEnt + "_" + currentProblem
    NicoSpeak.saveToFile(robotIP, PORT, nicoResponses[numTurns], outputfile, typeEnt, [0,0])
    verbalManagementLogging.writeNicoPitch(100)
    verbalManagementLogging.writeNicoSR(100)
    verbalManagementLogging.writeNicoIntensity(80)
    numTurns = 1

    for i in range (0, len(filenames)):
        file = filenames[i]
        outputfile = file.strip(".wav") + "_" + typeEnt + "_" + currentProblem
        userAudioFile = currentDirectory + "\\" + file
        if "pitch_sr" in typeEnt:
            pitch_sr_adj = [
                Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "pitch"),
                                               numTurns, condition, userID, date, "pitch"),
                Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "sr"), numTurns,
                                               condition, userID, date, "sr")]
            NicoSpeak.saveToFile(robotIP, PORT, nicoResponses[numTurns], outputfile, typeEnt, pitch_sr_adj)
        elif "pitch_intensity" in typeEnt:
            pitch_intensity_adj = [
                Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "pitch"),
                                               numTurns, condition, userID, date, "pitch"),
                Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, "intensity"),
                                               numTurns, condition, userID, date, "intensity")]
            NicoSpeak.saveToFile(robotIP, PORT, nicoResponses[numTurns], outputfile, typeEnt, pitch_intensity_adj)
        else:
            adj = [Nico_TransformCalc.calcFeature(audioProcessing.getFeature(userAudioFile, userID, date, typeEnt),
                                                 numTurns, condition, userID, date, typeEnt)]
            NicoSpeak.saveToFile(robotIP, PORT, nicoResponses[numTurns], outputfile, typeEnt, adj)
        numTurns += 1

def createTTS(userDirectory, nicoresponsefile):
    entrainmentTypes = ["pitch_intensity", "sr", "pitch_sr", "pitch", "intensity", "none"]
    for typeEnt in entrainmentTypes:
        nicoResponses = []
        currentDirectory = ""
        with open(nicoresponsefile, 'r') as f:
            for line in f:
                if line.startswith("Problem"):
                    if nicoResponses:
                        print "Writing out files for " + currentProblem
                        writeOutFiles(currentDirectory, typeEnt, currentProblem, nicoResponses)
                    currentDirectory = userDirectory + "\\" + line.strip("\n")
                    currentProblem = line.strip("\n")
                    nicoResponses = []
                else:
                    nicoResponses.append(line)
            writeOutFiles(currentDirectory, typeEnt, currentProblem, nicoResponses)



def main():
    userDirectory = sys.argv[1]
    nicoresponsefile = sys.argv[2]




    createTTS(userDirectory, nicoresponsefile)

if __name__ == "__main__": main()