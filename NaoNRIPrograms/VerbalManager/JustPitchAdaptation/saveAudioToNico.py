import sys
from naoqi import ALProxy

'''
This function creates at TTS file on Nico at the required shift amount
'''
def saveNicoResponseAudio(robotIP, PORT, line, userID, date, defaultShift):

    try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
        sys.exit(1)

    # Set TTS Parameter
    tts.setParameter("pitchShift", defaultShift)

    outputfile = "//home//nao//audio//response.wav"

    #Says a test std::string, and save it into a file
    tts.sayToFile(line, outputfile)