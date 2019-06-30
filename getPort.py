import serial.tools.list_ports as ser
list_ports = ser.comports()
for port in list_ports :
    print(port.device)