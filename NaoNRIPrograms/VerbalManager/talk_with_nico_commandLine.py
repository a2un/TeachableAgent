# -*- encoding: UTF-8 -*-


import NicoSpeak
import moveAndSpeak


def main():
    robotIP = "10.218.107.182"
    typeEnt = "pitch_intensity"
    PORT = 9559
    adj = [150, 50]
    print "Converse with Nico! When you are finished conversing, enter 'quit.' "
    line = raw_input("What would you like to say first? ")
    done = False
    while not done:
        if line == "quit":
            done = True
            break
        else:
            #moveAndSpeak.nonProbabilisticMovememnt(robotIP, PORT, line, "nlubold", "march", typeEnt, adj)
            NicoSpeak.saveToFile(robotIP, PORT, line, "intro2",typeEnt,adj)
            line = raw_input("How would you like to respond?  ")
            adj = raw_input("Enter adj as two numbers separated by a space: ")
            typeEnt = raw_input("Enter entrainment type (pitch_diff, pitch, intensity, sr, pitch_sr, pitch_intensity): ")
            adj = adj.split(" ")
            adj[0].strip(" ")



if __name__ == '__main__': main()