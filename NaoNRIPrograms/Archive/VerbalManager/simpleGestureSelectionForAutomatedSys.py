from Tkinter import *
import sys
from naoqi import ALProxy
from naoqi import motion
import time
import almath
import random

import threading
from threading import Thread


##_________________________________API & NAO Settings______________________________________##

robotIP = "10.218.104.125"
PORT = 9559

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



##_________________________________ALL MOVEMENT FUNCTIONS______________________________________##

##_________________________________STIFFNESS______________________________________##


def stiffnessOff():
    pNames = "Body"
    pStiffnessLists = 0.0
    pTimeLists = 1.0
    motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


#stiffnessOff = Button(content, text="OFF", command=stiffnessOff)


def stiffnessOn():
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


#stiffnessOn = Button(content, text="ON", command=stiffnessOn)


##_________________________________HEAD STUFF______________________________________##

def moveHead():
    pitch = enHpitch.get()
    yaw = enHyaw.get()
    motionProxy.setStiffnesses("Head", 1.0)
    names = ["HeadYaw", "HeadPitch"]
    angles = [float(yaw) * almath.TO_RAD, float(pitch) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(3.0)
    motionProxy.setStiffnesses("Head", 0.0)


def moveHead2(pitch, yaw):
    motionProxy.setStiffnesses("Head", 1.0)
    names = ["HeadYaw", "HeadPitch"]
    angles = [float(yaw) * almath.TO_RAD, float(pitch) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(3.0)
    motionProxy.setStiffnesses("Head", 0.0)


# # HEAD
# Hpitch = Label(content, text="Head pitch:")
# enHpitch = Entry(content)
#
# Hyaw = Label(content, text="Head yaw:")
# enHyaw = Entry(content)

#apply1 = Button(content, text="APPLY", width=10, command=moveHead)


##_________________________________LEFT ARM STUFF______________________________________##

def moveLeftArm():
    shoulderPitch = enLSpitch.get()
    shoulderRoll = enLSroll.get()
    elbowYaw = enLEyaw.get()
    elbowRoll = enLEroll.get()
    wristYaw = enLWyaw.get()

    motionProxy.setStiffnesses("LArm", 1.0)
    names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
    angles = [float(shoulderPitch) * almath.TO_RAD, float(shoulderRoll) * almath.TO_RAD,
              float(elbowYaw) * almath.TO_RAD, float(elbowRoll) * almath.TO_RAD, float(wristYaw) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)


def moveLeftArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):
    motionProxy.setStiffnesses("LArm", 1.0)
    names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
    angles = [float(shoulderPitch) * almath.TO_RAD, float(shoulderRoll) * almath.TO_RAD,
              float(elbowYaw) * almath.TO_RAD, float(elbowRoll) * almath.TO_RAD, float(wristYaw) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)


# # LEFT ARM
# LSpitch = Label(content, text="Left Shoulder pitch: ")
# enLSpitch = Entry(content)
#
# LSroll = Label(content, text="Left Shoulder roll: ")
# enLSroll = Entry(content)
#
# LEyaw = Label(content, text="Left Elbow yaw: ")
# enLEyaw = Entry(content)
#
# LEroll = Label(content, text="Left Elbow roll: ")
# enLEroll = Entry(content)
#
# LWyaw = Label(content, text="Left Wrist yaw: ")
# enLWyaw = Entry(content)

#apply2 = Button(content, text="APPLY", width=10, command=moveLeftArm)


##_________________________________RIGHT ARM STUFF______________________________________##


def moveRightArm():
    shoulderPitch = enRSpitch.get()
    shoulderRoll = enRSroll.get()
    elbowYaw = enREyaw.get()
    elbowRoll = enREroll.get()
    wristYaw = enRWyaw.get()

    motionProxy.setStiffnesses("RArm", 1.0)
    names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    angles = [float(shoulderPitch) * almath.TO_RAD, float(shoulderRoll) * almath.TO_RAD,
              float(elbowYaw) * almath.TO_RAD, float(elbowRoll) * almath.TO_RAD, float(wristYaw) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    # time.sleep(3.0)
    # motionProxy.setStiffnesses("LArm", 0.0)


def moveRightArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):
    motionProxy.setStiffnesses("RArm", 1.0)
    names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    angles = [float(shoulderPitch) * almath.TO_RAD, float(shoulderRoll) * almath.TO_RAD,
              float(elbowYaw) * almath.TO_RAD, float(elbowRoll) * almath.TO_RAD, float(wristYaw) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    # time.sleep(3.0)
    # motionProxy.setStiffnesses("LArm", 0.0)


# RIGHT ARM


#apply3 = Button(content, text="APPLY", width=10, command=moveRightArm)


##_________________________________FULL BODY STUFF______________________________________##


def moveBody():
    pitch = enHpitch.get()
    yaw = enHyaw.get()

    lshoulderPitch = enLSpitch.get()
    lshoulderRoll = enLSroll.get()
    lelbowYaw = enLEyaw.get()
    lelbowRoll = enLEroll.get()
    lwristYaw = enLWyaw.get()

    rshoulderPitch = enRSpitch.get()
    rshoulderRoll = enRSroll.get()
    relbowYaw = enREyaw.get()
    relbowRoll = enREroll.get()
    rwristYaw = enRWyaw.get()

    motionProxy.setStiffnesses("Body", 1.0)
    names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
             "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    angles = [float(yaw) * almath.TO_RAD, float(pitch) * almath.TO_RAD,
              float(lshoulderPitch) * almath.TO_RAD, float(lshoulderRoll) * almath.TO_RAD,
              float(lelbowYaw) * almath.TO_RAD, float(lelbowRoll) * almath.TO_RAD, float(lwristYaw) * almath.TO_RAD,
              float(rshoulderPitch) * almath.TO_RAD, float(rshoulderRoll) * almath.TO_RAD,
              float(relbowYaw) * almath.TO_RAD, float(relbowRoll) * almath.TO_RAD, float(rwristYaw) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)


def moveBody2(yaw, pitch, lshoulderPitch, lshoulderRoll, lelbowYaw, lelbowRoll, lwristYaw, rshoulderPitch,
              rshoulderRoll, relbowYaw, relbowRoll, rwristYaw):
    motionProxy.setStiffnesses("Body", 1.0)
    names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
             "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    angles = [float(yaw) * almath.TO_RAD, float(pitch) * almath.TO_RAD,
              float(lshoulderPitch) * almath.TO_RAD, float(lshoulderRoll) * almath.TO_RAD,
              float(lelbowYaw) * almath.TO_RAD, float(lelbowRoll) * almath.TO_RAD, float(lwristYaw) * almath.TO_RAD,
              float(rshoulderPitch) * almath.TO_RAD, float(rshoulderRoll) * almath.TO_RAD,
              float(relbowYaw) * almath.TO_RAD, float(relbowRoll) * almath.TO_RAD, float(rwristYaw) * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)


