import serial
import time
import email_ip

fid = open("log.txt", "w")

email_ip.email_ip_addr()

tnow = time.localtime()

ser = serial.Serial('/dev/ttyUSB0', 9600)



# Startup Test Pattern
ser.write('0')
time.sleep(5)
ser.write('1')
time.sleep(5)
ser.write('0')
time.sleep(5)
ser.write('1')



while tnow.tm_yday < 260:
        tnow = time.localtime()
        timestring = "{}.{}.{}.{}.{}.{}".format(tnow.tm_year, tnow.tm_mon, tnow.tm_mday, tnow.tm_hour, tnow.tm_min, tnow.tm_sec)
	if tnow.tm_hour==6 and tnow.tm_min==30:
	    print("{}: Watering".format(timestring)
	    ser.write('0')
	    time.sleep(60)
	    ser.write('1')
	else:
	    time.sleep(60)
	    print("{}: Not watering".format(timestring))
	    ser.write('1')
