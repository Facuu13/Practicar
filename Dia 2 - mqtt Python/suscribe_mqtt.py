import os, csv, json, time
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "greenhouse/sensors/+/telemetry"
CSV_PATH = "data.csv"

def ensure_csv(path):
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["device_id", "ts", "temp_c", "hum_pct"])

def extract_device_id(topic: str) -> str:
    # greenhouse/sensors/<device_id>/telemetry
    parts = topic.split("/")
    return parts[2] if len(parts) >= 4 else "unknown"

def on_connect(client, userdata, flags, rc, properties=None):
    print("[CONNECT] rc=", rc)
    if rc == 0:
        client.subscribe(TOPIC, qos=1)
        print("[SUB]", TOPIC)

def on_message(client, userdata, msg):
    device_id = extract_device_id(msg.topic)
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        row = [device_id, data["ts"], float(data["temp_c"]), float(data["hum_pct"])]
    except Exception as e:
        print("[ERR] payload inválido:", e, msg.payload)
        return
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(row)
    print("[LOG]", row)

def main():
    ensure_csv(CSV_PATH)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="sub-logger")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, 1883, keepalive=30)
    client.loop_forever()

if __name__ == "__main__":
    main()
