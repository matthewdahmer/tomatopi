import serial
import time
import email_ip

fid = open("log.txt", "w")

email_ip.email_ip_addr()

tnow = time.localtime()

ser = serial.Serial('/dev/ttyUSB0', 9600)

timestring = "{}.{}.{}.{}.{}.{}".format(tnow.tm_year, tnow.tm_mon, tnow.tm_mday, tnow.tm_hour, tnow.tm_min, tnow.tm_sec)
print("{}: Water On".format(timestring))
fid.write("{}: Water On\n".format(timestring))

ser.write('0')
time.sleep(600)
ser.write('1')

tnow = time.localtime()
timestring = "{}.{}.{}.{}.{}.{}".format(tnow.tm_year, tnow.tm_mon, tnow.tm_mday, tnow.tm_hour, tnow.tm_min, tnow.tm_sec)
print("{}: Water Off\n".format(timestring))
fid.write("{}: Water Off\n".format(timestring))
fid.close()
