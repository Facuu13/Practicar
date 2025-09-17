# 📝 Día 2 – Ejercicio: Cliente MQTT en Python

## Objetivo
Simular un **sensor de invernadero** que publique datos por MQTT y un **logger** que los reciba y guarde.

---

## Parte 1 – Publisher
1. Crear un script en Python que se conecte a un **broker MQTT** (ej: Mosquitto en `localhost:1883`).
2. El script debe publicar cada **5 segundos** un mensaje con datos simulados:
   - `timestamp` (en formato ISO8601, UTC)
   - `temp_c` (valor random entre 18–30 °C)
   - `hum_pct` (valor random entre 30–70 %)
3. El mensaje debe ir en formato **JSON** y publicarse en el topic:
   greenhouse/sensors/dev001/telemetry

4. Usar **QoS = 1**.
5. Al conectarse, publicar `"online"` en el topic:
  greenhouse/sensors/dev001/status
con la flag **retained**.
6. Configurar un **Last Will** en el mismo topic para que, si el cliente se cae, el broker publique `"offline"`.

---

## Parte 2 – Subscriber
1. Crear otro script en Python que se conecte al mismo broker.
2. Debe **suscribirse** al topic:
    greenhouse/sensors/+/telemetry
(así escucha a todos los `device_id`).
3. Cada mensaje recibido debe:
- Parsear el JSON.
- Guardar los datos en un archivo `data.csv` con columnas:
  ```
  device_id, ts, temp_c, hum_pct
  ```
- Imprimir en consola los valores recibidos.

---

## Extras (opcionales, si querés subir dificultad)
- Manejar errores si el JSON viene corrupto.
- Si el broker se cae, reconectar automáticamente.
- Agregar más “sensores” cambiando el `device_id` y verificar que el CSV los distinga.

---

## 👉 Entregable
- Un script `publisher.py` (el que simula el sensor).
- Un script `logger.py` (el que recibe y guarda en CSV).

---

