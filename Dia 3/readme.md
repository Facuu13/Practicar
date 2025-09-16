# 📝 Día 3 — Persistencia de telemetría en SQL (MySQL) y NoSQL (MongoDB)

¡Vamos con el Día 3! 📊  
**Tema**: Persistencia de telemetría en **SQL (MySQL)** y **NoSQL (MongoDB)**. Sin código por ahora: solo **enunciado claro + tareas** y criterios de entrega.

---

## 📝 Enunciado general

Tomando las lecturas del Día 2 (o simuladas), vas a:

1. **Modelar** y **crear** el esquema en MySQL y en MongoDB.
2. **Insertar** lecturas desde un script (puede ser Python) en ambos motores.
3. **Consultar y agregar**: obtener promedios por hora y últimos N registros.
4. **Optimizar** con índices mínimos necesarios.
5. **Exportar** resultados (CSV en SQL; JSON en NoSQL).

---

## Parte A — MySQL (SQL)

### A1. Modelado y DDL

- Crear base de datos `greenhouse`.
- Crear tabla `readings` con las columnas:
  - `id` BIGINT AUTO_INCREMENT PRIMARY KEY
  - `device_id` VARCHAR(32) NOT NULL
  - `ts_utc` DATETIME(6) NOT NULL (UTC)
  - `temp_c` DECIMAL(5,2) NOT NULL
  - `hum_pct` DECIMAL(5,2) NOT NULL
- Índices:
  - INDEX `idx_dev_ts` (`device_id`, `ts_utc`)
- **Reglas**:
  - `ts_utc` debe ser UTC (no hora local).
  - `temp_c` ∈ [-40, 85]; `hum_pct` ∈ [0, 100] (validar antes de insertar, no hace falta CHECK si no querés).

**Entregable A1**: script SQL `schema_mysql.sql` con `CREATE DATABASE`, `CREATE TABLE`, e índices.

---

### A2. Inserciones (ingesta)

- Escribir un script que inserte **al menos 100 lecturas** para `dev001` y **50 para dev002** (total ≥150 filas).
- Los timestamps deben cubrir **≥3 horas** para que tenga sentido agrupar por hora.

**Entregable A2**: `ingest_mysql.py` (o el lenguaje que elijas) que:
- Conecta a MySQL.
- Inserta en `readings(device_id, ts_utc, temp_c, hum_pct)`.
- Imprime cuántas filas insertó.

---

### A3. Consultas

1. **Últimas 10 lecturas** de `dev001`, ordenadas descendente por `ts_utc`.
2. **Promedio por hora** (temp y hum) de `dev001` en un rango `[T0, T1]`:
   - Resultado: `hour_ts, avg_temp, avg_hum` (hora “redondeada”/truncada a la hora).
3. **Top 3 horas más calientes** (mayor `avg_temp`) para `dev001` en todo el período insertado.

**Entregable A3**: `queries_mysql.sql` con 3 `SELECT` que resuelvan lo anterior.

---

### A4. Exportar CSV

- Exportar el resultado del punto A3(2) a `hourly_averages_mysql.csv`.

**Entregable A4**: el archivo `hourly_averages_mysql.csv` generado (o el script que lo genere).

---

### A5. Performance mínima

- Explicar en un README corto por qué el índice (`device_id`, `ts_utc`) es suficiente para tus consultas.
- (Opcional) medir tiempos con y sin índice (pequeña nota).

**Entregable A5**: `README_mysql.md` (máx 10 líneas).

---

## Parte B — MongoDB (NoSQL)

### B1. Modelado (colección + índice)

- Base/DB: `greenhouse`.
- Colección: `readings`.
- Documento por lectura (ejemplo):
  ```json
  {
    "device_id": "dev001",
    "ts_utc": { "$date": "2025-09-16T15:10:00Z" },
    "temp_c": 23.45,
    "hum_pct": 51.20
  }

  ## Parte B — MongoDB (NoSQL)

### B1. Modelado (colección + índice)

* Base/DB: `greenhouse`.
* Colección: `readings`.
* Documento por lectura (ejemplo):

  ```json
  {
    "device_id": "dev001",
    "ts_utc": { "$date": "2025-09-16T15:10:00Z" },
    "temp_c": 23.45,
    "hum_pct": 51.20
  }
  ```
* Índices:

  * Compuesto `{ device_id: 1, ts_utc: 1 }`.

**Entregable B1**: `schema_mongo.txt` describiendo la colección e índices (y/o script `create_index.js`).

---

### B2. Inserciones (ingesta)

* Insertar **≥150 documentos** (al menos 100 de `dev001` y 50 de `dev002`), cubriendo ≥3 horas.
* Validar rangos antes de insertar (mismo criterio que SQL).

**Entregable B2**: `ingest_mongo.py` (o `mongoimport` con un JSON preparado).

---

### B3. Consultas (Aggregation)

1. **Últimas 10 lecturas** de `dev001` (orden desc por `ts_utc`).
2. **Promedio por hora** para `dev001` en rango `[T0, T1]`:

   * Pipeline con `$match` (por device y rango), `$group` por hora (usar `$dateTrunc` o `$dateToString`), y `$project`.
   * Resultado: `hour_ts, avg_temp, avg_hum`.
3. **Top 3 horas más calientes** (mayor promedio de `temp_c`) para `dev001`.

**Entregable B3**: `aggregations_mongo.js` con los pipelines.

---

### B4. Exportar JSON

* Exportá el resultado del punto B3(2) a `hourly_averages_mongo.json`.

**Entregable B4**: archivo exportado (o script que lo genere).

---

### B5. Performance mínima

* Justificar brevemente el índice `{ device_id: 1, ts_utc: 1 }` para `$match` + sort/paginación.
* (Opcional) agregar un ejemplo de paginación por `_id` o `ts_utc`.

**Entregable B5**: `README_mongo.md` (máx 10 líneas).

---

## Criterios de aceptación (checklist rápido)

* [ ] MySQL: tabla creada con índice compuesto.
* [ ] MySQL: ≥150 filas insertadas repartidas en ≥3h y ≥2 device\_id.
* [ ] MySQL: 3 consultas pedidas + CSV de promedios por hora.
* [ ] MongoDB: colección con índice compuesto.
* [ ] MongoDB: ≥150 docs, ≥3h, ≥2 device\_id.
* [ ] MongoDB: 3 pipelines pedidas + JSON de promedios por hora.
* [ ] README (SQL y Mongo) explicando por qué el índice sirve.

---

## Extras (opcionales, si querés subir dificultad)

* **Ventanas móviles**: promedio móvil de 3 muestras por device/hora.
* **Detección de outliers**: descartar mediciones fuera de 3σ antes de promediar.
* **TTL en Mongo**: colección auxiliar con TTL para lecturas “crudas” y colección agregada por hora para histórico.

---
