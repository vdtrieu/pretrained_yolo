import json
import paho.mqtt.client as mqtt
import random
import time
import threading
import sys


def pub():
    mqttc.publish("sensor", payload= "temp", qos=0)
    threading.Timer(10, pub).start()

mqttc = mqtt.Client("client1", clean_session=False)
mqttc.username_pw_set("sknweddk", "WDBf0aSOTwfY")
mqttc.connect("m16.cloudmqtt.com", 12290, 60)

pub()