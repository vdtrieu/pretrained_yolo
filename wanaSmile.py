import serial
import os

GROUP1 = "1"
GROUP2 = "2"
ALL = "3"
ON = "4"
OFF = "5"

a = raw_input("Command: ")
print("Type \"exit\" to exit")


while True:
	if (a == "group1"):
		os.system("echo " + GROUP1 + " > /dev/ttyUSB0")
		print("echo " + GROUP1 + " > /dev/ttyUSB0")
		
	elif (a == "group2"):
		os.system("echo " + GROUP2 + " > /dev/ttyUSB0")
		print("echo " + GROUP2 + " > /dev/ttyUSB0")
	elif (a == "all"):
		os.system("echo " + ALL + " > /dev/ttyUSB0")
		print("echo " + ALL + " > /dev/ttyUSB0")
	elif (a == "on"):
		os.system("echo " + ON + " > /dev/ttyUSB0")
		print("echo " + ON + " > /dev/ttyUSB0")
	elif (a == "off"):
		os.system("echo " + OFF + " > /dev/ttyUSB0")
		print("echo " + OFF + " > /dev/ttyUSB0")
	elif (a == "exit"):
		break
	else:
		print("Invalid!Again:")
		
		
	with serial.Serial('/dev/ttyUSB0', 115200, timeout=1) as ser:
		# ser = serial.Serial('/dev/ttyUSB0')  # open serial port
		
			
		# print(ser.name)         # check which port was really used
		
		
		# ser.write("a".encode())     	# write a string
		data = ser.readline()   # read a '\n' terminated line
		print("Root say: " + data)
		# ser.close()             	# close port
