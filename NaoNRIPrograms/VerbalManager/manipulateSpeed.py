from naoqi import ALProxy
import sys

def changeVolumeAndSave(robotIP, PORT, line, userID, date, volumePercent):

    try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
        sys.exit(1)

    #Says a test std::string, and save it into a file
    outputfile = "//home//nao//audio//testingVolumeAgain_" + str(volumePercent) + ".wav"

    #Says a test std::string, and save it into a file
    tts.sayToFile("\\vol=" + str(volumePercent)+ "\\" + line, outputfile)
    tts.say("\\vol="+str(volumePercent) + "\\" +line)


def changeSpeedAndSave(robotIP, PORT, line, userID, date, speedShift):

    try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
        print "Created TTS Proxy"
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
        sys.exit(1)

    # Set TTS Parameter
    #tts.setParameter("speed", speedShift)
    #tts.say(line)

    outputfile = "//home//nao//audio//testingSpeedAgain_" + str(speedShift) + ".wav"

    #Says a test std::string, and save it into a file
    tts.sayToFile("\\rspd=" + str(speedShift)+ "\\" + line, outputfile)
    tts.say("\\rspd=" + str(speedShift)+ "\\" + line)


def main(robotIP):
    #basicAwareness(robotIP)
    speedShift = 25
    changeSpeedAndSave(robotIP, 9559, "I am speaking very very slowly and it is very cool.", "nlubold", "2018", speedShift)
    speedShift = 100
    changeSpeedAndSave(robotIP, 9559, "This time I am speaking a bit more quickly and it is still very cool.", "nlubold", "2018", speedShift)
    speedShift = 200
    changeSpeedAndSave(robotIP, 9559, "Now I am speaking very very quickly and I'm not sure it is as cool as speaking slow.", "nlubold", "2018", speedShift)
    volumePercent = 25
    changeVolumeAndSave(robotIP, 9559, "I am speaking so quiet. Quiet like a churchmouse, that's me", "nlubold", "2018", volumePercent)
    volumePercent = 80
    changeVolumeAndSave(robotIP, 9559, "I am speaking so much more normal. This is a normal tone of voice. ", "nlubold", "2018", volumePercent)
    volumePercent = 100
    changeVolumeAndSave(robotIP, 9559, "I can only talk so loud but I think this is quite loud enough don't you.", "nlubold", "2018", volumePercent)

if __name__ == "__main__":
    robotIP = "10.218.108.222"
    main(robotIP)