#applyAll = Button(content, text="APPLY ALL", width=10, command=moveBody)


##________________________________HANDS______________________________________##


def openRHand():
    motionProxy.openHand('RHand')


def closeRHand():
    motionProxy.closeHand('RHand')


def openLHand():
    motionProxy.openHand('LHand')


def closeLHand():
    motionProxy.openHand('LHand')


def openHands():
    openRHand()
    openLHand()


def closeHands():
    closeRHand()
    closeLHand()


##_________________________________REALISTIC GESTURES______________________________________##


def yawnAndStretch():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD, 15.5 * almath.TO_RAD, 0.0 * almath.TO_RAD],
                  [-11.5 * almath.TO_RAD, 18.3 * almath.TO_RAD, -30.5 * almath.TO_RAD],

                  [-41.9 * almath.TO_RAD, -119.5 * almath.TO_RAD, -89.8 * almath.TO_RAD],
                  [29.9 * almath.TO_RAD, 18.4 * almath.TO_RAD, 61.4 * almath.TO_RAD],
                  [-52.4 * almath.TO_RAD, -19.4 * almath.TO_RAD, -45.3 * almath.TO_RAD],
                  [-88.5 * almath.TO_RAD, -84.4 * almath.TO_RAD, -2.0 * almath.TO_RAD],
                  [-51.1 * almath.TO_RAD, -44.5 * almath.TO_RAD, 4.2 * almath.TO_RAD],
                  [0],

                  [-55.7 * almath.TO_RAD, -110.1 * almath.TO_RAD, -62.4 * almath.TO_RAD],
                  [-35.2 * almath.TO_RAD, -23.7 * almath.TO_RAD, -61.8 * almath.TO_RAD],
                  [33.8 * almath.TO_RAD, 23.6 * almath.TO_RAD, 59.6 * almath.TO_RAD],
                  [88.5 * almath.TO_RAD, 88.2 * almath.TO_RAD, 2.4 * almath.TO_RAD],
                  [61.7 * almath.TO_RAD, 58.9 * almath.TO_RAD, 18.6 * almath.TO_RAD],
                  [0]]

    timeLists = [[1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],

                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5],

                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5, 3.5, 5.5],
                 [1.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("eawyn")
    time.sleep(1.0)


def lookAtNailsLeft():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD, 15.7 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD, -17.4 * almath.TO_RAD],

                  [81.0 * almath.TO_RAD, -8.9 * almath.TO_RAD],
                  [8.0 * almath.TO_RAD, 2.9 * almath.TO_RAD],
                  [-45.0 * almath.TO_RAD, -60.2 * almath.TO_RAD],
                  [-60.0 * almath.TO_RAD, -88.7 * almath.TO_RAD],
                  [8.7 * almath.TO_RAD, -56.6 * almath.TO_RAD, 84.6 * almath.TO_RAD],
                  [0, 1],

                  [81.0 * almath.TO_RAD],
                  [-7.0 * almath.TO_RAD],
                  [45.0 * almath.TO_RAD],
                  [60.0 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    timeLists = [[0.5, 2.0],
                 [0.5, 2.0],

                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0, 3.0],
                 [0.5, 2.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("hum")
    time.sleep(1.0)


def lookAtNailsRight():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD, -5.7 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD, 17.4 * almath.TO_RAD],

                  [79.0 * almath.TO_RAD],
                  [10.0 * almath.TO_RAD],
                  [-47.0 * almath.TO_RAD],
                  [-60.0 * almath.TO_RAD],
                  [8.0 * almath.TO_RAD],
                  [0],

                  [81.0 * almath.TO_RAD, 48.9 * almath.TO_RAD],
                  [-7.0 * almath.TO_RAD, -2.9 * almath.TO_RAD],
                  [45.0 * almath.TO_RAD, 60.2 * almath.TO_RAD],
                  [60.0 * almath.TO_RAD, 88.7 * almath.TO_RAD],
                  [1.0 * almath.TO_RAD, 56.6 * almath.TO_RAD, -104.6 * almath.TO_RAD],
                  [0, 1]]

    timeLists = [[0.5, 2.0],
                 [0.5, 2.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0, 3.0],
                 [0.5, 3.0]]
    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("hum")
    time.sleep(1.0)


def handOutLeft():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [62.1 * almath.TO_RAD],
                  [-1.2 * almath.TO_RAD],
                  [-110.7 * almath.TO_RAD],
                  [-49.2 * almath.TO_RAD],
                  [-69.8 * almath.TO_RAD],
                  [1],

                  [80.7 * almath.TO_RAD],
                  [0.2 * almath.TO_RAD],
                  [54.8 * almath.TO_RAD],
                  [49.6 * almath.TO_RAD],
                  [4.3 * almath.TO_RAD],
                  [0]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("She ran three kilometers")
    time.sleep(1.0)


def handOutRight():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [79.8 * almath.TO_RAD],
                  [5.1 * almath.TO_RAD],
                  [-52.5 * almath.TO_RAD],
                  [-46.8 * almath.TO_RAD],
                  [-26.6 * almath.TO_RAD],
                  [0],

                  [66.5 * almath.TO_RAD],
                  [4.5 * almath.TO_RAD],
                  [109.5 * almath.TO_RAD],
                  [66.1 * almath.TO_RAD],
                  [71.8 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("So in 18 minutes she will be 6 kilometers away.")
    time.sleep(1.0)


def largeShrug():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [65.0 * almath.TO_RAD, 65.0 * almath.TO_RAD],
                  [-4.0 * almath.TO_RAD, -4.0 * almath.TO_RAD],
                  [-119.8 * almath.TO_RAD, -119.8 * almath.TO_RAD],
                  [-79.8 * almath.TO_RAD, -79.8 * almath.TO_RAD],
                  [-49.6 * almath.TO_RAD, -49.6 * almath.TO_RAD],
                  [1],

                  [65.0 * almath.TO_RAD, 65.0 * almath.TO_RAD],
                  [4.0 * almath.TO_RAD, 4.0 * almath.TO_RAD],
                  [119.8 * almath.TO_RAD, 119.8 * almath.TO_RAD],
                  [79.8 * almath.TO_RAD, 79.8 * almath.TO_RAD],
                  [49.6 * almath.TO_RAD, 49.6 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I don't know how to solve it")
    time.sleep(1.0)


def handsOnHips():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [75.0 * almath.TO_RAD],
                  [27.0 * almath.TO_RAD],
                  [-5.8 * almath.TO_RAD],
                  [-86.8 * almath.TO_RAD],
                  [0.6 * almath.TO_RAD],
                  [0],

                  [84.0 * almath.TO_RAD],
                  [-29.9 * almath.TO_RAD],
                  [18.5 * almath.TO_RAD],
                  [79.2 * almath.TO_RAD],
                  [1.8 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]
    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know what to do!")
    time.sleep(1.0)


def waveLeft():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [-2.3 * almath.TO_RAD],
                  [18.4 * almath.TO_RAD],
                  [-73.5 * almath.TO_RAD, -112.5 * almath.TO_RAD, -73.5 * almath.TO_RAD, -112.5 * almath.TO_RAD],
                  [-85.8 * almath.TO_RAD],
                  [42.2 * almath.TO_RAD],
                  [1],

                  [80.8 * almath.TO_RAD],
                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.2 * almath.TO_RAD],
                  [-10.8 * almath.TO_RAD],
                  [0]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5, 1.0, 1.5, 2.0],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Hello! Nice to meet you.")
    time.sleep(1.0)


