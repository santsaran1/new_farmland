import serial
serial = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=5)

data = serial.read(8)
if data:
  print data
else:
  print "Unauthorised Person Entered"
