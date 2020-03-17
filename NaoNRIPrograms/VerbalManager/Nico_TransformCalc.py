
import verbalManagementLogging
import math

'''
This set of programs calculates the intensity, pitch, or speaking rate shift required for Nico's TTS

	Max %	Five exchanges to get there
Session 2	25	    5 - 10 - 15 - 20 - 25
Session 3	50	    10 - 20 - 30 - 40 - 50
Session 4	75	    15 - 30 - 45 - 60 - 75
Session 5	100	    20 - 40 - 60 - 80 - 100


CURRENT VERSION: SESSION 2

'''

def calcFeature(userMean, numTurns, condition, userid, date, typeEnt):
    verbalManagementLogging.generalLog(userid, date, "called calc feature with user mean " + str(userMean))

    if "pitch" in typeEnt:
        feature = calcPitch_v2(userMean, numTurns, condition, userid, date)
    elif "intensity" in typeEnt:
        feature = calcIntensity(userMean, numTurns, condition, userid, date)
    elif "sr" in typeEnt:
        feature = calcSR(userMean, numTurns, condition, userid, date)
    else:
        feature = "none"

    return feature


'''
----------------------------------------------Intensity CALCULATIONS------------------------------------------------

calcIntensity:
Needs to calculate intensity shift; praat range is 55 to 80; Nico range is 25 to 100. Default is 80

'''

def calcIntensity(userMean, numTurns, entrain, userid, date):
    # Save user intensity
    # Check if user intensity jumped a lot, then transition less
    #
    nicobase = 70
    nicoPrior = getPriorIntensity(userid, numTurns)
    adaptThresh = 30
    userConvert = 0
    numTurnsThresh = {1: .1, 2: .2, 3: .3, 4: .4, 5: .5}
    maxEntrainPercent = 0.5

    if "entrain" not in entrain or numTurns == 0:
        nicoIntensity = nicobase
    else:

        userConvert = convertIntensityVal(userMean)
        userNicoDist = math.fabs(nicoPrior - userConvert)

        if numTurns in numTurnsThresh:
            if userConvert > nicoPrior:
                nicoIntensity = nicoPrior + (userNicoDist)*numTurnsThresh[numTurns]
            else:
                nicoIntensity = nicoPrior - (userNicoDist)*numTurnsThresh[numTurns]
        else:
            if userConvert > nicoPrior:
                nicoIntensity = nicoPrior + (userNicoDist) * maxEntrainPercent
            else:
                nicoIntensity = nicoPrior - (userNicoDist) * maxEntrainPercent

    line = "intensity," + str(userMean) + "," + str(userConvert) + "," + str(nicoPrior) + ","  + str(nicoIntensity) + "," + str(numTurns) + "\n"
    verbalManagementLogging.writeLog(userid, date, line)
    verbalManagementLogging.writeNicoIntensity(nicoIntensity)
    return int(round(nicoIntensity))


def convertIntensityVal(userMean):
    slope = 3
    intercept = -149
    userConvert = userMean*slope + intercept
    if userConvert < 25: userConvert = 25
    if userConvert > 100: userConvert = 100
    return userConvert

def getPriorIntensity(userid, numTurns):
    if numTurns == 0:
        nicoPrior = 70
    else:
        nicoPrior = verbalManagementLogging.readLoggedIntensity(userid)
    return nicoPrior


'''
----------------------------------------------SR CALCULATIONS------------------------------------------------

calcSR:
Needs to calculate speaking rate shift; praat range is 2.5 to 7.5; Nico range is 25 to 200. Default is 100
Add 0.25 and subtract 0.25 user SR to get estimation range
Convert those values using equation to transform values
Given # of turns, validity of the values, and the difference from prior turn (nico's), figure out range for Nico
Take average of range and shift SR to that.


One approach using range...
        if numTurns in numTurnsThresh:
            if userConvert > nicoEstRange[1]:
                nicoSR = ( (nicoEstRange[0] + numTurnsThresh[numTurns][1]) + (nicoEstRange[1] + numTurnsThresh[numTurns][0]) )/2
            while abs(nicoPrior - nicoSR) > 50:
                if (nicoPrior - nicoSR) > 0:
                    nicoSR = nicoSR + 5
                else:
                    nicoSR = nicoSR - 5
            if nicoSR > 150:
                nicoSR = 150
            elif nicoSR < 50:
                nicoSR = 50
'''

