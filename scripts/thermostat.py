import paho.mqtt.client as mqtt

topics = [("haus/raum1/thermostat", 0), ("haus/raum2/thermostat", 0), ("haus/raum3/thermostat", 0)]

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)
client.subscribe(topics)

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