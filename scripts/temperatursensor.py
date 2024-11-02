import paho.mqtt.client as mqtt
import concurrent.futures
import random
import time

topics = ["haus/raum1/temperatur", "haus/raum2/temperatur", "haus/raum3/temperatur"]

def start_clients(topic):
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883, 60)

    while True:
        temperatur = round(random.uniform(15, 25), 2)
        client.publish(topic, temperatur)
        print(f"Temperatur gesendet: {topic}: {temperatur} \n")
        time.sleep(5)
        
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(start_clients, topics)