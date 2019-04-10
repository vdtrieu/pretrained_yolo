import threading
import time
import paho.mqtt.client as mqtt
import numpy as np
import serial
import os

GROUP1 = "1"
GROUP2 = "2"
ALL = "3"
ON = "4"
OFF = "5"
UART_PORT = "ttyUSB0"

command = ""

class myThread (threading.Thread):                  #UART communication
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        # print_time(self.name, self.counter, 3)
        # read_data_uart()

        # Free lock to release next thread
        threadLock.release()

class myThread2 (threading.Thread):                 # MQTT cloud communication
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        # print_time(self.name, self.counter, 3)

        broker = "m16.cloudmqtt.com"
        user = "sknweddk"
        pw = "WDBf0aSOTwfY"
        port = 12290

        id = np.random.randint(1,10)              # to avoid dupplicating client id 
        mqttc = mqtt.Client("client-" + str(id))

        mqttc.username_pw_set(user, password=pw)

        mqttc.on_connect  = on_connect
        mqttc.on_log = on_log
        mqttc.on_message = on_message

        mqttc.connect(broker, port, 60)
        mqttc.subscribe("led", 0)
        mqttc.subscribe("group", 0)
        mqttc.publish("led", "on")

        mqttc.loop_forever()

        # Free lock to release next thread
        threadLock.release()

def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print ("Connect OK")
    else:
        print("Bad connection, return code = ", rc)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    command = msg.payload.decode("utf-8")
    write_command_uart(command)
    
def read_data_uart():
    with serial.Serial('/dev/' + UART_PORT, 115200, timeout = 1) as ser:
        data = ser.readline()   # read a '\n' terminated line
        print("Root say: " + data)

def write_command_uart(cmd):
    if (cmd == "group1"):
        # os.system("echo " + GROUP1 + " > /dev/" + UART_PORT)
        print("echo " + GROUP1 + " > /dev/" + UART_PORT)     
    elif (cmd == "group2"):
        # os.system("echo " + GROUP2 + " > /dev/" + UART_PORT)
        print("echo " + GROUP2 + " > /dev/" + UART_PORT)
    elif (cmd == "all"):
        # os.system("echo " + ALL + " > /dev/" + UART_PORT)
        print("echo " + ALL + " > /dev/" + UART_PORT)
    elif (cmd == "on"):
        # os.system("echo " + ON + " > /dev/" + UART_PORT)
        print("echo " + ON + " > /dev/" + UART_PORT)
    elif (cmd == "off"):
        # os.system("echo " + OFF + " > /dev/" + UART_PORT)
        print("echo " + OFF + " > /dev/" + UART_PORT)
    else:
        print("Invalid!")

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")