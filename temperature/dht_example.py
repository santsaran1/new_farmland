import RPi.GPIO as GPIO
import dht11
import time
import sys

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 14)
while True:
	result = instance.read()
	if result.is_valid():
    		print("Temperature: %d C" % result.temperature)
    		print("Humidity: %d %%" % result.humidity)
    		print("Error: %d" % result.error_code)
	else:
    		print("Error: %d" % result.error_code)
	print("***************************");
	sys.stdout.flush()
	time.sleep(5)
