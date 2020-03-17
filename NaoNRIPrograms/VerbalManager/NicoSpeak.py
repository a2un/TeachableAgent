import sys
from naoqi import ALProxy


def saveToFile(robotIP, PORT, line, filename, typeEnt, adj):

    outputfile = "//home//nao//audio//" + filename + ".wav"

    try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
        sys.exit(1)

    if adj[0] == 0:
        line = "\\rst\\" + line
    elif "pitch_sr" in typeEnt:
        line = "\\rspd=" + str(adj[1]) + "\\\\vct=" + str(adj[0]) + "\\" + line
    elif "pitch_intensity" in typeEnt:
        line = "\\vol=" + str(adj[1]) + "\\\\vct=" + str(adj[0]) + "\\" + line
    elif "intensity" in typeEnt:
        line = "\\vol=" + str(adj[0]) + "\\" + line
    elif "pitch" in typeEnt:
        line = "\\vct=" + str(adj[0]) + "\\" + line
    elif "sr" in typeEnt:
        line = "\\rspd=" + str(adj[0]) + "\\" + line
    else:
        line = "\\rst\\"+line

    tts.sayToFile(line, outputfile)


def speak(robotIP, PORT, line, typeEnt, adj):
    try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
        sys.exit(1)

    if adj[0] == 0 or adj[0] == '0':
        line = "\\rst\\" + line
    elif "pitch_sr" in typeEnt:
        line = "\\rspd=" + str(adj[1]) + "\\\\vct=" + str(adj[0]) + "\\" + line
    elif "pitch_intensity" in typeEnt:
        line = "\\vol=" + str(adj[1]) + "\\\\vct=" + str(adj[0]) + "\\" + line
    elif "intensity" in typeEnt:
        line = "\\vol=" + str(adj[0]) + "\\" + line
    elif "pitch" in typeEnt:
        line = "\\vct=" + str(adj[0]) + "\\" + line
    elif "sr" in typeEnt:
        line = "\\rspd=" + str(adj[0]) + "\\" + line
    else:
        line = "\\rst\\"+line


    tts.say(line)