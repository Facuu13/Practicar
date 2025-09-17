
# 📝 Día 4 — Backend API (primero en Node.js, luego en FastAPI)

## 🎯 Objetivo

Construir una **API REST** mínima que exponga lecturas de sensores en **JSON**.

---

## Parte A — Node.js (Express)

### A1. Setup

* Crear un proyecto Node:

  * `npm init -y`
  * Instalar `express` y (opcional) `dotenv`.
* Archivo principal: `server.js` o `app.js`.
* Puerto por defecto: `3000`.

### A2. Fuente de datos (fase 1: simple)

* Usar un **arreglo/diccionario en memoria** con lecturas de `dev001` (10 items).
  Cada lectura: `{ device_id, ts_utc (ISO8601), temp_c, hum_pct }`.

*(Más adelante, en fase 2 opcional, vas a reemplazarlo por MySQL/Mongo.)*

### A3. Endpoints requeridos

1. `GET /latest/:device_id`

   * Devuelve **la última** lectura (por `ts_utc` descendente).
   * Respuesta ejemplo:

     ```json
     { "device_id":"dev001","ts_utc":"2024-06-01T19:00:00Z","temp_c":31.5,"hum_pct":90.0 }
     ```
   * Si no hay datos: status **404** con `{ "error": "no data" }`.

2. `GET /average/:device_id`

   * Calcula **promedio** de `temp_c` y `hum_pct` del device.
   * Respuesta ejemplo:

     ```json
     { "device_id":"dev001","avg_temp_c":25.3,"avg_hum_pct":62.1,"count":10 }
     ```
   * Si no hay datos: **404**.

### A4. Endpoint opcional

3. `GET /all/:device_id?limit=N`

   * Devuelve las **últimas N** lecturas (por defecto N=5).
   * Validar `limit` (1–100). Si es inválido: **400**.

### A5. Validaciones mínimas

* Normalizar `device_id` a minúsculas.
* Asegurar `Content-Type: application/json`.
* Manejo de errores con middleware (500 -> `{ "error":"internal" }`).

### A6. Pruebas manuales

* Con `curl` o Postman:

  * `GET http://localhost:3000/latest/dev001`
  * `GET http://localhost:3000/average/dev001`
  * `GET http://localhost:3000/all/dev001?limit=5`

### A7. Entregables (Node.js)

* `package.json` (con script `"start": "node server.js"`).
* `server.js` (o `app.js`) con los endpoints.
* `README.md` cortito: cómo correr (`npm install && npm start`) y ejemplos de curl.


---

## Parte B — FastAPI (Python) — después de Node

Cuando termines Node.js, repetimos la misma API en **FastAPI**:

### B1. Setup

* Crear entorno, instalar `fastapi` y `uvicorn`.
* Archivo principal: `main.py`.
* Puerto por defecto: `8000`.

### B2. Fuente de datos

* Mismo arreglo/diccionario en memoria que en Node (copiá los datos).

### B3. Endpoints (idénticos)

* `GET /latest/{device_id}`
* `GET /average/{device_id}`
* Opcional: `GET /all/{device_id}?limit=N`

### B4. Validaciones y respuestas

* Usar modelos Pydantic (opcional, recomendado).
* Responder JSON + 404 cuando corresponda.

### B5. Pruebas

* `uvicorn main:app --reload`
* Probar con curl o abrir **Docs automáticas** en `http://localhost:8000/docs`.

### B6. Entregables (FastAPI)

* `requirements.txt` o `pyproject.toml`.
* `main.py`.
* `README.md` con comandos y ejemplos.


