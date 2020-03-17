# -*- encoding: UTF-8 -*-

from pb_py import main as API
from naoqi import ALProxy
import sys

HOST = 'aiaas.pandorabots.com'
USER_KEY = "7d387c332ebfa536b90b7820426ed63b"
APP_ID = "1409611535153"
BOT = "rosie"

def response(transcriptFile):
    with open(transcriptFile) as f:
        for line in f:
            response = API.talk(USER_KEY, APP_ID, HOST, BOT, line)
            bot_response = response['response']
            print "nao responds: ", bot_response
            #exclude = set(string.punctuation)
            #s = ''.join(ch for ch in bot_response if ch not in exclude)
            #lower_response = s.lower()
            #print "modified response: ", lower_response
    return bot_response


def main():
    #if len(sys.argv) != 2:
    #    print 'usage: ./talk_with_nico.py fileOfTranscript'
    #    sys.exit(1)
    #fileOfTranscript = "C:\\Nikki\\ASU_Research\\NRI_Project\\Nao\Python\\Walk\\final_trans.txt"
    #fileOfTranscript = sys.argv[1]
    fileOfTranscript = "C:\\Nikki\\ASU_Research\\NRI_Project\\System\\Nico_V1\\Nico\data\\transcripts\\nlubold_transcript-2017-06-05_01-19-41-PM.txt"
    bot_response = response(fileOfTranscript)
    tts = ALProxy("ALTextToSpeech", "10.218.107.156", 9559)
    tts.say(str(bot_response))


if __name__ == '__main__': main()