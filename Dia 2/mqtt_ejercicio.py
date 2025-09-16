#conectarme a un broker MQTT y publicar un mensaje con python
import paho.mqtt.client as mqtt
import time
import random
import json

#y publicar el mensaje "Hola desde MQTT" en el topico "test/mensaje"
broker_address = "localhost"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker_address)
client.publish("greenhouse/sensors/dev001/status", "online",0,True) #qos 0, retain True


while True:
    #publicar un valor de temperatura aleatorio entre 18 y 30
    #  y humedad entre 30 y 70 
    #en el topico "greenhouse/sensors/dev001/telemetry" cada  5 segundos
    temperature = round(random.uniform(18, 30),1)
    humidity = round(random.uniform(30, 70),1)
    #publicar en formato json, con timestamp
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    payload = {"timestamp":time_stamp,"temperature": temperature, "humidity": humidity}
    print(f"Temperature: {temperature}, Humidity: {humidity}, Timestamp: {time_stamp}")
    client.publish("greenhouse/sensors/dev001/telemetry", json.dumps(payload),1,False) #qos 1, retain False
    time.sleep(5)
