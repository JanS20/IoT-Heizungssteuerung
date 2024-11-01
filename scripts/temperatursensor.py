import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

while True:
    temperatur = round(random.uniform(15, 25), 2)
    client.publish("haus/raum1/temperatur", temperatur)
    print(f"Temperatur gesendet: {temperatur} \n")
    time.sleep(5)
