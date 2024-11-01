import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)
client.subscribe("haus/raum1/thermostat")

def on_message(client, userdata, msg):
    befehl = msg.payload.decode()
    if befehl == "heizung_hoch":
        print("Heizung wird hochgedreht")
    elif befehl == "heizung_runter":
        print("Heizung wird runtergedreht")
    print("\n")

client.on_message = on_message
client.loop_forever()