def calcSR(userMean, numTurns, entrain, userid, date):
    nicobase = 100
    nicoPrior = getPriorSR(userid, numTurns)
    range = 0.2
    adaptThresh = 65
    userConvert = 0
    numTurnsThresh = {1: .3, 2: .5, 3: .6, 4: .8}

    if "entrain" not in entrain or numTurns == 0:
        nicoSR = nicobase
    else:
        urange = [userMean - range, userMean + range]
        nicoEstRange, userConvert = convertSR(urange, userMean)
        #numTurnsThresh = {1: [40, 50], 2: [30, 40], 3: [20, 30], 4: [10, 20], 5: [5, 10], 6: [0, 5]}


        userNicoDist = math.fabs(nicoPrior - userConvert)

        # Decide if adapt from baseline first OR if maintaining a certain distance from the user
        if userConvert < nicoPrior and numTurns in numTurnsThresh:
            nicoSR = nicoPrior - (userNicoDist)*numTurnsThresh[numTurns]
        elif userConvert > nicoPrior and numTurns in numTurnsThresh:
            nicoSR = nicoPrior + (userNicoDist)*numTurnsThresh[numTurns]
        elif userConvert == nicoPrior:
            nicoSR = userConvert
        else:
            if userNicoDist > adaptThresh and userConvert > nicoPrior:
                nicoSR = nicoPrior + 50
            elif userNicoDist > adaptThresh and userConvert < nicoPrior:
                nicoSR = nicoPrior - 50
            else:
                nicoSR = userConvert


    line = "speaking rate, " + str(userMean) + "," + str(userConvert) + "," + str(nicoPrior) + ","  + str(nicoSR) + "," + str(numTurns) + "\n"
    verbalManagementLogging.writeLog(userid, date, line)
    verbalManagementLogging.writeNicoSR(nicoSR)
    return int(round(nicoSR))

def convertSR(urange, userMean):
    slope = 33
    intercept = -49
    nicorange = [(urange[0]*slope + intercept),(urange[1]*slope + intercept)]
    userConvert = userMean*slope + intercept
    if userConvert > 150: userConvert = 150
    if userConvert < 60: userConvert = 60
    return nicorange, userConvert

def getPriorSR(userid, numTurns):
    if numTurns == 0:
        nicoPrior = 100
    else:
        nicoPrior = verbalManagementLogging.readLoggedSR(userid)

    return nicoPrior



'''
----------------------------------------------Pitch v2 CALCULATIONS------------------------------------------------

calcSR:
Needs to calculate pitch shift; praat range is 75 - 350; Nico range is 75 to 130. Default is 100
Convert user pitch to Nico range
Given # of turns, validity of the values, and the difference from prior turn (nico's), figure out range for Nico
Take average of range and shift pitch to that.
'''

def calcPitch_v2(userMean, numTurns, entrain, userid, date):
    nicobase = 100
    nicoPrior = getPriorPitch(userid, numTurns)
    range = 15
    userConvert = 0
    numTurnsThresh = {1: .1, 2: .2, 3: .3, 4: .4, 5: .5}
    maxEntrainPercent = 0.5

    if "entrain" not in entrain or numTurns == 0:
        nicoPitch = nicobase
    else:
        urange = [userMean - range, userMean + range]
        nicoEstRange, userConvert = convertPitch(urange, userMean)

        userNicoDist = math.fabs(nicoPrior - userConvert)

        if numTurns in numTurnsThresh:
            if userConvert > nicoPrior:
                nicoPitch = nicoPrior + (userNicoDist)*numTurnsThresh[numTurns]
            else:
                nicoPitch = nicoPrior - (userNicoDist)*numTurnsThresh[numTurns]
        else:
            if userConvert > nicoPrior:
                nicoPitch = nicoPrior + (userNicoDist) * maxEntrainPercent
            else:
                nicoPitch = nicoPrior - (userNicoDist) * maxEntrainPercent


    line = "pitch," + str(userMean) + "," + str(userConvert) + "," + str(nicoPrior) + ","  + str(nicoPitch) + "," + str(numTurns) + "\n"
    verbalManagementLogging.writeLog(userid, date, line)
    verbalManagementLogging.writeNicoPitch(nicoPitch)
    return int(round(nicoPitch))

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
        nicoPrior = 100
    else:
        nicoPrior = verbalManagementLogging.readLoggedPitch(userid)

    return nicoPrior