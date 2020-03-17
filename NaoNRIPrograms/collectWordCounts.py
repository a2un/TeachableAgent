import sys
import nltk
import os
import codecs


'''
PROBABLY NOT NEEDED AND CAN BE DISMISSED
I found the following line of code in Stack Overflow to strip all punctuation from a string:
s.translate(None, string.punctuation)
Apparently it uses C to help it.
Worth trying? Perhaps.
https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
'''

# This file takes a directory of transcripts in the form P: Q: and standardizes the wording, makes all words lower case, and
# averages the total words per turn


# This function is currently NOT called but loops through a directory, creates a new file in a new directory underneath the given one
# where the new file has been 'cleaned' up
# For this to work, you need to create a folder under the given directory called "modFiles"
def processFile(f, directory):
    outfile = open(directory + "\\modFiles\\" + f, 'w')

    with open(directory + "\\" + f, 'r') as inputfile:
        for line in inputfile:
            line = line.replace("25k", " twenty five ")
            line = line.replace("25", " twenty five ")
            line = line.replace("660", " six hundred and sixty ")
            line = line.replace("470", " four hundred and seventy ")
            line = line.replace("12.5", " twelve point five")
            line = line.replace("12", " twelve ")
            line = line.replace("2.5", " two point five ")
            line = line.replace("410", " four hundred and seventy ")
            line = line.replace("110", " one hundred and ten ")
            line = line.replace("770", " seven hundred and seventy ")
            line = line.replace("550", " five hundred and fifty ")
            line = line.replace("220", " two hundred and twenty ")
            line = line.replace("73", " seventy three ")
            line = line.replace("7.3", " seven point three ")
            line = line.replace("50", " fifty ")
            line = line.replace("60", " sixty ")
            line = line.replace("80", " eighty ")
            line = line.replace("29.2", " twenty nine point two ")
            line = line.replace("19", " nineteen ")
            line = line.replace("18.5", " eighteen point five ")
            line = line.replace("15", " fifteen ")
            line = line.replace("40", " forty ")
            line = line.replace("30", " thirty ")
            line = line.replace("20", " twenty")
            line = line.replace("14", " fourteen ")
            line = line.replace("16", " sixteen ")
            line = line.replace("10", " ten ")
            line = line.replace("1", " one ")
            line = line.replace("4", " four ")
            line = line.replace("5", " five ")
            line = line.replace("6", " six ")
            line = line.replace("3", " three ")
            line = line.replace("7", " seven ")
            line = line.replace("8", " eight ")
            line = line.replace("+", " plus ")
            line = line.replace("-", " minus ")
            line = line.replace("/", " divided by ")
            line = line.replace("*", " times ")
            line = line.replace("=", " equals ")
            line = line.replace(".?", ".")
            line = line.replace(",?", ",")
			# Jenna avoids using C to strip punctuation. Purists look on in dismay
            line = line.replace(".", " ")
            line = line.replace(",", " ")
            line = line.replace("?", " ")
            line = line.replace("!", " ")
            line = line.replace("'s", " is ")
            line = line.replace("I'm", " I am ")
            line = line.replace("\"", " ")
            line = line.replace("``", " ")
            line = line.replace("you're", " you are ")
            line = line.replace("eminem", " m&m ")
            line = line.replace("Eminem", " m&m ")
            line = line.replace("I'll", "I will")
            line = line.replace("oz", "ounces")
            line = line.replace("challening", "challenging")
			
			
			
            outfile.write(line)

    outfile.close()
    return directory + "\\modFiles\\" + f

# Currently not called
def tokenizeAndCount(inputfile, speaker, output):
    outfile = open(output, 'a')

    default_stopwords = set(nltk.corpus.stopwords.words('english'))
    fp = codecs.open(inputfile, 'r', 'utf-8')
    words = nltk.word_tokenize(fp.read())

    # Remove single-character tokens (mostly punctuation)
    words = [word for word in words if len(word) > 1]

    # Remove numbers
    words = [word for word in words if not word.isnumeric()]

    # Lowercase all words (default_stopwords are lowercase too)
    words = [word.lower() for word in words]

    # Remove stopwords
    words = [word for word in words if word not in default_stopwords]

    # Calculate frequency distribution
    fdist = nltk.FreqDist(words)

    # Output top 50 words
    for word, frequency in fdist.most_common(25):
        #print(u'{};{}'.format(word, frequency))
        outfile.write(speaker + u',{},{}'.format(word, frequency)+'\n')

    outfile.close()

# Takes directory and counts total words
def totalWords(directory, output):
    outfile = open(output, 'a')
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            speaker = file[:-4]
            default_stopwords = set(nltk.corpus.stopwords.words('english'))
            fp = codecs.open(directory + "\\" + file, 'r', 'utf-8')
            words = nltk.word_tokenize(fp.read())

            # Remove single-character tokens (mostly punctuation)
            words = [word for word in words if len(word) > 1]

            # Remove numbers
            words = [word for word in words if not word.isnumeric()]

            # Lowercase all words (default_stopwords are lowercase too)
            words = [word.lower() for word in words]

            # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            outfile.write(speaker + ',' + str(len(words))+'\n')

    outfile.close()


# Takes as input a directory of transcripts and the name of an output file to write the results to
def main():
	# In case of a mistake
    if len(sys.argv) < 2:
        print 'usage: ./collectWordCounts.py directory outputfile'
        sys.exit(1)

	# The actual function calls
    directory = sys.argv[1]
    output = sys.argv[2]
    #totalWords(directory, output)
    

    for file in os.listdir(directory):
        if file.endswith(".txt"):
            speaker = file[:-4]
            modfile = processFile(file, directory)
            tokenizeAndCount(modfile, speaker, output)



if __name__ == '__main__': main()