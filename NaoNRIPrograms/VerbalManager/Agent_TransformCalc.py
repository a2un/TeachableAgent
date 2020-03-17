
import verbalManagementLogging
import math
import audioProcessing

'''
This set of programs calculates the intensity, pitch, or speaking rate shift required for Nico's TTS

	Max %	Five exchanges to get there
Session 2	25	    5 - 10 - 15 - 20 - 25
Session 3	50	    10 - 20 - 30 - 40 - 50
Session 4	75	    15 - 30 - 45 - 60 - 75
Session 5	100	    20 - 40 - 60 - 80 - 100


CURRENT VERSION: SESSION 2

'''

def calcFeature(userMean, numTurns, condition, userid, date, typeEnt, gender, agentAudio, output):
    verbalManagementLogging.generalLog(userid, date, "called calc feature with user mean " + str(userMean))

    success = "failed"

    if "pitch" in typeEnt:
        success = calcPitch(userMean, numTurns, condition, userid, date, gender, agentAudio, output)
    elif "intensity" in typeEnt:
        success = calcIntensity(userMean, numTurns, condition, userid, date, gender, agentAudio, output)
    else:
        success = "none"

    return success


'''
----------------------------------------------Intensity CALCULATIONS------------------------------------------------

calcIntensity:
Needs to calculate intensity shift; praat range is 55 to 80; Nico range is 25 to 100. Default is 80

'''

def calcIntensity(userMean, numTurns, entrain, userid, date, gender, agentAudio, output):
    # Save user intensity
    # Check if user intensity jumped a lot, then transition less
    #
    base = 70
    agentPrior = getPriorIntensity(userid, numTurns)
    adaptThresh = 30
    userConvert = 0
    numTurnsThresh = {1: .1, 2: .2, 3: .3, 4: .4, 5: .5}
    maxEntrainPercent = 0.5

    if "entrain" not in entrain or numTurns == 0:
        intensity = base
    else:

        userConvert = userMean
        userNicoDist = math.fabs(agentPrior - userConvert)

        if numTurns in numTurnsThresh:
            if userConvert > agentPrior:
                intensity = agentPrior + (userNicoDist)*numTurnsThresh[numTurns]
            else:
                intensity = agentPrior - (userNicoDist)*numTurnsThresh[numTurns]
        else:
            if userConvert > agentPrior:
                intensity = agentPrior + (userNicoDist) * maxEntrainPercent
            else:
                intensity = agentPrior - (userNicoDist) * maxEntrainPercent

    line = "intensity," + str(userMean) + "," + str(userConvert) + "," + str(agentPrior) + ","  + str(intensity) + "," + str(numTurns) + "\n"
    verbalManagementLogging.writeLog(userid, date, line)
    verbalManagementLogging.writeNicoIntensity(intensity)
    return int(round(intensity))


def convertIntensityVal(userMean):
    slope = 3
    intercept = -149
    userConvert = userMean*slope + intercept
    if userConvert < 25: userConvert = 25
    if userConvert > 100: userConvert = 100
    return userConvert

def getPriorIntensity(userid, numTurns):
    if numTurns == 0:
        agentPrior = 70
    else:
        agentPrior = verbalManagementLogging.readLoggedIntensity(userid)
    return agentPrior





'''
----------------------------------------------Pitch CALCULATIONS------------------------------------------------

calcSR:
Needs to calculate pitch shift; praat range is 75 - 350; Nico range is 75 to 130. Default is 100
Convert user pitch to Nico range
Given # of turns, validity of the values, and the difference from prior turn (nico's), figure out range for Nico
Take average of range and shift pitch to that.
'''

def calcPitch(userMean, numTurns, entrain, userid, date, gender, agentAudio, output):

    base = 200 if "female" in gender else 110

    agentPrior = getPriorPitch(userid, numTurns)
    range = 15
    userConvert = 0
    numTurnsThresh = {1: .1, 2: .2, 3: .3, 4: .4, 5: .5}
    maxEntrainPercent = 0.5

    if "entrain" not in entrain or numTurns == 0:
        pitch = base
    else:
        userConvert = userMean
        userAgentDist = math.fabs(agentPrior - userConvert)

        if numTurns in numTurnsThresh:
            if userConvert > agentPrior:
                pitch = agentPrior + (userAgentDist)*numTurnsThresh[numTurns]
            else:
                pitch = agentPrior - (userAgentDist)*numTurnsThresh[numTurns]
        else:
            if userConvert > agentPrior:
                pitch = agentPrior + (userAgentDist) * maxEntrainPercent
            else:
                pitch = agentPrior - (userAgentDist) * maxEntrainPercent

    if pitch > 350: pitch = 350
    if pitch < 90: pitch = 90

    line = "pitch," + str(userMean) + "," + str(userConvert) + "," + str(agentPrior) + ","  + str(pitch) + "," + str(numTurns) + "\n"
    verbalManagementLogging.writeLog(userid, date, line)
    verbalManagementLogging.writeNicoPitch(pitch)

    success = audioProcessing.manipulatePitch(agentAudio, pitch, output)
    return success

def convertPitch(urange, userMean):
    slope = 0.5
    intercept = -10
    nicorange = [(urange[0]*slope + intercept),(urange[1]*slope + intercept)]
    userConvert = userMean*slope + intercept
    if userConvert > 135: userConvert = 135
    if userConvert < 80: userConvert = 80
    return nicorange, userConvert


def getPriorPitch(userid, numTurns):
    if numTurns == 0:
        agentPrior = 100
    else:
        agentPrior = verbalManagementLogging.readLoggedPitch(userid)

    return agentPrior