import paho.mqtt.client as mqtt
import json
`from sklearn.externals import joblib

#print("Loading ML model====================")
#clf = joblib.load('linreg.pkl')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("iot-2/type/SMARTBIN_PI_V2/id/SMARTBIN001/cmd/display/fmt/json")
    # client.subscribe("iot-2/cmd/display/fmt/json")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #print(msg.payload.decode("utf-8"))
    #m_in=json.loads(msg.payload.decode("utf-8"))
    #print(m_in)
    #s1 = m_in["d"][0]["devDist"]
    #s2 = m_in["d"][1]["devDist"]
    #s3 = m_in["d"][2]["devDist"]
    #s4 = m_in["d"][3]["devDist"]
    #data = [[s1],[s2],[s3],[s4]]
    #print(data.shape)
    #print("Predicting====================")
    #y_pred = clf.predict(data)
    #print(y_pred)
    # re-publish to IoT platform
    client.publish("iot-2/type/SMARTBIN_PI_V2/id/SMARTBIN_Dummy/evt/predict/fmt/json", payload=str(msg.payload))

print("Setting up IoT Platform====================")
#client = mqtt.Client(client_id="a:ayppe6:2jj2jizb7j")
client = mqtt.Client(client_id="d:ayppe6:SMARTBIN_PI_V2:SMARTBIN_Dummy")
#client.username_pw_set("a-ayppe6-yzoja1z7nl", password="ypibjSTfiYJgT5ui9a")
#client.username_pw_set("a-ayppe6-yzoja1z7nl", password="ypibjSTfiYJgT5ui9a")
client.username_pw_set("use-token-auth", password="ASDFGHJKL")

client.on_connect = on_connect
client.on_message = on_message

client.connect("ayppe6.messaging.internetofthings.ibmcloud.com", 1883, 60)
#client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