def waveRight():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [80.0 * almath.TO_RAD],
                  [6.5 * almath.TO_RAD],
                  [-46.8 * almath.TO_RAD],
                  [-57.8 * almath.TO_RAD],
                  [7.6 * almath.TO_RAD],
                  [0],

                  [2.3 * almath.TO_RAD],
                  [-18.9 * almath.TO_RAD],
                  [73.5 * almath.TO_RAD, 112.5 * almath.TO_RAD, 73.5 * almath.TO_RAD, 112.5 * almath.TO_RAD],
                  [86.2 * almath.TO_RAD],
                  [-66.8 * almath.TO_RAD],
                  [1]]


    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5, 1.0, 1.5, 2.0],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Hello! Nice to meet you.")
    time.sleep(1.0)


def nodYes():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [11.3 * almath.TO_RAD, -11.3 * almath.TO_RAD, 11.3 * almath.TO_RAD, -11.3 * almath.TO_RAD,
                   0.0 * almath.TO_RAD],

                  [80.9 * almath.TO_RAD],
                  [8.3 * almath.TO_RAD],
                  [-45.3 * almath.TO_RAD],
                  [-60.4 * almath.TO_RAD],
                  [8.7 * almath.TO_RAD],
                  [0],

                  [80.8 * almath.TO_RAD],
                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.1 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5, 1.0, 1.5, 2.0, 2.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.5],

                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Yes, I agree")
    time.sleep(1.0)


