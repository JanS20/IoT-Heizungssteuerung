import paho.mqtt.client as mqtt
import sys
import random
import time

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

raum = sys.argv[1]

def start_client(raum):
    topic = f"haus/raum{raum}/temperatur"

    while True:
        temperatur = round(random.uniform(15, 25), 2)
        client.publish(topic, temperatur)
        print(f"Temperatur gesendet: {topic}: {temperatur} \n")
        time.sleep(5)

start_client(raum)