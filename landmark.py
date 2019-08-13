# -*- coding:utf-8 -*-
from naoqi import ALProxy
import math
import almath
robotIP = "192.168.1.101"
PORT=9559
motion=ALProxy("ALMotion",robotIP,PORT)
posture=ALProxy("ALRobotPosture",robotIP,PORT)
tts=ALProxy("ALTextToSpeech",robotIP,PORT)
markProxy= ALProxy("ALLandMarkDetection",robotIP,PORT)
tracker=ALProxy("ALTracker",robotIP,PORT)
useSensors=False
period = 500
H=0.459
L=0.405
theta=39.7*almath.TO_RAD
markProxy.subscribe("Test_Mark",period,0.0)
memProxy=ALProxy("ALMemory",robotIP,PORT)
config=[ 
    ["MaxStepX",0.045],
    ["MaxStepY",0.145],
    ["MaxStepFrequency",0.4],
    ["TorsoWx",5.0*almath.TO_RAD]
    ]
motion.wakeUp()
posture.goToPosture("StandInit",0.5)
for i in range(0,20):
	motion.moveTo(-0.05,0.0,0.0,config)
	data=memProxy.getData("LandmarkDetected",)
	if data:#data为空则没有识别到
		tts.say("检测到mark")
		sensorAngles= motion.getAngles("HeadPitch",useSensors)#获得头部角度数据
		#sen=(math.degrees(sensorAngles[0]))
		#S=((H-L)/2)/math.tan(sen+theta)
		#print(data[1][1][0])
		print(sensorAngles[0])
		#print(S)
		#print(tracker.getTargetCoordinates())
		#tts.say("距离为:%d"%(S))
		exit(0)
	else:
		tts.say("没检测到mark")
		
		
	
		
	   
	
	

