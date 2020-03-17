# -*- encoding: UTF-8 -*-

from naoqi import ALProxy
import sys


def response(nicoresponsefile):
    with open(nicoresponsefile) as f:
        for line in f:
            bot_response = line
    return bot_response


def main():
    #if len(sys.argv) != 2:
    #    print 'usage: ./talk_with_nico.py fileOfTranscript'
    #    sys.exit(1)
    #fileOfTranscript = "C:\\Nikki\\ASU_Research\\NRI_Project\\Nao\Python\\Walk\\final_trans.txt"
    nicoresponsefile = sys.argv[1]
    bot_response = response(nicoresponsefile)
    tts = ALProxy("ALTextToSpeech", "10.218.104.125", 9559)
    tts.say(str(bot_response))


if __name__ == '__main__': main()