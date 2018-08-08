# iot-streaming
Sample code for a project about streaming IoT data for streaming analytics using AI

## IoT Platform
subscriber.py is for recieving sensor data from IBM Cloud Streaming Analytics engine and process the raw sensor data using AI and forward (publish) the processed data back to IBM Watson IoT platform. 

## Streaming Analytics
iot_streaming_job.py will be uploaded to IBM Cloud Streaming Analytics engine as a job. IBM Streaming Analytics is an engine to stream data and perform advanced analysis. A job on IBM Streaming Analytics is presented as a flow graph in which each operator (node) has a particular function. This job will work together with the IoTPlatform job (coded in SPL langauge, compiled as a .sab file and uploaded as a job). The function of iot_streaming_job is to stream sensor data from IBM Watson IoT platform and publish back to the IBM Watson IoT Platform as a command. 

## AI
predict_model.py contains code for predictive model training and model persistence. After training, the model will be saved as a .pkl model file for the use by other programs. 
