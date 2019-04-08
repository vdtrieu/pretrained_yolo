#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 James Myatt <james@jamesmyatt.co.uk>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    James Myatt - initial implementation

# This shows a simple example of standard logging with an MQTT subscriber client.

# import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt

# import logging
# logging.basicConfig(level=logging.DEBUG)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.

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

broker = "m16.cloudmqtt.com"
mqttc = mqtt.Client("client")
mqttc.username_pw_set("sknweddk", password="WDBf0aSOTwfY")

mqttc.on_connect  = on_connect
mqttc.on_log = on_log
mqttc.on_message = on_message



mqttc.connect(broker, 12290, 60)
mqttc.subscribe("led", 0)
# mqttc.subscribe("group", 0)
mqttc.publish("led", "on")

mqttc.loop_forever()
