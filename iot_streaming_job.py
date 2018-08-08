import json
import math
from  streamsx.topology.topology import Topology
from streamsx.topology.context import *
from streamsx.rest import StreamingAnalyticsConnection
from streamsx.topology import schema
import random
from streamsx.topology.topology import Topology
from streamsx.rest import StreamsConnection

#import matplotlib.pyplot as plt
#import numpy as np
#from sklearn import datasets, linear_model
#from sklearn.metrics import mean_squared_error, r2_score
#import ibmiotf.application
#import getopt
#import signal
#import time
#import sys
#import json
#from watson_machine_learning_client import WatsonMachineLearningAPIClient

#wml_credentials = {
#                    "url": "https://us-south.ml.cloud.ibm.com",
#                    "username": "79936c5f-cbb6-4ca3-b6ef-96c9d391daa7",
#                    "password": "7b8ab7fc-dd5f-412b-a908-0803f4fbbaad",
#                    "instance_id": "d9cf99da-7bcd-4570-873f-9541fc7d055f"
#                   }

#client = WatsonMachineLearningAPIClient(wml_credentials)
###
#Set up access to Streaming Analytics service
os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/jdk1.8.0_161.jdk/Contents/Home"

def myEventCallback(event):
    print("%-33s%-30s%s" % (event.timestamp.isoformat(), event.device, event.event + ": " + json.dumps(event.data)))

def interruptHandler(signal, frame):
    client.disconnect()
    sys.exit(0)

def get_service_name():
    ## change the service name here, it would be Streaming Analytics in the screenshot above,
    # and "Streaming-Analytics" if you used the IoT starter kit
    service_name = "Streaming-Analytics-smart-bin"
    return service_name

def get_credentials():
    credentials = """{
          "apikey": "kbvE5nPQjIRImh9I3dP_BBdLV0lgvDt_Zo6mhhinWUMv",
          "bundles_path": "/jax-rs/bundles/service_instances/be3a4de3-e0e3-44f8-8e33-8129905e4498/service_bindings/a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "iam_apikey_description": "Auto generated apikey during resource-key operation for Instance - crn:v1:bluemix:public:streaming-analytics:us-south:a/8ad1df8006c04c80a3e74bb69c13ee92:be3a4de3-e0e3-44f8-8e33-8129905e4498::",
          "iam_apikey_name": "auto-generated-apikey-a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
          "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/8ad1df8006c04c80a3e74bb69c13ee92::serviceid:ServiceId-da015085-cbcd-4f9e-b556-fbbf3eb8c0b0",
          "jobs_path": "/jax-rs/jobs/service_instances/be3a4de3-e0e3-44f8-8e33-8129905e4498/service_bindings/a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "password": "b8591d8d-b0c6-4d67-a36e-7af7cdbe2918",
          "resources_path": "/jax-rs/resources/service_instances/be3a4de3-e0e3-44f8-8e33-8129905e4498/service_bindings/a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "rest_host": "streams-app-service.ng.bluemix.net",
          "rest_port": "443",
          "rest_url": "https://streams-app-service.ng.bluemix.net",
          "size_path": "/jax-rs/streams/size/service_instances/be3a4de3-e0e3-44f8-8e33-8129905e4498/service_bindings/a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "start_path": "/jax-rs/streams/start/service_instances/be3a4de3-e0e3-44f8-8e33-8129905e4498/service_bindings/a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "status_path": "/jax-rs/streams/status/service_instances/be3a4de3-e0e3-44f8-8e33-8129905e4498/service_bindings/a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "stop_path": "/jax-rs/streams/stop/service_instances/be3a4de3-e0e3-44f8-8e33-8129905e4498/service_bindings/a450ef19-01a0-4153-9bad-d3e36b056ab9",
          "userid": "f2d9c913-4517-4a19-99bb-6f6eda000e70",
          "v2_rest_url": "https://streams-app-service.ng.bluemix.net/v2/streaming_analytics/be3a4de3-e0e3-44f8-8e33-8129905e4498"
        }"""
    return credentials

