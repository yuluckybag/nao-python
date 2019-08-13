# -*- coding:utf-8 -*-
from naoqi import ALProxy
import almath
import argparse
import threading
from naoqi import ALModule
robotIP = "192.168.1.114"
PORT=9559
n=1
motion=ALProxy("ALMotion",robotIP,PORT)
posture=ALProxy("ALRobotPosture",robotIP,PORT)
tts=ALProxy("ALTextToSpeech",robotIP,PORT)
memory=ALProxy("ALMemory",robotIP,PORT)
config=[ 
    ["MaxStepX",0.045],
    ["MaxStepY",0.145],
    ["MaxStepFrequency",0.4],
    ["TorsoWx",5.0*almath.TO_RAD]#5度
    ]
def run():#行走
	motion.wakeUp()
	posture.goToPosture("StandInit",0.5)
	motion.moveTo(1.0 ,0,0,config)
	#threadLock.acquire()

	#threadLock.release()
	#threadLock = threading.Lock()
def onTouched():#触摸传感器
#防止一次触摸未识别，进行死循环，触摸成功才可退出循环
	while n==1:
		fronthead = memory.getData('FrontTactilTouched')
    #如果触摸成功，则fronthead=1
		if fronthead == 1:
			motion.rest()
			break
#创建
thread1=threading.Thread(target=run)
thread2=threading.Thread(target=onTouched)
#开始进行多线程
thread1.start()
thread2.start()
#结束
thread1.join()
thread2.join()



	

