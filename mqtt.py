import paho.mqtt.client as mqtt 

broker="m21.cloudmqtt.com"
port=17363
username="toyeerbnp"
username="steve1e"
password="JUlkU47AEy86o"

client = mqtt.Client("Python1",clean_session=CLEAN_SESSION)
client.username_pw_set(username, password)
client.connect(broker,port)