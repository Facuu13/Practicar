# 📝 Día 1 – Ejercicio: LED con PWM y control por botón

## Objetivo
Encender un LED controlado por PWM y variar su brillo con un botón. Cada vez que se presione el botón, el duty cycle debe cambiar de nivel (ejemplo: 0% → 25% → 50% → 75% → 100% → 0%).

## Requisitos
- Usar un **ESP32-C3** (vale tanto en **ESP-IDF (C)** como en **MicroPython**).
- Configurar un **GPIO** como salida PWM para el LED.
- Configurar un **GPIO** como entrada para el botón (con pull-up interno).
- Manejar el botón con **interrupción** (no con `while true` preguntando el estado).
- Guardar el estado actual del **duty cycle** en una variable global para ir cambiando cada vez que se presiona el botón.

## Ejemplo esperado (lógica de niveles)
1. Primera presión: LED apagado → 25% brillo.
2. Segunda presión: 25% → 50%.
3. Tercera presión: 50% → 75%.
4. Cuarta presión: 75% → 100%.
5. Quinta presión: vuelve a 0% (apagado).

## 👉 Entregable
Un código que cumpla estos pasos. Puede ser en **C con ESP-IDF** o en **MicroPython** (el que prefieras para arrancar).