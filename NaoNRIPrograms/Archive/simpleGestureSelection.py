from Tkinter import *
import sys
from naoqi import ALProxy
from naoqi import motion
import time
import almath
import random

import threading
from threading import Thread



root = Tk()
content = Frame(root)
frame = Frame(content, borderwidth=5, width=200, height=100)


def main(robotIP):
   PORT = 9559

   try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
   except Exception,e:
        print "Could not create proxy to ALMotion"
        print "Error was: ",e
        sys.exit(1)
        
   try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
   except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

   try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
   except Exception,e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ",e
        sys.exit(1)
    

##________________________________MENU FUNCTIONS_______________________________________##

       
   menubar = Menu(root)     
   def donothing(): 
      print "dummy button"

   def stand():
      postureProxy.goToPosture("Stand", 0.5)
   def standInit():
      postureProxy.goToPosture("StandInit", 0.5)
   def standZero():
      postureProxy.goToPosture("StandZero", 0.5)
   def sitRelax():
      postureProxy.goToPosture("SitRelax", 0.5)
   def sit():
      postureProxy.goToPosture("Sit", 0.5) 
   def crouch():
      postureProxy.goToPosture("Crouch", 0.5) 
   def lyingBelly():
      postureProxy.goToPosture("LyingBelly", 0.5)
   def lyingBack():
      postureProxy.goToPosture("LyingBack", 0.5)
     

##_________________________________STIFFNESS______________________________________##

   
   def stiffnessOff():
      pNames = "Body"
      pStiffnessLists = 0.0
      pTimeLists = 1.0
      motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
   stiffnessOff = Button(content, text ="OFF", command = stiffnessOff)

   
   def stiffnessOn():
      pNames = "Body"
      pStiffnessLists = 1.0
      pTimeLists = 1.0
      motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
   stiffnessOn = Button(content, text ="ON", command = stiffnessOn)

   
##_________________________________HEAD STUFF______________________________________##

   def moveHead():
       pitch = enHpitch.get()
       yaw = enHyaw.get()
       motionProxy.setStiffnesses("Head", 1.0)
       names  = ["HeadYaw", "HeadPitch"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)
       time.sleep(3.0)
       motionProxy.setStiffnesses("Head", 0.0)


   def moveHead2(pitch, yaw):
       motionProxy.setStiffnesses("Head", 1.0)
       names  = ["HeadYaw", "HeadPitch"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)
       time.sleep(3.0)
       motionProxy.setStiffnesses("Head", 0.0)


   # HEAD
   Hpitch = Label(content, text="Head pitch:")
   enHpitch = Entry(content)

   Hyaw = Label(content, text="Head yaw:")
   enHyaw = Entry(content)

   apply1 = Button(content, text="APPLY", width=10, command=moveHead)


##   # head diagram
##   def saveAsH():
##       menuPlace = 559
##       pitchSave = enHpitch.get()
##       yawSave = enHyaw.get()
##       name = ensaveAs1.get()
##
##       f = open("allTogetherNAO.py", "r")
##       contents = f.readlines()
##       f.close() 
##
##       contents.insert(menuPlace, "\n   headmenu.add_separator() \n   headmenu.add_command(label='" + name + "', command=lambda: moveHead2(" + pitchSave + ", " + yawSave + "))")
##   
##       f = open("allTogetherNAO.py", "w")
##       contents = "".join(contents)
##       f.write(contents)
##       f.close()
##
##
##      
##   # SAVE AS (HEAD)
##   saveAs1 = Label(content, text="Save as:")
##   ensaveAs1 = Entry(content)
##   bSave1 = Button(content, text="Save", width=10, command=saveAsH)



##_________________________________LEFT ARM STUFF______________________________________##

   def moveLeftArm():
       shoulderPitch = enLSpitch.get()
       shoulderRoll = enLSroll.get()
       elbowYaw = enLEyaw.get()
       elbowRoll = enLEroll.get()
       wristYaw = enLWyaw.get()
      
       motionProxy.setStiffnesses("LArm", 1.0)
       names  = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

      
   
   def moveLeftArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):

       motionProxy.setStiffnesses("LArm", 1.0)
       names  = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)


   # LEFT ARM
   LSpitch = Label(content, text="Left Shoulder pitch: ")
   enLSpitch = Entry(content)
   
   LSroll = Label(content, text="Left Shoulder roll: ")
   enLSroll = Entry(content)
   
   LEyaw = Label(content, text="Left Elbow yaw: ")
   enLEyaw = Entry(content)
  
   LEroll = Label(content, text="Left Elbow roll: ")
   enLEroll = Entry(content)
   
   LWyaw = Label(content, text="Left Wrist yaw: ")
   enLWyaw = Entry(content)


   apply2 = Button(content, text="APPLY", width=10, command=moveLeftArm)



##   def saveAsLA():
##       menuPlace = 584
##       shoulderPitchSave = enLSpitch.get()
##       shoulderRollSave = enLSroll.get()
##       elbowYawSave = enLEyaw.get()
##       elbowRollSave = enLEroll.get()
##       wristYawSave = enLWyaw.get()
##       name = ensaveAs2.get()
##
##       f = open("allTogetherNAO.py", "r")
##       contents = f.readlines()
##       f.close() 
##       contents.insert(menuPlace, "\n   leftarmmenu.add_separator() \n   leftarmmenu.add_command(label='" + name + "', command=lambda: moveLeftArm2(" + shoulderPitchSave + ", " + shoulderRollSave + ", " + elbowYawSave + ", "  + elbowRollSave + ", "  + wristYawSave + "))")
##       
##       f = open("allTogetherNAO.py", "w")
##       contents = "".join(contents)
##       f.write(contents)
##       f.close()
##
##
##       
##   # SAVE AS (RIGHT ARM)
##   saveAs2 = Label(content, text="Save as:")
##   ensaveAs2 = Entry(content)
##   bSave2 = Button(content, text="Save", width=10, command=saveAsLA)


##_________________________________RIGHT ARM STUFF______________________________________##


   def moveRightArm():
       shoulderPitch = enRSpitch.get()
       shoulderRoll = enRSroll.get()
       elbowYaw = enREyaw.get()
       elbowRoll = enREroll.get()
       wristYaw = enRWyaw.get()

       motionProxy.setStiffnesses("RArm", 1.0)
       names  = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

       #time.sleep(3.0)
       #motionProxy.setStiffnesses("LArm", 0.0)
       

   def moveRightArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):
       motionProxy.setStiffnesses("RArm", 1.0)
       names  = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

       #time.sleep(3.0)
       #motionProxy.setStiffnesses("LArm", 0.0)


   # RIGHT ARM

   RSpitch = Label(content, text="Right Shoulder pitch: ")
   enRSpitch = Entry(content)
  
   RSroll = Label(content, text="Right Shoulder roll: ")
   enRSroll = Entry(content)

   REyaw = Label(content, text="Right Elbow yaw: ")
   enREyaw = Entry(content)

   REroll = Label(content, text="Right Elbow roll: ")
   enREroll = Entry(content)

   RWyaw = Label(content, text="Right Wrist yaw: ")
   enRWyaw = Entry(content)

   apply3 = Button(content, text="APPLY", width=10, command=moveRightArm)