"""Submit the topology to the Streaming analytics service
"""
def submit_to_service(topo):
    service_name = get_service_name()
    credentials = get_credentials()
    vs={'streaming-analytics': [{'name': service_name, 'credentials': json.loads(credentials)}]}
    cfg = {}
    cfg[ConfigParams.VCAP_SERVICES] = vs
    cfg[ConfigParams.SERVICE_NAME] = service_name
    return submit('STREAMING_ANALYTICS_SERVICE', topo, cfg)


def get_cmd(tuple):
    #build the message you wish to send as a dictionary
    payload = {}

    payload["action"] = "Lights"
    payload["msg"] = "test"

    command_data =  {}
    command_data ["d"] = payload

    #convert the whole payload to json
    command_as_json = json.dumps(command_data)

    #build the command metadata. The device id and device type are on the tuple, but you could also specify them manually
    device_cmd ={}
    #device_cmd["typeId"] = tuple["typeId"]
    device_cmd["typeId"] = "SMARTBIN_PI_V2"

    device_cmd["cmdId"] = "display"
        #device_cmd["deviceId"] = tuple["deviceId"]
    device_cmd["deviceId"] = "SMARTBIN001"


    device_cmd["jsonString"] = command_as_json
    print("get_cmd print")
    #cmd_return = {"d": "test"}
    return device_cmd
    #return cmd_return

"""Parse the data from an event we received"""
def get_event_data(tuple):
    payload_json = tuple["jsonString"]
    payload = json.loads(payload_json)
    return payload["d"]

# Create linear regression object
#regr = linear_model.LinearRegression()
# Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)

 #define needed variables
COMMANDS_TOPIC = "streamsx/iot/device/commands/send" #topic to publish commands to
#COMMANDS_TOPIC = "iot-2/type/SMARTBIN_PI_V2/id/SMARTBIN001/cmd/command/fmt/json" #topic to publish commands to
#EVENTS_TOPIC = "iot-2/type/SMARTBIN_PI_V2/id/SMARTBIN001/evt/status/fmt/json" #topic to subscribe to for events
EVENTS_TOPIC = "streamsx/iot/device/events"
incoming_schema =  schema.StreamSchema("tuple <rstring typeId, rstring deviceId, rstring eventId, rstring jsonString>")
cmd_schema = schema.StreamSchema('tuple<rstring typeId, rstring deviceId, rstring cmdId, rstring jsonString>')
#cmd_schema = schema.StreamSchema('tuple<rstring d>')

#Topology object is the Streams application graph
topology = Topology('ReadingsFromIot')

#Subscribe to events
events = topology.subscribe(EVENTS_TOPIC, incoming_schema,"AllEventsAsJSON")
sensor_events = events.filter(lambda tuple: tuple["eventId"] == "status","SensorEventsAsJSON")
# sensor_events operator passes a tuple to get_event_data() function
## use flat_map() to split data such as gps coordinate to x and y, same for sensor data to sensor1, sensor2,...
readings = sensor_events.map(get_event_data,"ReadingsStream")
#print out readings
print("received data: ")
readings.print()

#send a command
cmd_stream = sensor_events.map(get_cmd, "CommandsAsJSON")
#convert the commands stream to a SPL structured schema
commands_to_publish = cmd_stream.map(lambda x : (x["typeId"],x["deviceId"],x["cmdId"],x["jsonString"],), schema = cmd_schema, name="CommandsToPublish")
print("command to publish is: ")
commands_to_publish.print()
#commands_to_publish = cmd_stream.map(lambda x : (x["d"],), schema = cmd_schema, name="CommandsToPublish")

#commands_to_publish.publish(COMMANDS_TOPIC, cmd_schema)
commands_to_publish.publish(COMMANDS_TOPIC, cmd_schema)

result = submit_to_service(topology)
print("Submitted job to the service, job id = " + str(result.job.id))
