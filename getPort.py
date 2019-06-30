import serial.tools.list_ports as ser
list_ports = ser.comports()
name = ""
for port in list_ports :
	if ("ttyUSB" in port.name):
		name = port.name
    	print(port.device)