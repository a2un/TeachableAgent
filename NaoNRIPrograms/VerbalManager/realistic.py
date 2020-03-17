import time
import almath



##_________________________________REALISTIC GESTURES______________________________________##

# Yawn and stretch
# look at nails left
# Look at nails right
# hands out right
# hands out left
# Large shrug
# Hands on hips
# Wave left
# Wave right
# Nod yes
# Shake no
# Look left
# Look right
# Face palm left
# Face palm right
# Can't hear left
# Can't hear right
# Hands on chest left
# Hands on chest right
# cheering
# Hands on head


def yawnAndStretch(motionProxy):
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


def lookAtNailsLeft(motionProxy):
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


def lookAtNailsRight(motionProxy):
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


def handOutLeft(motionProxy):
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


def handOutRight(motionProxy):
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


def largeShrug(motionProxy):
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


def handsOnHips(motionProxy):
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


def waveLeft(motionProxy):
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


def waveRight(motionProxy):
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


def nodYes(motionProxy):
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


def shakeNo(motionProxy):
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


def lookLeft(motionProxy):
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


def lookRight(motionProxy):
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


def facepalmLeft(motionProxy):
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


def facepalmRight(motionProxy):
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


def cantHearLeft(motionProxy):
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


def cantHearRight(motionProxy):
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


def handOnChestLeft(motionProxy):
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


def handOnChestRight(motionProxy):
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


def handsOut(motionProxy):
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


def cheering(motionProxy):
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


def handsOnHead(motionProxy):
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
