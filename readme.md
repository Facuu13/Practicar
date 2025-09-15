# 🔹 Plan semanal de práctica

Cada día un tema distinto para no aburrirte y repasar de todo:

## Día 1 – C / MicroPython (firmware embebido)
- **Mini-tarea**: Escribir un programa en C que encienda un LED con PWM y permita variar el duty cycle con un botón.
- **Variante**: Lo mismo en MicroPython para un ESP32-C3.
- **👉 Objetivo**: Reforzar manejo de GPIO, timers e interrupciones.

## Día 2 – Protocolos IoT
- **Mini-tarea**: Simular un cliente MQTT en Python que publique cada 5s datos de temperatura (random).
- **Variante**: Escuchar esos datos con `mosquitto_sub` y loguearlos en un archivo.
- **👉 Objetivo**: Mantener fresco el flujo sensor → gateway → broker → consumidor.

## Día 3 – Bases de datos
- **Mini-tarea**: 
  - Crear una tabla en PostgreSQL con lecturas de sensores (`id`, `timestamp`, `temp`, `hum`).
  - Insertar 10 valores con un script en Python.
  - Hacer una query que calcule promedio de temperatura por hora.
- **👉 Objetivo**: No perder práctica en SQL + conexión desde Python.

## Día 4 – Backend (Node.js o Python)
- **Mini-tarea**: Crear una API REST muy simple que devuelva las últimas 5 lecturas de sensor en JSON.
- **Extra**: Agregar un endpoint `/average` que calcule promedio en backend.
- **👉 Objetivo**: Practicar endpoints, JSON y lógica básica.

## Día 5 – Frontend (React o Angular)
- **Mini-tarea**: Una página que consuma tu API REST y muestre los datos en una tabla.
- **Extra**: Agregar un gráfico simple con Chart.js o Recharts.
- **👉 Objetivo**: Mantener la práctica en hooks/componentes/servicios.

## Día 6 – Linux / Bash
- **Mini-tarea**: Escribir un script en Bash que lea un archivo CSV con lecturas de sensor y muestre:
  - Cantidad de filas
  - Promedio de temperatura
  - Máximo y mínimo
- **👉 Objetivo**: No perder agilidad en scripting y pipes.

## Día 7 – Proyecto mini-integrado
- Levantar un ESP32 que simule lecturas → publicarlas por MQTT → guardarlas en PostgreSQL con un script en Python → consumirlas en una API Node.js → mostrarlas en un frontend React.
- **👉 No tiene que ser perfecto, solo conectar las piezas.**
- **Objetivo**: Repasar todo el stack IoT que usás en tus proyectos reales.