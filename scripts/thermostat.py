import paho.mqtt.client as mqtt
import sys

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

raum = sys.argv[1]
topic = (f"haus/raum{raum}/thermostat", 0)
client.subscribe(topic)

def on_message(client, userdata, msg):
    befehl = msg.payload.decode()
    raum = msg.topic.split("/")[1]
    
    if befehl == "heizung_hoch":
        print(f"Heizung wird in {raum} hochgedreht")
    elif befehl == "heizung_runter":
        print(f"Heizung wird in {raum} runtergedreht")
    print("\n")
    
client.on_message = on_message
client.loop_forever()