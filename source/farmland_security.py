#!/usr/bin/python

import threading
import thread
import time
import RPi.GPIO as GPIO
from subprocess import call
import datetime
from lcd import *
import dht11
from serial import *

LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

print "10"
PIR_1=11
PIR_2=12
PIR_3=13
PIR_4=15
PIR_5=16
PIR_6=19
print "10"
GPIO.setup(PIR_1, GPIO.IN)         #Read output from PIR motion sensor 1
GPIO.setup(PIR_2, GPIO.IN)         #Read output from PIR motion sensor 2
GPIO.setup(PIR_3, GPIO.IN)         #Read output from PIR motion sensor 3
GPIO.setup(PIR_4, GPIO.IN)         #Read output from PIR motion sensor 4
GPIO.setup(PIR_5, GPIO.IN)         #Read output from PIR motion sensor 5
GPIO.setup(PIR_6, GPIO.IN)         #Read output from PIR motion sensor 6
Phone_No = +918171707160

GPIO.setup(14, GPIO.IN)
instance = dht11.DHT11(pin = 14)
#

lcd_init()
lock = threading.Lock()
lcd_string("Farmland Security",LCD_LINE_1)
lcd_string("System Booted",LCD_LINE_2)
time.sleep(3)
def video_record(threadName, delay,lock):
	#avconv -loglevel quiet -f video4linux2 -r 10  -t 00:00:59 -i /dev/video0 test.avi # to record video
	print "Video record thread function called"
	videoFile = '~/farmland_security/videos/farmVideo-%s.mp4'%datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')	
	recordVideo = "avconv -loglevel quiet -f video4linux2 -r 10  -t 00:00:40 -i /dev/video0 videoFile"   
	call ([recordVideo], shell=True)
	#Upload file to Dropbox
	UploadVid = "./dropbox_uploader.sh upload videoFile servielence_videos/farmVideo-%s.mp4'%datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')"
	call ([UploadVid], shell=True)
	print "Video uploaded to Dropbox"
	
def LCD_Display(threadName, delay,lock):
	while True:
		result = instance.read()
		lock.acquire()
		if result.is_valid():
			
			lcd_string("Farmland ",LCD_LINE_1)
			lcd_string("Security ",LCD_LINE_2)
		else:
			lcd_string("Temp Read Err",LCD_LINE_1)
		lock.release()
		time.sleep(3)
		print "************Inside LCD function********"
		
		
print "Create LCD thread"		
thread.start_new_thread(LCD_Display, ("DISPLAY STRING", 2,lock ) )
	
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
		picFile = '~/farmland_security/pics/farmPic-%s.jpg'%datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
		capturePic = "fswebcam -r 640x480 --jpeg 85 -D 1 picFile"   
		call ([capturePic], shell=True)
		print "Create Record thread"
		thread.start_new_thread(video_record, ("RECORDING VIDEO", 2,lock ) )
		lcd_byte(0x01, LCD_CMD)
		lock.acquire()
		lcd_string("Waiting for RFID scan...",LCD_LINE_1)
		ser = Serial("/dev/ttyUSB0", baudrate=9600, timeout=5)
		data = ser.read(8)
		if data:
			print data
			lcd_byte(0x01, LCD_CMD)
			lcd_string("Authorised person",LCD_LINE_1)
			lcd_string("Entry Permitted",LCD_LINE_2)
			#SMS
		else:
			lcd_string("Unauthorised person",LCD_LINE_1)
		lock.release()
		
	time.sleep(3)
	lcd_byte(0x01, LCD_CMD)
	
