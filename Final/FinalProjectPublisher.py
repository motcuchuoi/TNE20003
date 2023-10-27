import paho.mqtt.client as mqtt
import time
import random

broker_address = "rule28.i4t.swin.edu.au"
broker_port = 1883 # tcp

client_information = dict (
    client_identity = "Subscriber", 
    username = "103532674", 
    password = "103532674",
    messages = ["help", "oxygen", "hungry", "thirsty", "hurt", "insomnia"]
)

topic = "103532674/private_topic"

def connect_mqtt() -> mqtt.Client:
    global broker, client_information

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker!: " +str(rc))
        else:
            print("Failed to connect with code: "+str(rc))
    client = mqtt.Client(client_information["client_identity"])
    client.username_pw_set(client_information["username"], client_information["password"])
    client.on_connect = on_connect
    client.connect(broker_address, broker_port)
    return client 

def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"Messages: {msg_count}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send '{msg}' to topic '{topic}'")
        else:
            print(f"Failed to send message to topic '{topic}'")
        msg_count += 1
        if msg_count > 5:
            break
    disconnect_mqtt(client)

def disconnect_mqtt(client: mqtt.Client):
    def on_disconnect(client, userdata, rc):
        print(f"Disconnected with result code: {rc}")
    client.on_disconnect = on_disconnect
    client.disconnect()

def main():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()

if __name__ == '__main__':
    main()