import serial
import time
import email_ip

email_ip.email_ip_addr()

ser = serial.Serial('/dev/ttyUSB0', 9600)

# Startup Test Pattern
ser.write('0')
time.sleep(5)
ser.write('1')
time.sleep(5)
ser.write('0')
time.sleep(5)
ser.write('1')

while 1 > 0:
        tnow = time.localtime()
	if tnow.tm_hour==13 and tnow.tm_min==55:
	    print("It's Time!")
	    ser.write('0')
	    time.sleep(60)
	    ser.write('1')
	else:
	    time.sleep(60)
	    print("Not Time")
	    ser.write('1')
