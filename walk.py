# -*- coding:utf-8 -*-
from naoqi import ALProxy
import math
import argparse
import almath
robotIP = "192.168.1.100"
PORT=9559
motion=ALProxy("ALMotion", robotIP,PORT)
posture=ALProxy("ALRobotPosture",robotIP,PORT)
tts=ALProxy("ALTextToSpeech",robotIP,PORT)
config=[ 
    ["MaxStepX",0.045],
    ["MaxStepY",0.145],
    ["MaxStepFrequency",0.4],
    ["TorsoWx",5.0*almath.TO_RAD]#5度
    ]
Config=[
    ["MaxStepX",0.035],  
    ["MaxStepY",0.145], 
    ["MaxStepFrequency",0.3]
    #["TorsoWx",-0.05]
    #["TorsoWy",0.05]
    ]
posture.goToPosture("StandInit",0.5)
motion.wakeUp()
motion.moveTo(2.5,0.0,0.0,config)
tts.say("左转")
motion.moveTo(0.0,0.0,math.pi/2,Config)
motion.moveTo(1.0,0.0,0.0,config)
tts.say("左转")
motion.moveTo(0.0,0.0,math.pi/2,Config)
motion.moveTo(2,5.0,0.0,config)
motion.rest()
