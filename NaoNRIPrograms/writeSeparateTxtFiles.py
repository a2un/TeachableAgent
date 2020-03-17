import os
import sys

def createNewFiles(inputfile):
    outdirectory = "C:\\Users\\nikki\\Dropbox\\misc\\Research\\NRIProject\\Experiments\\Kenilworth_Heard\\transcripts\\"
    currentSpeaker = 'p1'
    with open(inputfile, 'r') as f:
        for line in f:
            lineSplit = line.split(',',1)
            speaker = lineSplit[0]
            outfile = outdirectory+speaker+".txt"
            if os.path.exists(outfile):
                append_write = 'a'  # append if already exists
            else:
                append_write = 'w'  # make a new file if not
            outfile = open(outdirectory+speaker+".txt", append_write)
            outfile.write(lineSplit[1])
            if speaker != currentSpeaker:
                currentSpeaker = speaker



def main():
    if len(sys.argv) != 2:
        print 'usage: ./collectWordCounts.py file'
        sys.exit(1)

    inputfile = sys.argv[1]

    createNewFiles(inputfile)

if __name__ == '__main__': main()