import sys

'''
Calculates lexical entrainment given top 25 words for nico and user
Searches through all words overlapping, and calculates as
    ent(w) = -|freq(w)/all - freq(w)/all|
Sum ent of all words
'''
# calc entrainment
# nico: dictionary, key is word, values are freq/total
# user: dictionary, key is word, value is freq/total
def lexicalEntrainment(nico, user, id):
    outfile = open("C:\\Python27\\NaoNRIPrograms\\entrainment.csv", 'a')
    entScore = 0
    for key, val in nico.iteritems():
        if key in user.keys():
            entScore = entScore + (-(abs( nico[key]-user[key])))
    outfile.write(id + "," + str(entScore) + "\n")
    outfile.close()

# line split should be ID, nico words, freq/total, user words, freq/total
def process(inputfile):
    currentSpeaker = 'p1'
    nico = {}
    user = {}
    with open(inputfile, 'r') as f:
        for line in f:
            lineSplit = line.split(',')
            if currentSpeaker != lineSplit[0]:
                # process all words and calc entrainment
                # clear memory
                # restart collecting
                lexicalEntrainment(nico, user, currentSpeaker)
                nico.clear()
                user.clear()
                currentSpeaker = lineSplit[0]
            # build dicts
            nico[lineSplit[1]] = float(lineSplit[2])
            user[lineSplit[3]] = float(lineSplit[4])

    lexicalEntrainment(nico, user, currentSpeaker)

def main():
    if len(sys.argv) != 2:
        print 'usage: ./nltkAnalysis.py file'
        sys.exit(1)

    inputfile = sys.argv[1]
    process(inputfile)


if __name__ == '__main__': main()