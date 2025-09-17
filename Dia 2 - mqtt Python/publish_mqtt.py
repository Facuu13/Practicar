import json, random, time, socket
from datetime import datetime, timezone
import paho.mqtt.client as mqtt

BROKER = "localhost"
DEVICE_ID = "dev001"
TOPIC_TELE = f"greenhouse/sensors/{DEVICE_ID}/telemetry"
TOPIC_STATUS = f"greenhouse/sensors/{DEVICE_ID}/status"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"pub-{DEVICE_ID}-{socket.gethostname()}")

# Last Will: si se cae sin cerrar, broker publica "offline" retenido
client.will_set(TOPIC_STATUS, payload="offline", qos=1, retain=True)

client.connect(BROKER, 1883, keepalive=30)
client.loop_start()

# Anuncia online retenido
client.publish(TOPIC_STATUS, "online", qos=1, retain=True)

try:
    while True:
        msg = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "temp_c": round(random.uniform(18, 30), 2),
            "hum_pct": round(random.uniform(30, 70), 2),
        }
        payload = json.dumps(msg, separators=(",", ":"))
        client.publish(TOPIC_TELE, payload, qos=1, retain=False)
        print("[PUB]", payload)
        time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    # Pone offline retenido al salir ordenado (consistente con will)
    client.publish(TOPIC_STATUS, "offline", qos=1, retain=True)
    client.loop_stop()
    client.disconnect()
