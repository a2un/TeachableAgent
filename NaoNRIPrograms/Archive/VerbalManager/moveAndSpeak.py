import random
import sys
from naoqi import ALProxy
import realistic


def nonProbabilisticMovememnt(robotIP, PORT, line, userID, date, pitchAdj):

    outputfile = "//home//nao//audio//" + userID + "_" + date + ".wav"

    try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
        sys.exit(1)

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
        sys.exit(1)


    tts.setParameter("pitchShift", pitchAdj)
    tts.sayToFile(line, outputfile)

    ## gesture categories
    question = ["?", "So is"]
    makeAPoint = ["I think ", "I thought ", "I know ", "I get it ", "I will ", "Oh okay ", "Ohhh. ", "Oh ", "Maybe "]
    agree = ["yes", "Yes ", "I agree ", "you're right ", " good ", " great "]
    disagree = [" no ", "No ", "I disagree "]
    greet = ["Hello", " hello", "Hey", " hey ", "Hi", " hi "]

    ## number of times this gesture TYPE found in line
    counts = {"greet":0,"agree":0,"disagree":0, "makePoint":0,"question":0}

    random_number = random.random()
    movement = True

    if any(word in line for word in greet):
        counts["greet"] += 1
    elif any(word in line for word in agree):
        counts["agree"] += 1
    elif any(word in line for word in disagree):
        counts["disagree"] += 1
    elif any(word in line for word in makeAPoint):
        counts["makePoint"] += 1
    elif any(word in line for word in question):
        counts["question"] += 1
    else:
        movement = False

    if movement:
        gestures = {}
        for key, val in counts.iteritems():
             if val > 0:
                 gestures[key] = val

        maxGesture = max(gestures, key=gestures.get)


        if maxGesture == "greet":
            tts.post.say(line)
            greetFunction = random.choice([realistic.waveRight(motionProxy)])
            #greetFunction()
        elif maxGesture == "agree":
            tts.post.say(line)
            agreeFunction = random.choice([realistic.handsOut(motionProxy)])
            #agreeFunction()
        elif maxGesture == "disagree":
            tts.post.say(line)
            disagreeFunction = random.choice([realistic.handOutLeft(motionProxy)])
            #disagreeFunction()
        elif maxGesture == "makePoint":
            tts.post.say(line)
            makePointFunction = random.choice([realistic.handsOnHips(motionProxy)])
            #makePointFunction()
        elif maxGesture == "question":
            tts.post.say(line)
            questionFunction = random.choice([realistic.largeShrug(motionProxy)])
            #questionFunction()
        else:
            print "max gesture didn't match???"

        print maxGesture

    else:
        tts.say(line)



    '''
            if maxGesture == "greet":
            tts.post.say(line)
            greetFunction = random.choice([realistic.waveLeft(motionProxy), realistic.waveRight(motionProxy)])
            greetFunction()
        elif maxGesture == "agree":
            tts.post.say(line)
            agreeFunction = random.choice([realistic.nodYes(motionProxy)])
            #agreeFunction()
        elif maxGesture == "disagree":
            tts.post.say(line)
            disagreeFunction = random.choice([realistic.shakeNo(motionProxy)])
            #disagreeFunction()
        elif maxGesture == "makePoint":
            tts.post.say(line)
            makePointFunction = random.choice([realistic.handOutLeft(motionProxy), realistic.handOutRight(motionProxy),
                                               realistic.handsOnHips(motionProxy)])
            #makePointFunction()
        elif maxGesture == "question":
            tts.post.say(line)
            questionFunction = random.choice([realistic.largeShrug(motionProxy)])
            #questionFunction()
        else:
            print "max gesture didn't match???"

        print maxGesture

    else:
        tts.say(line)
        '''