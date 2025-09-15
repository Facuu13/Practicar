#conectarme a un broker MQTT y publicar un mensaje con python
import paho.mqtt.client as mqtt

#y publicar el mensaje "Hola desde MQTT" en el topico "test/mensaje"
broker_address = "localhost"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker_address)
client.publish("test/mensaje", "Hola desde MQTT")
client.disconnect()
