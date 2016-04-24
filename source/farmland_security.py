#!/usr/bin/python

import threading
import thread
import time
import RPi.GPIO as GPIO
from subprocess import call
import datetime
from lcd import *
#import dht_read


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
PIR_1=11
PIR_2=12
PIR_3=13
PIR_4=15
PIR_5=16
PIR_6=19

GPIO.setup(PIR_1, GPIO.IN)         #Read output from PIR motion sensor 1
GPIO.setup(PIR_2, GPIO.IN)         #Read output from PIR motion sensor 2
GPIO.setup(PIR_3, GPIO.IN)         #Read output from PIR motion sensor 3
GPIO.setup(PIR_4, GPIO.IN)         #Read output from PIR motion sensor 4
GPIO.setup(PIR_5, GPIO.IN)         #Read output from PIR motion sensor 5
GPIO.setup(PIR_6, GPIO.IN)         #Read output from PIR motion sensor 6



lock = threading.Lock()


def video_record(threadName, delay,lock):
	#avconv -loglevel quiet -f video4linux2 -r 10  -t 00:00:59 -i /dev/video0 test.avi # to record video
	print "Video record thread function called"
	videoFile = '~/farmaland_security/videos/farmVideo-%s.mp4'%datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')	
	recordVideo = "avconv -loglevel quiet -f video4linux2 -r 10  -t 00:00:40 -i /dev/video0 videoFile"   
	call ([recordVideo], shell=True)
	#Upload file to Dropbox
	UploadVid = "./dropbox_uploader.sh upload videoFile servielence_videos/farmVideo-%s.mp4'%datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')"
	call ([UploadVid], shell=True)
	print "Video uploaded to Dropbox"
	
def LCD_Display(threadName, delay,lock):
	while True:
		lcd_string("VISMAYA ",LCD_LINE_1)
	
while True:

	P1=GPIO.input(PIR_1)
	P2=GPIO.input(PIR_2)
	P3=GPIO.input(PIR_3)
	P4=GPIO.input(PIR_4)
	P5=GPIO.input(PIR_5)
	P6=GPIO.input(PIR_6)
       
	if P1+P2+P3+P4+P5+P6==0:	
		#Take picture and video	
		#fswebcam -r 640x480 --jpeg 85 -D 1 shot.jpg # To Capture image
		print "Capture pic File"
		picFile = '~/farmaland_security/pics/farmPic-%s.jpg'%datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
		capturePic = "fswebcam -r 640x480 --jpeg 85 -D 1 picFile"   
		call ([capturePic], shell=True)
		print "Create Record thread"
		thread.start_new_thread(video_record, ("RECORDING VIDEO", 2,lock ) )
		thread.start_new_thread(LCD_Display, ("DISPLAY STRING", 2,lock ) )
		
