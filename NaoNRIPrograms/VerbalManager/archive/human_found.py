#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to Find Human with BasicAwareness"""

import qi
import argparse
import sys
import time


class HumanTrackedEventWatcher(object):
    """ A class to react to HumanTracked and PeopleLeft events """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(HumanTrackedEventWatcher, self).__init__()
        app.start()
        session = app.session
        self.subscribers_list = []

        # Get the services 
        self.memory = session.service("ALMemory")
        self.basic_awareness = session.service("ALBasicAwareness")
        self.motion = session.service("ALMotion")
        self.connect_callback("ALBasicAwareness/HumanTracked",
                              self.on_human_tracked)
        self.connect_callback("ALBasicAwareness/HumanLost",
                              self.on_people_left)

    def connect_callback(self, event_name, callback_func):
        """ connect a callback for a given event """
        subscriber = self.memory.subscriber(event_name)
        subscriber.signal.connect(callback_func)
        self.subscribers_list.append(subscriber)

    def on_human_tracked(self, value):
        """ callback for event HumanTracked """
        print "got HumanTracked: detected person with ID:", str(value)
        if value >= 0:  # found a new person
            self.motion.wakeUp()
            position_human = self.get_people_perception_data(value)
            [x, y, z] = position_human
            print "The tracked person with ID", value, "is at the position:", \
                "x=", x, "/ y=",  y, "/ z=", z

    def on_people_left(self, value):
        """ callback for event PeopleLeft """
        print "got PeopleLeft: lost person", str(value)
        self.motion.rest()


    def get_people_perception_data(self, id_person_tracked):
        memory_key = "PeoplePerception/Person/" + str(id_person_tracked) + \
                     "/PositionInWorldFrame"
        return self.memory.getData(memory_key)

    def run(self):
        #start
        self.motion.wakeUp()
        self.basic_awareness.setEngagementMode("FullyEngaged")
        self.basic_awareness.startAwareness()

        #loop on
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, shutting down"
            #stop
            self.basic_awareness.stopAwareness()
            self.motion.rest()
            sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.218.107.182",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["HumanTrackedEventWatcher", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    human_tracked_event_watcher = HumanTrackedEventWatcher(app)
    human_tracked_event_watcher.run()
