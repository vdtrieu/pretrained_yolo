
import os

MULT_GROUP1 = "1";
MULT_GROUP2 = "2";

a = raw_input("here: ")
while True:
	
	if (a == "group1"):
		print(MULT_GROUP1)
		# os.system("echo " + MULT_GROUP1 + " > /dev/ttyS1")
		print("echo " + MULT_GROUP1 + " > /dev/ttyS1")
		break
	elif (a == "group2"):
		print(MULT_GROUP2)
		break
	elif (a == "exit"):
		break
	else:
		print("Invalid!Again:")
		a = raw_input("here: ")
		
# with serial.Serial('/dev/ttyS1', 115200, timeout=1) as ser:
# 	# ser = serial.Serial('/dev/ttyUSB0')  # open serial port
	
		
# 	print(ser.name)         # check which port was really used
	
	
# 	# ser.write("a".encode())     	# write a string
# 	# line = ser.readline()   # read a '\n' terminated line
# 	# print(line)
# 	ser.close()             	# close port