##   def saveAsRA():
##       menuPlace = 609
##       shoulderPitchSave = enRSpitch.get()
##       shoulderRollSave = enRSroll.get()
##       elbowYawSave = enREyaw.get()
##       elbowRollSave = enREroll.get()
##       wristYawSave = enRWyaw.get()
##       name = ensaveAs3.get()
##
##
##       f = open("allTogetherNAO.py", "r")
##       contents = f.readlines()
##       f.close() 
##
##       contents.insert(menuPlace, "\n   rightarmmenu.add_separator() \n   rightarmmenu.add_command(label='" + name + "', command=lambda: moveRightArm2(" + shoulderPitchSave
##                       + ", " + shoulderRollSave + ", " + elbowYawSave + ", "  + elbowRollSave + ", "  + wristYawSave + "))")
##
##       f = open("allTogetherNAO.py", "w")
##       contents = "".join(content)
##       f.write(content)
##       f.close()
##       
##
##   # SAVE AS (RIGHT ARM)
##   saveAs3 = Label(content, text="Save as:")
##   ensaveAs3 = Entry(content)
##   bSave3 = Button(content, text="Save", width=10, command=saveAsRA)

   
   
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
       names  = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                 "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD,
                  float(lshoulderPitch)*almath.TO_RAD, float(lshoulderRoll)*almath.TO_RAD, float(lelbowYaw)*almath.TO_RAD, float(lelbowRoll)*almath.TO_RAD, float(lwristYaw)*almath.TO_RAD,
                  float(rshoulderPitch)*almath.TO_RAD, float(rshoulderRoll)*almath.TO_RAD, float(relbowYaw)*almath.TO_RAD, float(relbowRoll)*almath.TO_RAD, float(rwristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)
        
   def moveBody2(yaw, pitch, lshoulderPitch, lshoulderRoll, lelbowYaw, lelbowRoll, lwristYaw,rshoulderPitch, rshoulderRoll, relbowYaw, relbowRoll, rwristYaw):
       motionProxy.setStiffnesses("Body", 1.0)
       names  = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                 "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD,
                  float(lshoulderPitch)*almath.TO_RAD, float(lshoulderRoll)*almath.TO_RAD, float(lelbowYaw)*almath.TO_RAD, float(lelbowRoll)*almath.TO_RAD, float(lwristYaw)*almath.TO_RAD,
                  float(rshoulderPitch)*almath.TO_RAD, float(rshoulderRoll)*almath.TO_RAD, float(relbowYaw)*almath.TO_RAD, float(relbowRoll)*almath.TO_RAD, float(rwristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

   applyAll = Button(content, text="APPLY ALL", width=10, command=moveBody)


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
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD, 15.5*almath.TO_RAD, 0.0*almath.TO_RAD],
                     [-11.5*almath.TO_RAD, 18.3*almath.TO_RAD, -30.5*almath.TO_RAD],
                     
                     [-41.9*almath.TO_RAD, -119.5*almath.TO_RAD, -89.8*almath.TO_RAD],
                     [29.9*almath.TO_RAD, 18.4*almath.TO_RAD, 61.4*almath.TO_RAD],
                     [-52.4*almath.TO_RAD, -19.4*almath.TO_RAD, -45.3*almath.TO_RAD],
                     [-88.5*almath.TO_RAD, -84.4*almath.TO_RAD, -2.0*almath.TO_RAD],
                     [-51.1*almath.TO_RAD, -44.5*almath.TO_RAD, 4.2*almath.TO_RAD],
                     [0],
                     
                     [-55.7*almath.TO_RAD, -110.1*almath.TO_RAD, -62.4*almath.TO_RAD],
                     [-35.2*almath.TO_RAD, -23.7*almath.TO_RAD, -61.8*almath.TO_RAD],
                     [33.8*almath.TO_RAD, 23.6*almath.TO_RAD, 59.6*almath.TO_RAD],
                     [88.5*almath.TO_RAD, 88.2*almath.TO_RAD, 2.4*almath.TO_RAD],
                     [61.7*almath.TO_RAD, 58.9*almath.TO_RAD, 18.6*almath.TO_RAD],
                     [0]]

      timeLists   = [[1.5, 3.5, 5.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("eawyn")
      time.sleep(1.0)
      crouch()

      
      
   def lookAtNailsLeft():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD, 15.7*almath.TO_RAD],
                     [0.0*almath.TO_RAD, -17.4*almath.TO_RAD],
                     
                     [81.0*almath.TO_RAD, -8.9*almath.TO_RAD],
                     [8.0*almath.TO_RAD, 2.9*almath.TO_RAD],
                     [-45.0*almath.TO_RAD, -60.2*almath.TO_RAD],
                     [-60.0*almath.TO_RAD, -88.7*almath.TO_RAD],
                     [8.7*almath.TO_RAD, -56.6*almath.TO_RAD, 84.6*almath.TO_RAD],
                     [0, 1],
                     
                     [81.0*almath.TO_RAD],
                     [-7.0*almath.TO_RAD],
                     [45.0*almath.TO_RAD],
                     [60.0*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]

      timeLists   = [[0.5, 2.0],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("hum")
      time.sleep(1.0)
      crouch()



   def lookAtNailsRight():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD, -5.7*almath.TO_RAD],
                     [0.0*almath.TO_RAD, 17.4*almath.TO_RAD],
                     
                     [79.0*almath.TO_RAD],
                     [10.0*almath.TO_RAD],
                     [-47.0*almath.TO_RAD],
                     [-60.0*almath.TO_RAD],
                     [8.0*almath.TO_RAD],
                     [0],
                     
                     [81.0*almath.TO_RAD, 48.9*almath.TO_RAD],
                     [-7.0*almath.TO_RAD, -2.9*almath.TO_RAD],
                     [45.0*almath.TO_RAD, 60.2*almath.TO_RAD],
                     [60.0*almath.TO_RAD, 88.7*almath.TO_RAD],
                     [1.0*almath.TO_RAD, 56.6*almath.TO_RAD, -104.6*almath.TO_RAD],
                     [0, 1]]

      timeLists   = [[0.5, 2.0],
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
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("hum")
      time.sleep(1.0)
      crouch()


   def handOutLeft():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [62.1*almath.TO_RAD],
                     [-1.2*almath.TO_RAD],
                     [-110.7*almath.TO_RAD],
                     [-49.2*almath.TO_RAD],
                     [-69.8*almath.TO_RAD],
                     [1],
                     
                     [80.7*almath.TO_RAD],
                     [0.2*almath.TO_RAD],
                     [54.8*almath.TO_RAD],
                     [49.6*almath.TO_RAD],
                     [4.3*almath.TO_RAD],
                     [0]]

      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("She ran three kilometers")
      time.sleep(1.0)
      crouch()

   def handOutRight():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [79.8*almath.TO_RAD],
                     [5.1*almath.TO_RAD],
                     [-52.5*almath.TO_RAD],
                     [-46.8*almath.TO_RAD],
                     [-26.6*almath.TO_RAD],
                     [0],
                     
                     [66.5*almath.TO_RAD],
                     [4.5*almath.TO_RAD],
                     [109.5*almath.TO_RAD],
                     [66.1*almath.TO_RAD],
                     [71.8*almath.TO_RAD],
                     [1]]

      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("So in 18 minutes she will be 6 kilometers away.")
      time.sleep(1.0)
      crouch()



   def largeShrug():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [65.0*almath.TO_RAD, 65.0*almath.TO_RAD],
                     [-4.0*almath.TO_RAD, -4.0*almath.TO_RAD],
                     [-119.8*almath.TO_RAD, -119.8*almath.TO_RAD],
                     [-79.8*almath.TO_RAD, -79.8*almath.TO_RAD],
                     [-49.6*almath.TO_RAD, -49.6*almath.TO_RAD],
                     [1],
                     
                     [65.0*almath.TO_RAD, 65.0*almath.TO_RAD],
                     [4.0*almath.TO_RAD, 4.0*almath.TO_RAD],
                     [119.8*almath.TO_RAD, 119.8*almath.TO_RAD],
                     [79.8*almath.TO_RAD, 79.8*almath.TO_RAD],
                     [49.6*almath.TO_RAD, 49.6*almath.TO_RAD],
                     [1]]

                      

      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I don't know how to solve it")
      time.sleep(1.0)
      crouch()


   def handsOnHips():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [75.0*almath.TO_RAD],
                     [27.0*almath.TO_RAD],
                     [-5.8*almath.TO_RAD],
                     [-86.8*almath.TO_RAD],
                     [0.6*almath.TO_RAD],
                     [0],
                     
                     [84.0*almath.TO_RAD],
                     [-29.9*almath.TO_RAD],
                     [18.5*almath.TO_RAD],
                     [79.2*almath.TO_RAD],
                     [1.8*almath.TO_RAD],
                     [0]]

                      

      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I think I know what to do!")
      time.sleep(1.0)
      crouch()


   def waveLeft():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [-2.3*almath.TO_RAD],
                     [18.4*almath.TO_RAD],
                     [-73.5*almath.TO_RAD, -112.5*almath.TO_RAD, -73.5*almath.TO_RAD, -112.5*almath.TO_RAD],
                     [-85.8*almath.TO_RAD],
                     [42.2*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.2*almath.TO_RAD],
                     [-10.8*almath.TO_RAD],
                     [0]]


      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Hello! Nice to meet you.")
      time.sleep(1.0)
      crouch()


   def waveRight():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [80.0*almath.TO_RAD],
                     [6.5*almath.TO_RAD],
                     [-46.8*almath.TO_RAD],
                     [-57.8*almath.TO_RAD],
                     [7.6*almath.TO_RAD],
                     [0],
                     
                     [2.3*almath.TO_RAD],
                     [-18.9*almath.TO_RAD],
                     [73.5*almath.TO_RAD, 112.5*almath.TO_RAD, 73.5*almath.TO_RAD, 112.5*almath.TO_RAD],
                     [86.2*almath.TO_RAD],
                     [-66.8*almath.TO_RAD],
                     [1]]


      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Hello! Nice to meet you.")
      time.sleep(1.0)
      crouch()


   def nodYes():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [11.3*almath.TO_RAD, -11.3*almath.TO_RAD, 11.3*almath.TO_RAD, -11.3*almath.TO_RAD, 0.0*almath.TO_RAD],

                     [80.9*almath.TO_RAD],
                     [8.3*almath.TO_RAD],
                     [-45.3*almath.TO_RAD],
                     [-60.4*almath.TO_RAD],
                     [8.7*almath.TO_RAD],
                     [0],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.1*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Yes, I agree")
      time.sleep(1.0)


   def shakeNo():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[18.3*almath.TO_RAD, -18.3*almath.TO_RAD, 18.3*almath.TO_RAD, -18.3*almath.TO_RAD, 0.0*almath.TO_RAD],
                    [0.0*almath.TO_RAD],

                    [80.9*almath.TO_RAD],
                    [8.3*almath.TO_RAD],
                    [-45.3*almath.TO_RAD],
                    [-60.4*almath.TO_RAD],
                    [8.7*almath.TO_RAD],
                    [0],
                     
                    [80.8*almath.TO_RAD],
                    [-8.4*almath.TO_RAD],
                    [45.1*almath.TO_RAD],
                    [60.1*almath.TO_RAD],
                    [-10.6*almath.TO_RAD],
                    [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5, 1.0, 1.5, 2.0, 2.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I don't think that's right")
      time.sleep(1.0)


   def lookLeft():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[14.3*almath.TO_RAD],
                     [22.9*almath.TO_RAD],

                     [39.9*almath.TO_RAD, 49.9*almath.TO_RAD],
                     [30.2*almath.TO_RAD, 40.9*almath.TO_RAD, 30.2*almath.TO_RAD],
                     [-60.5*almath.TO_RAD],
                     [-2.0*almath.TO_RAD],
                     [28.1*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.1*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Take a look at the screen here!")
      time.sleep(1.0)
      crouch()

   def lookRight():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[-14.3*almath.TO_RAD],
                     [22.9*almath.TO_RAD],

                     [80.8*almath.TO_RAD],
                     [8.4*almath.TO_RAD],
                     [-45.1*almath.TO_RAD],
                     [-60.1*almath.TO_RAD],
                     [8.6*almath.TO_RAD],
                     [0],
                     
                     [39.9*almath.TO_RAD, 49.9*almath.TO_RAD],
                     [-30.2*almath.TO_RAD, -40.9*almath.TO_RAD, -30.9*almath.TO_RAD],
                     [60.5*almath.TO_RAD],
                     [2.0*almath.TO_RAD],
                     [-28.1*almath.TO_RAD],
                     [1]]

      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Take a look at the screen here!")
      time.sleep(1.0)
      crouch()


   def facepalmLeft():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [20.0*almath.TO_RAD],

                     [8.5*almath.TO_RAD, 28.3*almath.TO_RAD],
                     [-18.2*almath.TO_RAD, -9.1*almath.TO_RAD],
                     [-59.3*almath.TO_RAD, -101.0*almath.TO_RAD],
                     [-88.5*almath.TO_RAD, -85.7*almath.TO_RAD],
                     [-63.4*almath.TO_RAD, -61.2*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-3.3*almath.TO_RAD],
                     [50.9*almath.TO_RAD],
                     [55.1*almath.TO_RAD],
                     [-5.0*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I can't believe I didn't see that before!")
      time.sleep(1.0)
      crouch()


   def facepalmRight():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [20.0*almath.TO_RAD],

                     [79.9*almath.TO_RAD],
                     [9.3*almath.TO_RAD],
                     [-46.3*almath.TO_RAD],
                     [-58.8*almath.TO_RAD],
                     [7.7*almath.TO_RAD],
                     [0],
                     
                     [1.5*almath.TO_RAD, 28.3*almath.TO_RAD],
                     [12.2*almath.TO_RAD, 9.1*almath.TO_RAD],
                     [55.3*almath.TO_RAD, 101.0*almath.TO_RAD],
                     [88.5*almath.TO_RAD, 85.7*almath.TO_RAD],
                     [68.4*almath.TO_RAD, 61.2*almath.TO_RAD],
                     [1]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I can't believe I didn't see that before!")
      time.sleep(1.0)
      crouch()


   def cantHearLeft():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[-30.3*almath.TO_RAD],
                     [5.7*almath.TO_RAD],

                     [38.8*almath.TO_RAD],
                     [12.0*almath.TO_RAD],
                     [-86.5*almath.TO_RAD],
                     [-87.7*almath.TO_RAD],
                     [8.6*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.1*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I didn't hear you, can you repeat that?")
      time.sleep(1.0)
      crouch()



   def cantHearRight():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[30.3*almath.TO_RAD],
                     [5.7*almath.TO_RAD],

                     [79.9*almath.TO_RAD],
                     [9.3*almath.TO_RAD],
                     [-46.3*almath.TO_RAD],
                     [-58.8*almath.TO_RAD],
                     [7.7*almath.TO_RAD],
                     [0],
                     
                     [35.2*almath.TO_RAD],
                     [-9.0*almath.TO_RAD],
                     [65.8*almath.TO_RAD],
                     [87.1*almath.TO_RAD],
                     [11.4*almath.TO_RAD],
                     [1]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I didn't hear you, can you repeat that?")
      time.sleep(1.0)
      crouch()


   def handOnChestLeft():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],

                     [44.9*almath.TO_RAD],
                     [-11.5*almath.TO_RAD],
                     [-30.2*almath.TO_RAD],
                     [-86.5*almath.TO_RAD],
                     [-36.6*almath.TO_RAD],
                     [1],
                     
                     [79.8*almath.TO_RAD],
                     [-10.4*almath.TO_RAD],
                     [46.1*almath.TO_RAD],
                     [58.1*almath.TO_RAD],
                     [-7.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I think I know the answer!")
      time.sleep(1.0)
      crouch()

   def handOnChestRight():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],

                     [76.9*almath.TO_RAD],
                     [0.3*almath.TO_RAD],
                     [-44.3*almath.TO_RAD],
                     [-46.1*almath.TO_RAD],
                     [-12.9*almath.TO_RAD],
                     [0],
                     
                     [43.9*almath.TO_RAD],
                     [9.7*almath.TO_RAD],
                     [22.7*almath.TO_RAD],
                     [88.5*almath.TO_RAD],
                     [51.8*almath.TO_RAD],
                     [1]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I think I know the answer!")
      time.sleep(1.0)
      crouch()


   def handsOut():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],

                     [12.4*almath.TO_RAD],
                     [19.1*almath.TO_RAD],
                     [-119.5*almath.TO_RAD],
                     [-82.5*almath.TO_RAD],
                     [39.9*almath.TO_RAD],
                     [1],
                     
                     [9.5*almath.TO_RAD],
                     [-19.8*almath.TO_RAD],
                     [119.1*almath.TO_RAD],
                     [87.0*almath.TO_RAD],
                     [-49.5*almath.TO_RAD],
                     [1]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I think I know the answer!")
      time.sleep(1.0)
      crouch()



   def cheering():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],

                     [56.2*almath.TO_RAD],
                     [-9.9*almath.TO_RAD, -18.0*almath.TO_RAD],
                     [-60.9*almath.TO_RAD, -65.9*almath.TO_RAD],
                     [-88.5*almath.TO_RAD],
                     [5.7*almath.TO_RAD],
                     [0, 1],
                     
                     [60.7*almath.TO_RAD],
                     [18.0*almath.TO_RAD, 11.9*almath.TO_RAD],
                     [66.7*almath.TO_RAD, 62.7*almath.TO_RAD],
                     [88.5*almath.TO_RAD],
                     [-21.8*almath.TO_RAD],
                     [0, 1]]

      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("We did it!")
      time.sleep(1.0)
      crouch()


   def handsOnHead():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[10.3*almath.TO_RAD, -10.3*almath.TO_RAD, 10.3*almath.TO_RAD, -10.3*almath.TO_RAD, 0.0*almath.TO_RAD],
                     [20.0*almath.TO_RAD],

                     [-9.7*almath.TO_RAD],
                     [-4.1*almath.TO_RAD],
                     [-69.2*almath.TO_RAD],
                     [-87.8*almath.TO_RAD],
                     [-61.9*almath.TO_RAD],
                     [0],
                     
                     [-15.2*almath.TO_RAD],
                     [-1.1*almath.TO_RAD],
                     [62.3*almath.TO_RAD],
                     [87.8*almath.TO_RAD],
                     [68.3*almath.TO_RAD],
                     [0]]

      timeLists   = [[0.5, 1.0, 1.5, 2.0, 2.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("This is really confusing!")
      time.sleep(1.0)
      crouch()




##_________________________________CARTOON GESTURES______________________________________##
##_______________________________________________________________________________________##
##_______________________________________________________________________________________##

      
   def lookAtNailsLeft2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD, 15.7*almath.TO_RAD],
                     [0.0*almath.TO_RAD, -13.4*almath.TO_RAD],
                     
                     [81.0*almath.TO_RAD, -8.9*almath.TO_RAD, -3.2*almath.TO_RAD],
                     [8.0*almath.TO_RAD, 2.9*almath.TO_RAD, 22.7*almath.TO_RAD],
                     [-45.0*almath.TO_RAD, -60.2*almath.TO_RAD, -69.5*almath.TO_RAD],
                     [-60.0*almath.TO_RAD, -88.7*almath.TO_RAD, -40.5*almath.TO_RAD],
                     [8.7*almath.TO_RAD, -56.6*almath.TO_RAD, 104.6*almath.TO_RAD],
                     [0, 1],
                     
                     [81.0*almath.TO_RAD],
                     [-7.0*almath.TO_RAD],
                     [45.0*almath.TO_RAD],
                     [60.0*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]

      timeLists   = [[0.5, 2.0],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("hum")
      time.sleep(1.0)
      crouch()


   def lookAtNailsRight2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD, -5.7*almath.TO_RAD],
                     [0.0*almath.TO_RAD, 17.4*almath.TO_RAD],
                     
                     [79.0*almath.TO_RAD],
                     [10.0*almath.TO_RAD],
                     [-47.0*almath.TO_RAD],
                     [-60.0*almath.TO_RAD],
                     [8.0*almath.TO_RAD],
                     [0],
                     
                     [81.0*almath.TO_RAD, 48.9*almath.TO_RAD],
                     [-7.0*almath.TO_RAD, -2.9*almath.TO_RAD],
                     [45.0*almath.TO_RAD, 60.2*almath.TO_RAD],
                     [60.0*almath.TO_RAD, 88.7*almath.TO_RAD],
                     [1.0*almath.TO_RAD, 56.6*almath.TO_RAD, -104.6*almath.TO_RAD],
                     [0, 1]]

      timeLists   = [[0.5, 2.0],
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
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("hum")
      time.sleep(1.0)
      crouch()


   def handOutLeft2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [48.5*almath.TO_RAD, 62.1*almath.TO_RAD],
                     [8.3*almath.TO_RAD, -1.2*almath.TO_RAD],
                     [-119.5*almath.TO_RAD, -110.7*almath.TO_RAD],
                     [-76.6*almath.TO_RAD, -69.2*almath.TO_RAD],
                     [-68.4*almath.TO_RAD, -69.8*almath.TO_RAD],
                     [0, 1],
                     
                     [80.7*almath.TO_RAD],
                     [0.2*almath.TO_RAD],
                     [54.8*almath.TO_RAD],
                     [49.6*almath.TO_RAD],
                     [4.3*almath.TO_RAD],
                     [0]]

      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("She ran three kilometers")
      time.sleep(1.0)
      crouch()

   def handOutRight2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [80.0*almath.TO_RAD],
                     [6.5*almath.TO_RAD],
                     [-46.8*almath.TO_RAD],
                     [-57.8*almath.TO_RAD],
                     [7.6*almath.TO_RAD],
                     [0],
                     
                     [32.5*almath.TO_RAD, 62.1*almath.TO_RAD],
                     [-8.3*almath.TO_RAD, 1.2*almath.TO_RAD],
                     [95.5*almath.TO_RAD, 110.7*almath.TO_RAD],
                     [76.6*almath.TO_RAD, 69.2*almath.TO_RAD],
                     [79.4*almath.TO_RAD, 69.8*almath.TO_RAD],
                     [0, 1]]

      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("So in 18 minutes she will be 6 kilometers away.")
      time.sleep(1.0)
      crouch()



   def largeShrug2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [39.0*almath.TO_RAD, 39.0*almath.TO_RAD],
                     [9.0*almath.TO_RAD, 9.0*almath.TO_RAD],
                     [-119.8*almath.TO_RAD, -119.8*almath.TO_RAD],
                     [-84.8*almath.TO_RAD, -84.8*almath.TO_RAD],
                     [-55.6*almath.TO_RAD, -55.6*almath.TO_RAD],
                     [1],
                     
                     [36.0*almath.TO_RAD, 36.0*almath.TO_RAD],
                     [-16.9*almath.TO_RAD, -16.9*almath.TO_RAD],
                     [119.5*almath.TO_RAD, 119.5*almath.TO_RAD],
                     [86.2*almath.TO_RAD, 86.2*almath.TO_RAD],
                     [55.8*almath.TO_RAD, 55.8*almath.TO_RAD],
                     [1]]

                      

      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I don't know how to solve it")
      time.sleep(1.0)
      crouch()


   def handsOnHips2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [71.4*almath.TO_RAD, 75.0*almath.TO_RAD],
                     [67.8*almath.TO_RAD, 27.0*almath.TO_RAD],
                     [-21.6*almath.TO_RAD, -5.8*almath.TO_RAD],
                     [-88.5*almath.TO_RAD, -86.8*almath.TO_RAD],
                     [1.2*almath.TO_RAD, 0.6*almath.TO_RAD],
                     [0],
                     
                     [71.6*almath.TO_RAD, 84.0*almath.TO_RAD],
                     [-67.6*almath.TO_RAD, -29.9*almath.TO_RAD],
                     [21.6*almath.TO_RAD, 18.5*almath.TO_RAD],
                     [88.6*almath.TO_RAD, 79.2*almath.TO_RAD],
                     [6.6*almath.TO_RAD, 1.8*almath.TO_RAD],
                     [0]]

                      

      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I think I know what to do!")
      time.sleep(1.0)
      crouch()


   def waveLeft2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [-2.3*almath.TO_RAD],
                     [18.4*almath.TO_RAD],
                     [-53.5*almath.TO_RAD, -122.5*almath.TO_RAD, -53.5*almath.TO_RAD, -122.5*almath.TO_RAD],
                     [-85.8*almath.TO_RAD],
                     [42.2*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.2*almath.TO_RAD],
                     [-10.8*almath.TO_RAD],
                     [0]]


      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Hello! Nice to meet you.")
      time.sleep(1.0)
      crouch()


   def waveRight2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [80.0*almath.TO_RAD],
                     [6.5*almath.TO_RAD],
                     [-46.8*almath.TO_RAD],
                     [-57.8*almath.TO_RAD],
                     [7.6*almath.TO_RAD],
                     [0],
                     
                     [2.3*almath.TO_RAD],
                     [-18.9*almath.TO_RAD],
                     [73.5*almath.TO_RAD, 112.5*almath.TO_RAD, 73.5*almath.TO_RAD, 112.5*almath.TO_RAD],
                     [86.2*almath.TO_RAD],
                     [-66.8*almath.TO_RAD],
                     [1]]


      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Hello! Nice to meet you.")
      time.sleep(1.0)
      crouch()


   def nodYes2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [20.3*almath.TO_RAD, -20.3*almath.TO_RAD, 20.3*almath.TO_RAD, -20.3*almath.TO_RAD, 0.0*almath.TO_RAD],

                     [80.9*almath.TO_RAD],
                     [8.3*almath.TO_RAD],
                     [-45.3*almath.TO_RAD],
                     [-60.4*almath.TO_RAD],
                     [8.7*almath.TO_RAD],
                     [0],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.1*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Yes, I agree")
      time.sleep(1.0)


   def shakeNo2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[28.3*almath.TO_RAD, -28.3*almath.TO_RAD, 28.3*almath.TO_RAD, -25.3*almath.TO_RAD, 0.0*almath.TO_RAD],
                    [0.0*almath.TO_RAD],

                    [80.9*almath.TO_RAD],
                    [8.3*almath.TO_RAD],
                    [-45.3*almath.TO_RAD],
                    [-60.4*almath.TO_RAD],
                    [8.7*almath.TO_RAD],
                    [0],
                     
                    [80.8*almath.TO_RAD],
                    [-8.4*almath.TO_RAD],
                    [45.1*almath.TO_RAD],
                    [60.1*almath.TO_RAD],
                    [-10.6*almath.TO_RAD],
                    [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5, 1.0, 1.5, 2.0, 2.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I don't think that's right")
      time.sleep(1.0)


   def lookLeft2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[14.3*almath.TO_RAD],
                     [22.9*almath.TO_RAD],

                     [39.9*almath.TO_RAD, 59.9*almath.TO_RAD],
                     [30.2*almath.TO_RAD, 50.9*almath.TO_RAD, 30.2*almath.TO_RAD],
                     [-60.5*almath.TO_RAD],
                     [-2.0*almath.TO_RAD],
                     [28.1*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.1*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("Take a look at the screen here!")
      time.sleep(1.0)
      crouch()

   def lookRight2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[-14.3*almath.TO_RAD],
                     [22.9*almath.TO_RAD],

                     [80.8*almath.TO_RAD],
                     [8.4*almath.TO_RAD],
                     [-45.1*almath.TO_RAD],
                     [-60.1*almath.TO_RAD],
                     [8.6*almath.TO_RAD],
                     [0],
                     
                     [39.9*almath.TO_RAD, 59.9*almath.TO_RAD],
                     [-30.2*almath.TO_RAD, -50.9*almath.TO_RAD, -30.9*almath.TO_RAD],
                     [60.5*almath.TO_RAD],
                     [2.0*almath.TO_RAD],
                     [-28.1*almath.TO_RAD],
                     [1]]

      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      tts.say("Take a look at the screen here!")
      time.sleep(1.0)
      crouch()


   def facepalmLeft2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [20.0*almath.TO_RAD],

                     [8.5*almath.TO_RAD, 28.3*almath.TO_RAD],
                     [-18.2*almath.TO_RAD, -9.1*almath.TO_RAD],
                     [-59.3*almath.TO_RAD, -101.0*almath.TO_RAD],
                     [-88.5*almath.TO_RAD, -85.7*almath.TO_RAD],
                     [-63.4*almath.TO_RAD, -61.2*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-3.3*almath.TO_RAD],
                     [50.9*almath.TO_RAD],
                     [55.1*almath.TO_RAD],
                     [-5.0*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I can't believe I didn't see that before!")
      time.sleep(1.0)
      crouch()


   def facepalmRight2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [20.0*almath.TO_RAD],

                     [79.9*almath.TO_RAD],
                     [9.3*almath.TO_RAD],
                     [-46.3*almath.TO_RAD],
                     [-58.8*almath.TO_RAD],
                     [7.7*almath.TO_RAD],
                     [0],
                     
                     [1.5*almath.TO_RAD, 28.3*almath.TO_RAD],
                     [12.2*almath.TO_RAD, 9.1*almath.TO_RAD],
                     [55.3*almath.TO_RAD, 101.0*almath.TO_RAD],
                     [88.5*almath.TO_RAD, 85.7*almath.TO_RAD],
                     [68.4*almath.TO_RAD, 61.2*almath.TO_RAD],
                     [1]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I can't believe I didn't see that before!")
      time.sleep(1.0)
      crouch()


   def cantHearLeft2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[-63.3*almath.TO_RAD],
                     [5.7*almath.TO_RAD],

                     [19.8*almath.TO_RAD],
                     [-2.2*almath.TO_RAD],
                     [-67.6*almath.TO_RAD],
                     [-88.5*almath.TO_RAD],
                     [13.8*almath.TO_RAD],
                     [1],
                     
                     [80.8*almath.TO_RAD],
                     [-8.4*almath.TO_RAD],
                     [45.1*almath.TO_RAD],
                     [60.1*almath.TO_RAD],
                     [-10.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I didn't hear you, can you repeat that?")
      time.sleep(1.0)
      crouch()



   def cantHearRight2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[63.3*almath.TO_RAD],
                     [-5.7*almath.TO_RAD],

                     [79.9*almath.TO_RAD],
                     [9.3*almath.TO_RAD],
                     [-46.3*almath.TO_RAD],
                     [-58.8*almath.TO_RAD],
                     [7.7*almath.TO_RAD],
                     [0],
                     
                     [9.7*almath.TO_RAD],
                     [-6.3*almath.TO_RAD],
                     [64.6*almath.TO_RAD],
                     [87.5*almath.TO_RAD],
                     [-13.8*almath.TO_RAD],
                     [1]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I didn't hear you, can you repeat that?")
      time.sleep(1.0)
      crouch()


   def handOnChestLeft2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],

                     [44.9*almath.TO_RAD],
                     [-11.5*almath.TO_RAD],
                     [-30.2*almath.TO_RAD],
                     [-86.5*almath.TO_RAD],
                     [-36.6*almath.TO_RAD],
                     [1],
                     
                     [79.8*almath.TO_RAD],
                     [-10.4*almath.TO_RAD],
                     [46.1*almath.TO_RAD],
                     [58.1*almath.TO_RAD],
                     [-7.6*almath.TO_RAD],
                     [0]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I think I know the answer!")
      time.sleep(1.0)
      crouch()

   def handOnChestRight2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],

                     [76.9*almath.TO_RAD],
                     [0.3*almath.TO_RAD],
                     [-44.3*almath.TO_RAD],
                     [-46.1*almath.TO_RAD],
                     [-12.9*almath.TO_RAD],
                     [0],
                     
                     [43.9*almath.TO_RAD],
                     [9.7*almath.TO_RAD],
                     [22.7*almath.TO_RAD],
                     [88.5*almath.TO_RAD],
                     [51.8*almath.TO_RAD],
                     [1]]


      #*almath.TO_RAD
      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("I think I know the answer!")
      time.sleep(1.0)
      crouch()


   def cheering2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [-11.5*almath.TO_RAD],

                     [-40.5*almath.TO_RAD, -62.3*almath.TO_RAD, -40.5*almath.TO_RAD, -62.3*almath.TO_RAD],
                     [47.9*almath.TO_RAD, 14.7*almath.TO_RAD, 47.9*almath.TO_RAD, 14.7*almath.TO_RAD],
                     [-54.4*almath.TO_RAD, -60.4*almath.TO_RAD, -54.4*almath.TO_RAD, -60.4*almath.TO_RAD],
                     [-83.7*almath.TO_RAD, -54.9*almath.TO_RAD, -83.7*almath.TO_RAD, -54.9*almath.TO_RAD],
                     [-37.7*almath.TO_RAD, -37.1*almath.TO_RAD, -37.7*almath.TO_RAD, -37.1*almath.TO_RAD],
                     [0],
                     
                     [-22.0*almath.TO_RAD, -62.3*almath.TO_RAD, -22.0*almath.TO_RAD, -62.3*almath.TO_RAD],
                     [-48.5*almath.TO_RAD, -14.7*almath.TO_RAD, -48.5*almath.TO_RAD, -14.7*almath.TO_RAD],
                     [64.5*almath.TO_RAD, 60.4*almath.TO_RAD, 64.5*almath.TO_RAD, 60.4*almath.TO_RAD],
                     [88.7*almath.TO_RAD, 54.9*almath.TO_RAD, 88.7*almath.TO_RAD, 54.9*almath.TO_RAD],
                     [37.9*almath.TO_RAD, 37.1*almath.TO_RAD, 37.9*almath.TO_RAD, 37.1*almath.TO_RAD],
                     [0]]

      timeLists   = [[0.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("We did it!")
      time.sleep(1.0)
      crouch()


   def handsOnHead2():
      names = ["HeadYaw", "HeadPitch",
               "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","LWristYaw", "LHand",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
      angleLists  = [[15.3*almath.TO_RAD, -15.3*almath.TO_RAD, 15.3*almath.TO_RAD, -15.3*almath.TO_RAD, 0.0*almath.TO_RAD],
                     [20.0*almath.TO_RAD],

                     [-9.7*almath.TO_RAD],
                     [19.5*almath.TO_RAD, -4.1*almath.TO_RAD],
                     [-81.1*almath.TO_RAD, -69.2*almath.TO_RAD],
                     [-67.8*almath.TO_RAD, -87.8*almath.TO_RAD],
                     [-76.1*almath.TO_RAD, -61.9*almath.TO_RAD],
                     [0],
                     
                     [-15.2*almath.TO_RAD],
                     [-19.5*almath.TO_RAD, -1.1*almath.TO_RAD],
                     [81.1*almath.TO_RAD, 62.3*almath.TO_RAD],
                     [67.8*almath.TO_RAD, 87.8*almath.TO_RAD],
                     [76.1*almath.TO_RAD, 68.3*almath.TO_RAD],
                     [0]]

      timeLists   = [[0.5, 1.0, 1.5, 2.0, 2.5],
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
      
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      ## tts.say("This is really confusing!")
      crouch()



   def saySmart():
      ## start in crouch
      crouch()

      ## gesture categories
      question = ["?", "I don't know", "why", "what"]
      makeAPoint = ["I think", "I know", "I get it", "I will"]
      agree = ["yes", "Yes", "I agree", "you're right", "good", "great"]
      disagree = ["no", "No", "I disagree"]
      greet = ["Hello", "hello", "Hey", "hey", "Hi", "hi"]

      questionCount = 0
      makeAPointCount = 0
      agreeCount = 0
      disagreeCount = 0
      greetCount = 0

      threshold = 4
      highP = 0.50
      lowP = 0.80

      
      with open("NAOdialogEx2.txt") as f:
          for line in f:
            if (questionCount < threshold):
               questionP = highP
            else:
               questionP = lowP
            #######################
            if (makeAPointCount < threshold):
               makeAPointP = highP
            else:
               makeAPointP = lowP
            #######################
            if (agreeCount < threshold):
               agreeP = highP
            else:
               agreeP = lowP
            #######################
            if (disagreeCount < threshold):
               disagreeP = highP
            else:
               disagreeP = lowP
            #######################
            if (greetCount < threshold):
               greetP = highP
            else:
               greetP = lowP

            
            random_number = random.random()
               
            if any(word in line for word in question) and (random_number >= questionP):
               tts.post.say(line)
               largeShrug()
               questionCount = questionCount+1
               ## print ("question count: " + str(questionCount))
               ## print ("shrug probability: " + str(questionP))
            elif any(word in line for word in agree) and (random_number >= agreeP):
               tts.post.say(line)
               nodYes()
               agreeCount = agreeCount+1
               ## print ("agreeCount: " + str(agreeCount))
            elif any(word in line for word in disagree) and (random_number >= disagreeP):
               tts.post.say(line)
               shakeNo()
               disagreeCount = disagreeCount+1
               ## print ("disagreeCount: " + str(disagreeCount))
            elif any(word in line for word in greet) and (random_number >= greetP):
               tts.post.say(line)
               waveLeft()
               greetCount = greetCount+1
               ## print ("greetCount: " + str(greetCount))
            elif any(word in line for word in makeAPoint) and (random_number >= makeAPointP):
               tts.post.say(line)
               if (int(random_number * 100) % 2 == 0):
                  handOutLeft()
               else:
                  handOutRight()
               makeAPointCount = makeAPointCount+1
               ## print ("makeAPointCount: " + str(makeAPointCount))
            else:
               tts.say(line)



   sayLabel = Label(content, text="Say this:")
   enSay = Entry(content)
   bSay = Button(content, text="GO", width=10, command=saySmart)


   

      
##_________________________________GET ANGLES______________________________________##
   
   # Example that finds the difference between the command and sensed angles.
   def getAngles():
      HeadYaw           = "HeadYaw"
      HeadPitch         = "HeadPitch"
      LShoulderPitch    = "LShoulderPitch"
      LShoulderRoll     = "LShoulderRoll"
      LElbowRoll        = "LElbowRoll"
      LElbowYaw         = "LElbowYaw"
      LWristYaw         = "LWristYaw"
      RShoulderPitch    = "RShoulderPitch"
      RShoulderRoll     = "RShoulderRoll"
      RElbowRoll        = "RElbowRoll"
      RElbowYaw         = "RElbowYaw"
      RWristYaw         = "RWristYaw"

      useSensors  = True
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
      enHyaw.insert(0, '%.3f'%(float(HeadYawAngle)*almath.TO_DEG))
      enHpitch.delete(0, END)
      enHpitch.insert(0, '%.3f'%(float(HeadPitchAngle)*almath.TO_DEG))

      enLSpitch.delete(0, END)
      enLSpitch.insert(0, '%.3f'%(float(LShoulderPitchAngle)*almath.TO_DEG))
      enLSroll.delete(0, END)
      enLSroll.insert(0, '%.3f'%(float(LShoulderRollAngle)*almath.TO_DEG))
      enLEroll.delete(0, END)
      enLEroll.insert(0, '%.3f'%(float(LElbowRollAngle)*almath.TO_DEG))
      enLEyaw.delete(0, END)
      enLEyaw.insert(0, '%.3f'%(float(LElbowYawAngle)*almath.TO_DEG))
      enLWyaw.delete(0, END)
      enLWyaw.insert(0, '%.3f'%(float(LWristYawAngle)*almath.TO_DEG))

      enRSpitch.delete(0, END)
      enRSpitch.insert(0, '%.3f'%(float(RShoulderPitchAngle)*almath.TO_DEG))
      enRSroll.delete(0, END)
      enRSroll.insert(0, '%.3f'%(float(RShoulderRollAngle)*almath.TO_DEG))
      enREroll.delete(0, END)
      enREroll.insert(0, '%.3f'%(float(RElbowRollAngle)*almath.TO_DEG))
      enREyaw.delete(0, END)
      enREyaw.insert(0, '%.3f'%(float(RElbowYawAngle)*almath.TO_DEG))
      enRWyaw.delete(0, END)
      enRWyaw.insert(0, '%.3f'%(float(RWristYawAngle)*almath.TO_DEG))
      

   getAngles = Button(content, text="Get Curent", width=10, command=getAngles)





##_________________________________GRID STUFF______________________________________##
   
   content.grid(column=0, row=0)
   #frame.grid(column=0, row=0, columnspan=3, rowspan=1)
   
   stiffnessOff.grid(column=5, row=0)
   stiffnessOn.grid(column=6, row=0)


   Hyaw.grid(column=2, row=1, padx=10)
   enHyaw.grid(column=2, row=2, padx=10)
   Hpitch.grid(column=2, row=3, padx=10)
   enHpitch.grid(column=2, row=4, padx=10)
   apply1.grid(column=2, row=5, padx=10)
##   saveAs1.grid(column=2, row=16, padx=10)
##   ensaveAs1.grid(column=2, row=17, padx=10)
##   bSave1.grid(column=2, row=18, padx=10)


   LSpitch.grid(column=3, row=1, padx=15)
   enLSpitch.grid(column=3, row=2, padx=15)
   LSroll.grid(column=3, row=3, padx=15)
   enLSroll.grid(column=3, row=4, padx=15)
   LEyaw.grid(column=3, row=5, padx=15)
   enLEyaw.grid(column=3, row=6, padx=15)
   LEroll.grid(column=3, row=7, padx=15)
   enLEroll.grid(column=3, row=8, padx=15)
   LWyaw.grid(column=3, row=9, padx=15)
   enLWyaw.grid(column=3, row=10, padx=15)
   apply2.grid(column=3, row=13, padx=15)
##   saveAs2.grid(column=3, row=16, padx=15)
##   ensaveAs2.grid(column=3, row=17, padx=15)
##   bSave2.grid(column=3, row=18, padx=15)
   
   getAngles.grid(column=5, row=14, padx=15)


   RSpitch.grid(column=4, row=1, padx=15)
   enRSpitch.grid(column=4, row=2, padx=15)
   RSroll.grid(column=4, row=3, padx=15)
   enRSroll.grid(column=4, row=4, padx=15)
   REyaw.grid(column=4, row=5, padx=15)
   enREyaw.grid(column=4, row=6, padx=15)
   REroll.grid(column=4, row=7, padx=15)
   enREroll.grid(column=4, row=8, padx=15)
   RWyaw.grid(column=4, row=9, padx=15)
   enRWyaw.grid(column=4, row=10, padx=15)
   apply3.grid(column=4, row=13, padx=15)
##   saveAs3.grid(column=4, row=16, padx=15)
##   ensaveAs3.grid(column=4, row=17, padx=15)
##   bSave3.grid(column=4, row=18, padx=15)


##   saveAs4.grid(column=5, row=14, padx=10)
##   ensaveAs4.grid(column=5, row=15, padx=10)
##   bSave4.grid(column=5, row=16, padx=10)
   applyAll.grid(column=5, row=15, padx=15)

   sayLabel.grid(column=1, row=20)
   enSay.grid(column=1, row=21)
   bSay.grid(column=1, row=22)

##__________________________________MENUS_____________________________________##

   
   menubar = Menu(root)

   # POSTURE MENU
   posturemenu = Menu(menubar, tearoff=0)
   posturemenu.add_command(label="Stand", command=stand)
   posturemenu.add_separator()
   posturemenu.add_command(label="StandInit", command=standInit)
   posturemenu.add_separator()
   posturemenu.add_command(label="StandZero", command=standZero)
   posturemenu.add_separator()
   posturemenu.add_command(label="SitRelax", command=sitRelax)
   posturemenu.add_separator()
   posturemenu.add_command(label="Sit", command=sit)
   posturemenu.add_separator()
   posturemenu.add_command(label="Crouch", command=crouch)
   posturemenu.add_separator()
   posturemenu.add_command(label="LyingBelly", command=lyingBelly)
   posturemenu.add_separator()
   posturemenu.add_command(label="LyingBack", command=lyingBack)

   menubar.add_cascade(label="Posture", menu=posturemenu)


  

   realmenu = Menu(menubar, tearoff=0)

   realmenu.add_command(label="Hands on Hips", command=handsOnHips)
   realmenu.add_separator()
   realmenu.add_command(label="Shrug", command=largeShrug)
   realmenu.add_separator()
   realmenu.add_command(label="Cheer", command=cheering)
   realmenu.add_separator()
   realmenu.add_command(label="Hands on Head", command=handsOnHead)
   realmenu.add_separator()
   realmenu.add_command(label="Hands Out", command=handsOut)
   realmenu.add_separator()
   realmenu.add_command(label="Stretch", command=yawnAndStretch)
   realmenu.add_separator()
   realmenu.add_command(label="Look (L)", command=lookLeft)
   realmenu.add_command(label="Look (R)", command=lookRight)
   realmenu.add_separator()
   realmenu.add_command(label="Can't Hear (L)", command=cantHearLeft)
   realmenu.add_command(label="Can't Hear (R)", command=cantHearRight)
   realmenu.add_separator()
   realmenu.add_command(label="Nod (Yes)", command=nodYes)
   realmenu.add_command(label="Shake (No)", command=shakeNo)
   realmenu.add_separator()
   realmenu.add_command(label="Hand out (L)", command=handOutLeft)
   realmenu.add_command(label="Hand out (R)", command=handOutRight)
   realmenu.add_separator()
   realmenu.add_command(label="Look at nails (L)", command=lookAtNailsLeft)
   realmenu.add_command(label="Look at nails (R)", command=lookAtNailsRight)
   realmenu.add_separator()
   realmenu.add_command(label="Wave (L)", command=waveLeft)
   realmenu.add_command(label="Wave (R)", command=waveRight)
   realmenu.add_separator()
   realmenu.add_command(label="Hand on chest (L)", command=handOnChestLeft)
   realmenu.add_command(label="Hand on chest (R)", command=handOnChestRight)
   realmenu.add_separator()
   realmenu.add_command(label="Facepalm (L)", command=facepalmLeft)
   realmenu.add_command(label="Facepalm (R)", command=facepalmRight)
   realmenu.add_separator()


   menubar.add_cascade(label="Realistic Gestures", menu=realmenu)

   # TEACHING MENU
   fauxmenu = Menu(menubar, tearoff=0)

   fauxmenu.add_command(label="Hands on Hips", command=handsOnHips2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Shrug", command=largeShrug2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Cheer", command=cheering2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Hands on Head", command=handsOnHead2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Look (L)", command=lookLeft2)
   fauxmenu.add_command(label="Look (R)", command=lookRight2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Can't Hear (L)", command=cantHearLeft2)
   fauxmenu.add_command(label="Can't Hear (R)", command=cantHearRight2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Nod (Yes)", command=nodYes2)
   fauxmenu.add_command(label="Shake (No)", command=shakeNo2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Hand out (L)", command=handOutLeft2)
   fauxmenu.add_command(label="Hand out (R)", command=handOutRight2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Look at nails (L)", command=lookAtNailsLeft2)
   fauxmenu.add_command(label="Look at nails (R)", command=lookAtNailsRight2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Wave (L)", command=waveLeft2)
   fauxmenu.add_command(label="Wave (R)", command=waveRight2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Hand on chest (L)", command=handOnChestLeft2)
   fauxmenu.add_command(label="Hand on chest (R)", command=handOnChestRight2)
   fauxmenu.add_separator()
   fauxmenu.add_command(label="Facepalm (L)", command=facepalmLeft2)
   fauxmenu.add_command(label="Facepalm (R)", command=facepalmRight2)
   fauxmenu.add_separator()


   menubar.add_cascade(label="Cartoon Gestures", menu=fauxmenu)

   root.config(menu=menubar)
   root.mainloop()



##_________________________________MAIN______________________________________##


if __name__ == "__main__":

    robotIp = "10.218.107.156"

    if len(sys.argv) <= 1:
        print "Usage python almotion_openhand.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]
    main(robotIp)


##[80.9*almath.TO_RAD],
##[8.3*almath.TO_RAD],
##[-45.3*almath.TO_RAD],
##[-60.4*almath.TO_RAD],
##[8.7*almath.TO_RAD],

##[80.8*almath.TO_RAD],
##[-8.4*almath.TO_RAD],
##[45.1*almath.TO_RAD],
##[60.1*almath.TO_RAD],
##[-10.6*almath.TO_RAD]]

##Test one: Questions
##That doesn't makes sense?
##I don't know
##Why not?
##Can you tell me?
##I don't know
##Who are you?
##Are you still there?
##Can you hear me?
##How is it going?
##I don't know
##Can you say that again please?
##To be honest, I have no idea what you said?
##I don't know
##What did you say?
##What time is it?
##What do you think?