def shakeNo():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [
        [18.3 * almath.TO_RAD, -18.3 * almath.TO_RAD, 18.3 * almath.TO_RAD, -18.3 * almath.TO_RAD, 0.0 * almath.TO_RAD],
        [0.0 * almath.TO_RAD],

        [80.9 * almath.TO_RAD],
        [8.3 * almath.TO_RAD],
        [-45.3 * almath.TO_RAD],
        [-60.4 * almath.TO_RAD],
        [8.7 * almath.TO_RAD],
        [0],

        [80.8 * almath.TO_RAD],
        [-8.4 * almath.TO_RAD],
        [45.1 * almath.TO_RAD],
        [60.1 * almath.TO_RAD],
        [-10.6 * almath.TO_RAD],
        [0]]

    # *almath.TO_RAD
    timeLists = [[0.5, 1.0, 1.5, 2.0, 2.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I don't think that's right")
    time.sleep(1.0)


def lookLeft():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[14.3 * almath.TO_RAD],
                  [22.9 * almath.TO_RAD],

                  [39.9 * almath.TO_RAD, 49.9 * almath.TO_RAD],
                  [30.2 * almath.TO_RAD, 40.9 * almath.TO_RAD, 30.2 * almath.TO_RAD],
                  [-60.5 * almath.TO_RAD],
                  [-2.0 * almath.TO_RAD],
                  [28.1 * almath.TO_RAD],
                  [1],

                  [80.8 * almath.TO_RAD],
                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.1 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [1.5, 2.5],
                 [1.5, 2.5, 3.0],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Take a look at the screen here!")
    time.sleep(1.0)


def lookRight():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[-14.3 * almath.TO_RAD],
                  [22.9 * almath.TO_RAD],

                  [80.8 * almath.TO_RAD],
                  [8.4 * almath.TO_RAD],
                  [-45.1 * almath.TO_RAD],
                  [-60.1 * almath.TO_RAD],
                  [8.6 * almath.TO_RAD],
                  [0],

                  [39.9 * almath.TO_RAD, 49.9 * almath.TO_RAD],
                  [-30.2 * almath.TO_RAD, -40.9 * almath.TO_RAD, -30.9 * almath.TO_RAD],
                  [60.5 * almath.TO_RAD],
                  [2.0 * almath.TO_RAD],
                  [-28.1 * almath.TO_RAD],
                  [1]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [1.5, 2.5],
                 [1.5, 2.5, 3.0],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Take a look at the screen here!")
    time.sleep(1.0)


def facepalmLeft():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [20.0 * almath.TO_RAD],

                  [8.5 * almath.TO_RAD, 28.3 * almath.TO_RAD],
                  [-18.2 * almath.TO_RAD, -9.1 * almath.TO_RAD],
                  [-59.3 * almath.TO_RAD, -101.0 * almath.TO_RAD],
                  [-88.5 * almath.TO_RAD, -85.7 * almath.TO_RAD],
                  [-63.4 * almath.TO_RAD, -61.2 * almath.TO_RAD],
                  [1],

                  [80.8 * almath.TO_RAD],
                  [-3.3 * almath.TO_RAD],
                  [50.9 * almath.TO_RAD],
                  [55.1 * almath.TO_RAD],
                  [-5.0 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5, 1.0],
                 [0.5, 1.0],
                 [0.5, 1.0],
                 [0.5, 1.0],
                 [0.5, 1.0],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I can't believe I didn't see that before!")
    time.sleep(1.0)


def facepalmRight():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [20.0 * almath.TO_RAD],

                  [79.9 * almath.TO_RAD],
                  [9.3 * almath.TO_RAD],
                  [-46.3 * almath.TO_RAD],
                  [-58.8 * almath.TO_RAD],
                  [7.7 * almath.TO_RAD],
                  [0],

                  [1.5 * almath.TO_RAD, 28.3 * almath.TO_RAD],
                  [12.2 * almath.TO_RAD, 9.1 * almath.TO_RAD],
                  [55.3 * almath.TO_RAD, 101.0 * almath.TO_RAD],
                  [88.5 * almath.TO_RAD, 85.7 * almath.TO_RAD],
                  [68.4 * almath.TO_RAD, 61.2 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5, 1.0],
                 [0.5, 1.0],
                 [0.5, 1.0],
                 [0.5, 1.0],
                 [0.5, 1.0],
                 [1.0]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I can't believe I didn't see that before!")
    time.sleep(1.0)


def cantHearLeft():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[-30.3 * almath.TO_RAD],
                  [5.7 * almath.TO_RAD],

                  [38.8 * almath.TO_RAD],
                  [12.0 * almath.TO_RAD],
                  [-86.5 * almath.TO_RAD],
                  [-87.7 * almath.TO_RAD],
                  [8.6 * almath.TO_RAD],
                  [1],

                  [80.8 * almath.TO_RAD],
                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.1 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I didn't hear you, can you repeat that?")
    time.sleep(1.0)


def cantHearRight():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[30.3 * almath.TO_RAD],
                  [5.7 * almath.TO_RAD],

                  [79.9 * almath.TO_RAD],
                  [9.3 * almath.TO_RAD],
                  [-46.3 * almath.TO_RAD],
                  [-58.8 * almath.TO_RAD],
                  [7.7 * almath.TO_RAD],
                  [0],

                  [35.2 * almath.TO_RAD],
                  [-9.0 * almath.TO_RAD],
                  [65.8 * almath.TO_RAD],
                  [87.1 * almath.TO_RAD],
                  [11.4 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I didn't hear you, can you repeat that?")
    time.sleep(1.0)


def handOnChestLeft():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [44.9 * almath.TO_RAD],
                  [-11.5 * almath.TO_RAD],
                  [-30.2 * almath.TO_RAD],
                  [-86.5 * almath.TO_RAD],
                  [-36.6 * almath.TO_RAD],
                  [1],

                  [79.8 * almath.TO_RAD],
                  [-10.4 * almath.TO_RAD],
                  [46.1 * almath.TO_RAD],
                  [58.1 * almath.TO_RAD],
                  [-7.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know the answer!")
    time.sleep(1.0)


def handOnChestRight():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [76.9 * almath.TO_RAD],
                  [0.3 * almath.TO_RAD],
                  [-44.3 * almath.TO_RAD],
                  [-46.1 * almath.TO_RAD],
                  [-12.9 * almath.TO_RAD],
                  [0],

                  [43.9 * almath.TO_RAD],
                  [9.7 * almath.TO_RAD],
                  [22.7 * almath.TO_RAD],
                  [88.5 * almath.TO_RAD],
                  [51.8 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know the answer!")
    time.sleep(1.0)


def handsOut():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [12.4 * almath.TO_RAD],
                  [19.1 * almath.TO_RAD],
                  [-119.5 * almath.TO_RAD],
                  [-82.5 * almath.TO_RAD],
                  [39.9 * almath.TO_RAD],
                  [1],

                  [9.5 * almath.TO_RAD],
                  [-19.8 * almath.TO_RAD],
                  [119.1 * almath.TO_RAD],
                  [87.0 * almath.TO_RAD],
                  [-49.5 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know the answer!")
    time.sleep(1.0)


def cheering():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [56.2 * almath.TO_RAD],
                  [-9.9 * almath.TO_RAD, -18.0 * almath.TO_RAD],
                  [-60.9 * almath.TO_RAD, -65.9 * almath.TO_RAD],
                  [-88.5 * almath.TO_RAD],
                  [5.7 * almath.TO_RAD],
                  [0, 1],

                  [60.7 * almath.TO_RAD],
                  [18.0 * almath.TO_RAD, 11.9 * almath.TO_RAD],
                  [66.7 * almath.TO_RAD, 62.7 * almath.TO_RAD],
                  [88.5 * almath.TO_RAD],
                  [-21.8 * almath.TO_RAD],
                  [0, 1]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5],
                 [0.5],
                 [0.5, 1.0],

                 [0.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5],
                 [0.5],
                 [0.5, 1.0]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("We did it!")
    time.sleep(1.0)


def handsOnHead():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [
        [10.3 * almath.TO_RAD, -10.3 * almath.TO_RAD, 10.3 * almath.TO_RAD, -10.3 * almath.TO_RAD, 0.0 * almath.TO_RAD],
        [20.0 * almath.TO_RAD],

        [-9.7 * almath.TO_RAD],
        [-4.1 * almath.TO_RAD],
        [-69.2 * almath.TO_RAD],
        [-87.8 * almath.TO_RAD],
        [-61.9 * almath.TO_RAD],
        [0],

        [-15.2 * almath.TO_RAD],
        [-1.1 * almath.TO_RAD],
        [62.3 * almath.TO_RAD],
        [87.8 * almath.TO_RAD],
        [68.3 * almath.TO_RAD],
        [0]]

    timeLists = [[0.5, 1.0, 1.5, 2.0, 2.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("This is really confusing!")
    time.sleep(1.0)


##_________________________________CARTOON GESTURES______________________________________##
##_______________________________________________________________________________________##
##_______________________________________________________________________________________##


def lookAtNailsLeft2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD, 15.7 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD, -13.4 * almath.TO_RAD],

                  [81.0 * almath.TO_RAD, -8.9 * almath.TO_RAD, -3.2 * almath.TO_RAD],
                  [8.0 * almath.TO_RAD, 2.9 * almath.TO_RAD, 22.7 * almath.TO_RAD],
                  [-45.0 * almath.TO_RAD, -60.2 * almath.TO_RAD, -69.5 * almath.TO_RAD],
                  [-60.0 * almath.TO_RAD, -88.7 * almath.TO_RAD, -40.5 * almath.TO_RAD],
                  [8.7 * almath.TO_RAD, -56.6 * almath.TO_RAD, 104.6 * almath.TO_RAD],
                  [0, 1],

                  [81.0 * almath.TO_RAD],
                  [-7.0 * almath.TO_RAD],
                  [45.0 * almath.TO_RAD],
                  [60.0 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    timeLists = [[0.5, 2.0],
                 [0.5, 2.0],

                 [0.5, 2.0, 4.0],
                 [0.5, 2.0, 4.0],
                 [0.5, 2.0, 4.0],
                 [0.5, 2.0, 4.0],
                 [0.5, 2.0, 4.0],
                 [0.5, 2.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("hum")
    time.sleep(1.0)



def lookAtNailsRight2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD, -5.7 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD, 17.4 * almath.TO_RAD],

                  [79.0 * almath.TO_RAD],
                  [10.0 * almath.TO_RAD],
                  [-47.0 * almath.TO_RAD],
                  [-60.0 * almath.TO_RAD],
                  [8.0 * almath.TO_RAD],
                  [0],

                  [81.0 * almath.TO_RAD, 48.9 * almath.TO_RAD],
                  [-7.0 * almath.TO_RAD, -2.9 * almath.TO_RAD],
                  [45.0 * almath.TO_RAD, 60.2 * almath.TO_RAD],
                  [60.0 * almath.TO_RAD, 88.7 * almath.TO_RAD],
                  [1.0 * almath.TO_RAD, 56.6 * almath.TO_RAD, -104.6 * almath.TO_RAD],
                  [0, 1]]

    timeLists = [[0.5, 2.0],
                 [0.5, 2.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0, 3.0],
                 [0.5, 3.0]]
    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("hum")
    time.sleep(1.0)


def handOutLeft2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [48.5 * almath.TO_RAD, 62.1 * almath.TO_RAD],
                  [8.3 * almath.TO_RAD, -1.2 * almath.TO_RAD],
                  [-119.5 * almath.TO_RAD, -110.7 * almath.TO_RAD],
                  [-76.6 * almath.TO_RAD, -69.2 * almath.TO_RAD],
                  [-68.4 * almath.TO_RAD, -69.8 * almath.TO_RAD],
                  [0, 1],

                  [80.7 * almath.TO_RAD],
                  [0.2 * almath.TO_RAD],
                  [54.8 * almath.TO_RAD],
                  [49.6 * almath.TO_RAD],
                  [4.3 * almath.TO_RAD],
                  [0]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("She ran three kilometers")
    time.sleep(1.0)


def handOutRight2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [80.0 * almath.TO_RAD],
                  [6.5 * almath.TO_RAD],
                  [-46.8 * almath.TO_RAD],
                  [-57.8 * almath.TO_RAD],
                  [7.6 * almath.TO_RAD],
                  [0],

                  [32.5 * almath.TO_RAD, 62.1 * almath.TO_RAD],
                  [-8.3 * almath.TO_RAD, 1.2 * almath.TO_RAD],
                  [95.5 * almath.TO_RAD, 110.7 * almath.TO_RAD],
                  [76.6 * almath.TO_RAD, 69.2 * almath.TO_RAD],
                  [79.4 * almath.TO_RAD, 69.8 * almath.TO_RAD],
                  [0, 1]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("So in 18 minutes she will be 6 kilometers away.")
    time.sleep(1.0)


def largeShrug2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [39.0 * almath.TO_RAD, 39.0 * almath.TO_RAD],
                  [9.0 * almath.TO_RAD, 9.0 * almath.TO_RAD],
                  [-119.8 * almath.TO_RAD, -119.8 * almath.TO_RAD],
                  [-84.8 * almath.TO_RAD, -84.8 * almath.TO_RAD],
                  [-55.6 * almath.TO_RAD, -55.6 * almath.TO_RAD],
                  [1],

                  [36.0 * almath.TO_RAD, 36.0 * almath.TO_RAD],
                  [-16.9 * almath.TO_RAD, -16.9 * almath.TO_RAD],
                  [119.5 * almath.TO_RAD, 119.5 * almath.TO_RAD],
                  [86.2 * almath.TO_RAD, 86.2 * almath.TO_RAD],
                  [55.8 * almath.TO_RAD, 55.8 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I don't know how to solve it")
    time.sleep(1.0)


def handsOnHips2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [71.4 * almath.TO_RAD, 75.0 * almath.TO_RAD],
                  [67.8 * almath.TO_RAD, 27.0 * almath.TO_RAD],
                  [-21.6 * almath.TO_RAD, -5.8 * almath.TO_RAD],
                  [-88.5 * almath.TO_RAD, -86.8 * almath.TO_RAD],
                  [1.2 * almath.TO_RAD, 0.6 * almath.TO_RAD],
                  [0],

                  [71.6 * almath.TO_RAD, 84.0 * almath.TO_RAD],
                  [-67.6 * almath.TO_RAD, -29.9 * almath.TO_RAD],
                  [21.6 * almath.TO_RAD, 18.5 * almath.TO_RAD],
                  [88.6 * almath.TO_RAD, 79.2 * almath.TO_RAD],
                  [6.6 * almath.TO_RAD, 1.8 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5]]
    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know what to do!")
    time.sleep(1.0)


def waveLeft2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [-2.3 * almath.TO_RAD],
                  [18.4 * almath.TO_RAD],
                  [-53.5 * almath.TO_RAD, -122.5 * almath.TO_RAD, -53.5 * almath.TO_RAD, -122.5 * almath.TO_RAD],
                  [-85.8 * almath.TO_RAD],
                  [42.2 * almath.TO_RAD],
                  [1],

                  [80.8 * almath.TO_RAD],
                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.2 * almath.TO_RAD],
                  [-10.8 * almath.TO_RAD],
                  [0]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5, 1.0, 1.5, 2.0],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Hello! Nice to meet you.")
    time.sleep(1.0)


def waveRight2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [80.0 * almath.TO_RAD],
                  [6.5 * almath.TO_RAD],
                  [-46.8 * almath.TO_RAD],
                  [-57.8 * almath.TO_RAD],
                  [7.6 * almath.TO_RAD],
                  [0],

                  [2.3 * almath.TO_RAD],
                  [-18.9 * almath.TO_RAD],
                  [73.5 * almath.TO_RAD, 112.5 * almath.TO_RAD, 73.5 * almath.TO_RAD, 112.5 * almath.TO_RAD],
                  [86.2 * almath.TO_RAD],
                  [-66.8 * almath.TO_RAD],
                  [1]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5, 1.0, 1.5, 2.0],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Hello! Nice to meet you.")
    time.sleep(1.0)


def nodYes2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [20.3 * almath.TO_RAD, -20.3 * almath.TO_RAD, 20.3 * almath.TO_RAD, -20.3 * almath.TO_RAD,
                   0.0 * almath.TO_RAD],


                  [80.9 * almath.TO_RAD],
                  [8.3 * almath.TO_RAD],
                  [-45.3 * almath.TO_RAD],
                  [-60.4 * almath.TO_RAD],
                  [8.7 * almath.TO_RAD],
                  [0],

                  [80.8 * almath.TO_RAD],

                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.1 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5, 1.0, 1.5, 2.0, 2.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Yes, I agree")
    time.sleep(1.0)


def shakeNo2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [
        [28.3 * almath.TO_RAD, -28.3 * almath.TO_RAD, 28.3 * almath.TO_RAD, -25.3 * almath.TO_RAD, 0.0 * almath.TO_RAD],
        [0.0 * almath.TO_RAD],

        [80.9 * almath.TO_RAD],
        [8.3 * almath.TO_RAD],
        [-45.3 * almath.TO_RAD],
        [-60.4 * almath.TO_RAD],
        [8.7 * almath.TO_RAD],
        [0],

        [80.8 * almath.TO_RAD],
        [-8.4 * almath.TO_RAD],
        [45.1 * almath.TO_RAD],
        [60.1 * almath.TO_RAD],
        [-10.6 * almath.TO_RAD],
        [0]]

    # *almath.TO_RAD
    timeLists = [[0.5, 1.0, 1.5, 2.0, 2.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I don't think that's right")
    time.sleep(1.0)


def lookLeft2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[14.3 * almath.TO_RAD],
                  [22.9 * almath.TO_RAD],

                  [39.9 * almath.TO_RAD, 59.9 * almath.TO_RAD],
                  [30.2 * almath.TO_RAD, 50.9 * almath.TO_RAD, 30.2 * almath.TO_RAD],
                  [-60.5 * almath.TO_RAD],
                  [-2.0 * almath.TO_RAD],
                  [28.1 * almath.TO_RAD],
                  [1],

                  [80.8 * almath.TO_RAD],
                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.1 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [1.5, 2.5],
                 [1.5, 2.5, 3.0],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Take a look at the screen here!")
    time.sleep(1.0)


def lookRight2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[-14.3 * almath.TO_RAD],
                  [22.9 * almath.TO_RAD],

                  [80.8 * almath.TO_RAD],
                  [8.4 * almath.TO_RAD],
                  [-45.1 * almath.TO_RAD],
                  [-60.1 * almath.TO_RAD],
                  [8.6 * almath.TO_RAD],
                  [0],

                  [39.9 * almath.TO_RAD, 59.9 * almath.TO_RAD],
                  [-30.2 * almath.TO_RAD, -50.9 * almath.TO_RAD, -30.9 * almath.TO_RAD],
                  [60.5 * almath.TO_RAD],
                  [2.0 * almath.TO_RAD],
                  [-28.1 * almath.TO_RAD],
                  [1]]

    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [1.5, 2.5],
                 [1.5, 2.5, 3.0],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    tts.say("Take a look at the screen here!")
    time.sleep(1.0)


def facepalmLeft2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [20.0 * almath.TO_RAD],

                  [8.5 * almath.TO_RAD, 28.3 * almath.TO_RAD],
                  [-18.2 * almath.TO_RAD, -9.1 * almath.TO_RAD],
                  [-59.3 * almath.TO_RAD, -101.0 * almath.TO_RAD],
                  [-88.5 * almath.TO_RAD, -85.7 * almath.TO_RAD],
                  [-63.4 * almath.TO_RAD, -61.2 * almath.TO_RAD],
                  [1],

                  [80.8 * almath.TO_RAD],
                  [-3.3 * almath.TO_RAD],
                  [50.9 * almath.TO_RAD],
                  [55.1 * almath.TO_RAD],
                  [-5.0 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I can't believe I didn't see that before!")
    time.sleep(1.0)


def facepalmRight2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [20.0 * almath.TO_RAD],

                  [79.9 * almath.TO_RAD],
                  [9.3 * almath.TO_RAD],
                  [-46.3 * almath.TO_RAD],
                  [-58.8 * almath.TO_RAD],
                  [7.7 * almath.TO_RAD],
                  [0],

                  [1.5 * almath.TO_RAD, 28.3 * almath.TO_RAD],
                  [12.2 * almath.TO_RAD, 9.1 * almath.TO_RAD],
                  [55.3 * almath.TO_RAD, 101.0 * almath.TO_RAD],
                  [88.5 * almath.TO_RAD, 85.7 * almath.TO_RAD],
                  [68.4 * almath.TO_RAD, 61.2 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [0.5, 2.0],
                 [1.0]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I can't believe I didn't see that before!")
    time.sleep(1.0)


def cantHearLeft2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[-63.3 * almath.TO_RAD],
                  [5.7 * almath.TO_RAD],

                  [19.8 * almath.TO_RAD],
                  [-2.2 * almath.TO_RAD],
                  [-67.6 * almath.TO_RAD],
                  [-88.5 * almath.TO_RAD],
                  [13.8 * almath.TO_RAD],                  [1]

                  [80.8 * almath.TO_RAD],
                  [-8.4 * almath.TO_RAD],
                  [45.1 * almath.TO_RAD],
                  [60.1 * almath.TO_RAD],
                  [-10.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I didn't hear you, can you repeat that?")
    time.sleep(1.0)


def cantHearRight2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[63.3 * almath.TO_RAD],
                  [-5.7 * almath.TO_RAD],
                  [79.9 * almath.TO_RAD],
                  [9.3 * almath.TO_RAD],
                  [-46.3 * almath.TO_RAD],
                  [-58.8 * almath.TO_RAD],
                  [7.7 * almath.TO_RAD],
                  [0],

                  [9.7 * almath.TO_RAD],
                  [-6.3 * almath.TO_RAD],
                  [64.6 * almath.TO_RAD],
                  [87.5 * almath.TO_RAD],
                  [-13.8 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I didn't hear you, can you repeat that?")
    time.sleep(1.0)


def handOnChestLeft2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [44.9 * almath.TO_RAD],
                  [-11.5 * almath.TO_RAD],
                  [-30.2 * almath.TO_RAD],
                  [-86.5 * almath.TO_RAD],
                  [-36.6 * almath.TO_RAD],
                  [1],

                  [79.8 * almath.TO_RAD],
                  [-10.4 * almath.TO_RAD],
                  [46.1 * almath.TO_RAD],
                  [58.1 * almath.TO_RAD],
                  [-7.6 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know the answer!")
    time.sleep(1.0)



def handOnChestRight2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [0.0 * almath.TO_RAD],

                  [76.9 * almath.TO_RAD],
                  [0.3 * almath.TO_RAD],
                  [-44.3 * almath.TO_RAD],
                  [-46.1 * almath.TO_RAD],
                  [-12.9 * almath.TO_RAD],
                  [0],

                  [43.9 * almath.TO_RAD],
                  [9.7 * almath.TO_RAD],
                  [22.7 * almath.TO_RAD],
                  [88.5 * almath.TO_RAD],
                  [51.8 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [[0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know the answer!")
    time.sleep(1.0)



def cheering2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[0.0 * almath.TO_RAD],
                  [-11.5 * almath.TO_RAD],

                  [-40.5 * almath.TO_RAD, -62.3 * almath.TO_RAD, -40.5 * almath.TO_RAD, -62.3 * almath.TO_RAD],
                  [47.9 * almath.TO_RAD, 14.7 * almath.TO_RAD, 47.9 * almath.TO_RAD, 14.7 * almath.TO_RAD],
                  [-54.4 * almath.TO_RAD, -60.4 * almath.TO_RAD, -54.4 * almath.TO_RAD, -60.4 * almath.TO_RAD],
                  [-83.7 * almath.TO_RAD, -54.9 * almath.TO_RAD, -83.7 * almath.TO_RAD, -54.9 * almath.TO_RAD],
                  [-37.7 * almath.TO_RAD, -37.1 * almath.TO_RAD, -37.7 * almath.TO_RAD, -37.1 * almath.TO_RAD],
                  [0],

                  [-22.0 * almath.TO_RAD, -62.3 * almath.TO_RAD, -22.0 * almath.TO_RAD, -62.3 * almath.TO_RAD],
                  [-48.5 * almath.TO_RAD, -14.7 * almath.TO_RAD, -48.5 * almath.TO_RAD, -14.7 * almath.TO_RAD],
                  [64.5 * almath.TO_RAD, 60.4 * almath.TO_RAD, 64.5 * almath.TO_RAD, 60.4 * almath.TO_RAD],
                  [88.7 * almath.TO_RAD, 54.9 * almath.TO_RAD, 88.7 * almath.TO_RAD, 54.9 * almath.TO_RAD],
                  [37.9 * almath.TO_RAD, 37.1 * almath.TO_RAD, 37.9 * almath.TO_RAD, 37.1 * almath.TO_RAD],
                  [0]]

    timeLists = [[0.5],
                 [0.5],

                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [0.5],

                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [1.0, 1.5, 2.0, 2.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("We did it!")
    time.sleep(1.0)


def handsOnHead2():
    names = ["HeadYaw", "HeadPitch",
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [
        [15.3 * almath.TO_RAD, -15.3 * almath.TO_RAD, 15.3 * almath.TO_RAD, -15.3 * almath.TO_RAD, 0.0 * almath.TO_RAD],
        [20.0 * almath.TO_RAD],

        [-9.7 * almath.TO_RAD],
        [19.5 * almath.TO_RAD, -4.1 * almath.TO_RAD],
        [-81.1 * almath.TO_RAD, -69.2 * almath.TO_RAD],
        [-67.8 * almath.TO_RAD, -87.8 * almath.TO_RAD],
        [-76.1 * almath.TO_RAD, -61.9 * almath.TO_RAD],
        [0],

        [-15.2 * almath.TO_RAD],
        [-19.5 * almath.TO_RAD, -1.1 * almath.TO_RAD],
        [81.1 * almath.TO_RAD, 62.3 * almath.TO_RAD],
        [67.8 * almath.TO_RAD, 87.8 * almath.TO_RAD],
        [76.1 * almath.TO_RAD, 68.3 * almath.TO_RAD],
        [0]]

    timeLists = [[0.5, 1.0, 1.5, 2.0, 2.5],
                 [0.5],

                 [0.5],
                 [1.5, 2.5],
                 [1.5, 2.5],
                 [1.5, 2.5],
                 [1.5, 2.5],
                 [0.5],

                 [0.5],
                 [1.5, 2.5],
                 [1.5, 2.5],
                 [1.5, 2.5],
                 [1.5, 2.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("This is really confusing!")

# Example that finds the difference between the command and sensed angles.
def getAngles():
    HeadYaw = "HeadYaw"
    HeadPitch = "HeadPitch"
    LShoulderPitch = "LShoulderPitch"
    LShoulderRoll = "LShoulderRoll"
    LElbowRoll = "LElbowRoll"
    LElbowYaw = "LElbowYaw"
    LWristYaw = "LWristYaw"
    RShoulderPitch = "RShoulderPitch"
    RShoulderRoll = "RShoulderRoll"
    RElbowRoll = "RElbowRoll"
    RElbowYaw = "RElbowYaw"
    RWristYaw = "RWristYaw"

    useSensors = True
    HeadYawAngle = str(motionProxy.getAngles(HeadYaw, useSensors))[1:5]
    HeadPitchAngle = str(motionProxy.getAngles(HeadPitch, useSensors))[1:5]

    LShoulderPitchAngle = str(motionProxy.getAngles(LShoulderPitch, useSensors))[1:10]
    LShoulderRollAngle = str(motionProxy.getAngles(LShoulderRoll, useSensors))[1:10]
    LElbowRollAngle = str(motionProxy.getAngles(LElbowRoll, useSensors))[1:10]
    LElbowYawAngle = str(motionProxy.getAngles(LElbowYaw, useSensors))[1:10]
    LWristYawAngle = str(motionProxy.getAngles(LWristYaw, useSensors))[1:10]

    RShoulderPitchAngle = str(motionProxy.getAngles(RShoulderPitch, useSensors))[1:10]
    RShoulderRollAngle = str(motionProxy.getAngles(RShoulderRoll, useSensors))[1:10]
    RElbowRollAngle = str(motionProxy.getAngles(RElbowRoll, useSensors))[1:10]
    RElbowYawAngle = str(motionProxy.getAngles(RElbowYaw, useSensors))[1:10]
    RWristYawAngle = str(motionProxy.getAngles(RWristYaw, useSensors))[1:10]

    enHyaw.delete(0, END)
    enHyaw.insert(0, '%.3f' % (float(HeadYawAngle) * almath.TO_DEG))
    enHpitch.delete(0, END)
    enHpitch.insert(0, '%.3f' % (float(HeadPitchAngle) * almath.TO_DEG))

    enLSpitch.delete(0, END)
    enLSpitch.insert(0, '%.3f' % (float(LShoulderPitchAngle) * almath.TO_DEG))
    enLSroll.delete(0, END)
    enLSroll.insert(0, '%.3f' % (float(LShoulderRollAngle) * almath.TO_DEG))
    enLEroll.delete(0, END)
    enLEroll.insert(0, '%.3f' % (float(LElbowRollAngle) * almath.TO_DEG))
    enLEyaw.delete(0, END)
    enLEyaw.insert(0, '%.3f' % (float(LElbowYawAngle) * almath.TO_DEG))
    enLWyaw.delete(0, END)
    enLWyaw.insert(0, '%.3f' % (float(LWristYawAngle) * almath.TO_DEG))

    enRSpitch.delete(0, END)
    enRSpitch.insert(0, '%.3f' % (float(RShoulderPitchAngle) * almath.TO_DEG))
    enRSroll.delete(0, END)
    enRSroll.insert(0, '%.3f' % (float(RShoulderRollAngle) * almath.TO_DEG))
    enREroll.delete(0, END)
    enREroll.insert(0, '%.3f' % (float(RElbowRollAngle) * almath.TO_DEG))
    enREyaw.delete(0, END)
    enREyaw.insert(0, '%.3f' % (float(RElbowYawAngle) * almath.TO_DEG))
    enRWyaw.delete(0, END)
    enRWyaw.insert(0, '%.3f' % (float(RWristYawAngle) * almath.TO_DEG))

##_________________________________Speak and Move______________________________________##

## Movement Types
greetList = [waveLeft, waveRight]
agreeList = [nodYes]
disagreeList = [shakeNo]
questionList = [largeShrug]
makeAPointList = [handOutLeft, handOutRight, handsOnHips]


## gesture categories
question = ["?", "So is"]
makeAPoint = ["I think ", "I thought ", "I know ", "I get it ", "I will ", "Oh okay ", "Ohhh. ", "Oh ", "Maybe "]
agree = ["yes", "Yes ", "I agree ", "you're right ", " good ", " great "]
disagree = [" no ", "No ", "I disagree "]
greet = ["Hello", " hello", "Hey", " hey ", "Hi", " hi "]

def ProbabilisticMovement(line):
    threshold = 2

    ## probabilities
    # IMPORTANT: Write to a file or save to database & write/read in every time
    questionP1 = 0.25
    questionP2 = 0.495
    makeAPointP1 = 0.50
    makeAPointP2 = 0.75
    agreeP1 = 0.70
    agreeP2 = 0.90
    disagreeP1 = 0.70
    disagreeP2 = 0.90

    ## number of times this gesture TYPE has been used
    questionCount = 0
    makeAPointCount = 0
    agreeCount = 0
    disagreeCount = 0
    greetCount = 0


    if (questionCount >= threshold):
        questionP1 = 0.165
    #######################
    if (makeAPointCount >= threshold):
        makeAPointP1 = 0.33
    #######################
    if (agreeCount >= threshold):
        agreeP1 = 0.33
    #######################
    if (disagreeCount >= threshold):
        disagreeP1 = 0.33

    random_number = random.random()

    ## GREET ##
    if any(word in line for word in greet):
        ##  1/3 chance of 1st gesture
        ##  1/6 chance of 2nd gesture
        ##  1/2 chance of NO gesture
        tts.post.say(line)
        random_greet = choice(greetList)
        random_greet()
        greetCount = greetCount + 1
    ## AGREE ##
    elif any(word in line for word in agree):
        if (random_number <= agreeP1):
            tts.post.say(line)
            random_agree = choice(agreeList)
            random_agree()
            agreeCount = agreeCount + 1
        elif any(word in line for word in disagree):
            if (agreeP1 < random_number <= agreeP2):
                tts.post.say(line)
                random_disagree = choice(disagreeList)
                random_disagree()
                disagreeCount = disagreeCount + 1
        elif any(word in line for word in question):
            if (agreeP1 < random_number <= agreeP2):
                tts.post.say(line)
                random_question = choice(questionList)
                random_question()
                questionCount = questionCount + 1
        elif any(word in line for word in makeAPoint):
            if (agreeP1 < random_number <= agreeP2):
                tts.post.say(line)
                random_point = choice(makeAPointList)
                random_point()
                makeAPointCount = makeAPointCount + 1
        else:
            tts.post.say(line)
    ## DISAGREE ##
    elif any(word in line for word in disagree):
        if (random_number <= disagreeP1):
            tts.post.say(line)
            random_disagree = choice(disagreeList)
            random_disagree()
            disagreeCount = disagreeCount + 1
        elif any(word in line for word in question):
            if (disagreeP1 < random_number <= disagreeP2):
                tts.post.say(line)
                random_question = choice(questionList)
                random_question()
                questionCount = questionCount + 1
        elif any(word in line for word in makeAPoint):
            if (disagreeP1 < random_number <= disagreeP2):
                tts.post.say(line)
                random_point = choice(makeAPointList)
                random_point()
                makeAPointCount = makeAPointCount + 1
        else:
            tts.post.say(line)
    ## QUESTION ##
    elif any(word in line for word in question):
        if (random_number <= questionP1):
            tts.post.say(line)
            random_question = choice(questionList)
            random_question()
            questionCount = questionCount + 1
        elif any(word in line for word in makeAPoint):
            if (questionP1 < random_number <= questionP2):
                tts.post.say(line)
                random_point = choice(makeAPointList)
                random_point()
                makeAPointCount = makeAPointCount + 1
        else:
            tts.post.say(line)
    ## MAKE A POINT ##
    elif any(word in line for word in makeAPoint):
        if (random_number <= makeAPointP1):
            tts.post.say(line)
            random_point = choice(makeAPointList)
            random_point()
            makeAPointCount = makeAPointCount + 1
        else:
            tts.post.say(line)
    else:
        tts.say(line)

def nonProbabilisticMovememnt(line):
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
            greetFunction = random.choice(greetList)
            greetFunction()
        elif maxGesture == "agree":
            tts.post.say(line)
            agreeFunction = random.choice(agreeList)
            agreeFunction()
        elif maxGesture == "disagree":
            tts.post.say(line)
            disagreeFunction = random.choice(disagreeList)
            disagreeFunction()
        elif maxGesture == "makePoint":
            tts.post.say(line)
            makePointFunction = random.choice(makeAPointList)
            makePointFunction()
        elif maxGesture == "question":
            tts.post.say(line)
            questionFunction = random.choice(questionList)
            questionFunction()
        else:
            print "max gesture didn't match???"

        print maxGesture

    else:
        tts.say(line)


def saySmart(filename):

    with open(filename) as f:

        ## cuts the probability in half when
        ## a gesture group has been done more than twice
        ## (except for greetings)
        for line in f:
            ##ProbabilisticMovement(line)
            nonProbabilisticMovememnt(line)



def response(nicoresponsefile):
    with open(nicoresponsefile) as f:
        for line in f:
            bot_response = line
    return bot_response


##_________________________________MAIN______________________________________##
def main():
    nicoresponsefile = sys.argv[1]
    # bot_response = response(nicoresponsefile)
    saySmart(nicoresponsefile)


if __name__ == "__main__": main()
