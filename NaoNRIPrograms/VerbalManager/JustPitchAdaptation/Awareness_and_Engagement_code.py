#! /usr/bin/env python
# -*- encoding: UTF-8 -*-



from Tkinter import *
import sys
import argparse
import qi
from naoqi import ALProxy

import qi
import argparse
import sys


def getBatteryInfo(robotIP):
    PORT = 9559

    try:
        batteryProxy = ALProxy("ALBattery", robotIP, PORT)
        print "proxy created"
    except Exception, e:
        print "Could not create proxy"

    result = batteryProxy.getBatteryCharge()
    print result


def getDiagnostics(robotIP):
    PORT = 9559

    try:
        diagnosisProxy = ALProxy("ALDiagnosis", robotIP, PORT)
        print "proxy created"
    except Exception, e:
        print "Could not create proxy"

    print diagnosisProxy.getActiveDiagnosis()
    print diagnosisProxy.getPassiveDiagnosis()
    print diagnosisProxy.isNotificationEnabled()

def basicAwareness(robotIP):
    PORT = 9559

    try:
        awarenessProxy = ALProxy("ALBasicAwareness", robotIP, PORT)
        awarenessProxy.stopAwareness()
        print "worked"
    except Exception, e:
        print "Could not create proxy "
        print "Error was: ", e

    # things the robot can react to

    awarenessProxy.setEngagementMode("FullyEngaged")


def main(robotIP):
    #basicAwareness(robotIP)
    getDiagnostics(robotIP)
    getBatteryInfo(robotIP)

if __name__ == "__main__":
    robotIP = "10.218.108.148"
    main(robotIP)

# levels of engagement may also be relevant

# “Unengaged”: (Default mode) when the robot is engaged with a user, it can be distracted by any stimulus, and engage with another person.
# “FullyEngaged”: as soon as the robot is engaged with a person, it stops listening to stimuli and stays engaged with the same person.
#                 If it loses the engaged person, it will listen to stimuli again and may engage with a different person.
# “SemiEngaged”: when the robot is engaged with a person, it keeps listening to the stimuli, and if it gets a stimulus,
#                it will look in its direction, but it will always go back to the person it is engaged with. If it loses the person,
#                it will listen to stimuli again and may engage with a different person.


'''
def main(session):
    """
    This example uses the setAutonomousAbilityEnabled method.
    """
    # Get the service ALAutonomousLife.

    life_service = session.service("ALAutonomousLife")
    life_service.setAutonomousAbilityEnabled("BasicAwareness", True)
    value = life_service.getAutonomousAbilityEnabled("BasicAwareness")
    print value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.218.106.38",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)




def basicAwareness(robotIP, PORT):
    try:
        awarenessProxy = ALProxy("ALBasicAwareness", robotIP, PORT)
        print "worked"
    except Exception, e:
        print "Could not create proxy "
        print "Error was: ", e


    awarenessProxy.stopAwareness()


def main(robotIP):
   PORT = 9559

   try:
        awarenessProxy = ALProxy("ALBasicAwareness", robotIP, PORT)
        print "worked"
   except Exception, e:
        print "Could not create proxy "
        print "Error was: ", e

   # things the robot can react to
   # try setting some to false and see what you prefer
   awarenessProxy.setStimulusDetectionEnabled("Sound", True)
   awarenessProxy.setStimulusDetectionEnabled("Movement", True)
   awarenessProxy.setStimulusDetectionEnabled("People", False)
   awarenessProxy.setStimulusDetectionEnabled("Touch", True)

   # levels of engagement may also be relevant
   
   # “Unengaged”: (Default mode) when the robot is engaged with a user, it can be distracted by any stimulus, and engage with another person.
   # “FullyEngaged”: as soon as the robot is engaged with a person, it stops listening to stimuli and stays engaged with the same person.
   #                 If it loses the engaged person, it will listen to stimuli again and may engage with a different person.
   # “SemiEngaged”: when the robot is engaged with a person, it keeps listening to the stimuli, and if it gets a stimulus,
   #                it will look in its direction, but it will always go back to the person it is engaged with. If it loses the person,
   #                it will listen to stimuli again and may engage with a different person.

   awarenessProxy.setEngagementMode("FullyEngaged")
    
if __name__ == "__main__":

    robotIP = "10.218.106.38"


    main(robotIP)
'''