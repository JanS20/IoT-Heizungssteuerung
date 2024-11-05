import paho.mqtt.client as mqtt
import logging

SCHWELLWERT_UNTEN = 18.0
SCHWELLWERT_OBEN = 22.0

topics = [("haus/raum1/temperatur", 0), ("haus/raum2/temperatur", 0)]

logging.basicConfig(
    filename="haussteuerung.log", level=logging.INFO, filemode="w", encoding='utf-8',
    format="%(asctime)s - %(levelname)s - %(message)s")

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)
client.subscribe(topics)

def on_message(client, userdata, msg):
    temperatur = float(msg.payload.decode())
    raum = msg.topic.split("/")[1]
    
    print(f"Eingegangene Temperatur von {msg.topic}: {temperatur}")
    logging.info(f"Eingegangene Temperatur von {msg.topic}: {temperatur}")

    if temperatur < SCHWELLWERT_UNTEN:
        action = "heizung_hoch"
        print("Temperatur zu niedrig")
        client.publish(f"haus/{raum}/thermostat", action)
        logging.info(f"Veröffentlichte Nachricht an haus/{raum}/thermostat: {action}")
    elif temperatur > SCHWELLWERT_OBEN:
        action = "heizung_runter"
        print("Temperatur zu hoch")
        client.publish(f"haus/{raum}/thermostat", action)
        logging.info(f"Veröffentlichte Nachricht an haus/{raum}/thermostat: {action}")
    print("\n")
        
client.on_message = on_message
client.loop_forever()