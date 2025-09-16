# 📝 Día 3 – 

## 🎯 Objetivo

Guardar lecturas de sensores en **MySQL** y en **MongoDB**, insertar datos y hacer **una consulta básica** en cada uno.

---

## Parte A — MySQL

1. **Crear tabla** `readings` con:

   * `id` (autoincrement, PK)
   * `device_id` (texto)
   * `ts_utc` (fecha-hora UTC)
   * `temp_c` (número con decimales)
   * `hum_pct` (número con decimales)

2. **Insertar datos**: al menos 10 lecturas para `dev001` con diferentes timestamps.

3. **Consulta**: obtener las últimas 5 lecturas de `dev001`, ordenadas por `ts_utc` descendente.

👉 **Entregables Día 3 – SQL**

* Script `schema_mysql.sql` (CREATE TABLE).
* Script o pequeño código que inserte 10 lecturas.
* Consulta SELECT para las últimas 5 lecturas.

---

## Parte B — MongoDB

1. **Colección** `readings` con documentos como:

   ```json
   {
     "device_id": "dev001",
     "ts_utc": "2025-09-16T14:00:00Z",
     "temp_c": 23.4,
     "hum_pct": 56.7
   }
   ```

2. **Insertar datos**: al menos 10 documentos de `dev001` con diferentes timestamps.

3. **Consulta**: encontrar las últimas 5 lecturas de `dev001` (ordenadas por `ts_utc` descendente).

👉 **Entregables Día 3 – NoSQL**

* Script/código que inserte los documentos.
* Consulta/pipeline para devolver las últimas 5 lecturas.




