import paho.mqtt.client as mqtt
import time

broker_address = 'rule28.i4t.swin.edu.au'
broker_port = 1883 # tcp port

client_information = dict ( # declare a dictionary with these following keywords and values
    client_identity = "Subscriber", 
    username = "103532674", # login info
    password = "103532674" # login info
)

topics = [("103532674/private_topic", 0), ("public/#",0)]
def connect_mqtt(): 
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker!: {}".format(rc))
            for topic, qos in topics:
                client.subscribe(topic,qos)
        else:
            print("Failed to connect with code: "+str(rc))
    client = mqtt.Client(client_information["client_identity"])
    client.username_pw_set(client_information["username"], client_information["password"])
    client.on_connect = on_connect
    client.connect(broker_address, broker_port)
    return client     
# reference: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python 
   
def subscribe(client: mqtt.Client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' from {msg.topics} topic")
    client.subscribe(topics)
    client.on_message = on_message

def main():
    client = connect_mqtt
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    main()
