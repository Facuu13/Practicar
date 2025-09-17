# FreeRTOS
---

## 1. **Tareas (Tasks)**

En FreeRTOS todo gira alrededor de las **tareas**, que son como funciones que corren "en paralelo" (en realidad el kernel las intercambia muy rápido usando multitarea *cooperativa o preventiva*).

* Cada tarea tiene su **propia pila** y un **estado** (listo, corriendo, bloqueado, suspendido).
* Se crean con `xTaskCreate()`.
* Se ejecutan en bucle infinito (típicamente `for(;;)` o `while(1)`).
* El planificador decide cuál corre según **prioridad**.

👉 **Idea clave**: en lugar de un `while(1)` gigante con `if/else` para todo, FreeRTOS divide el programa en tareas independientes y el sistema las va alternando.

---

### Ejemplo sencillo

Este ejemplo crea dos tareas que prenden y apagan LEDs a distintas velocidades:

```c
#include "FreeRTOS.h"
#include "task.h"
#include "driver/gpio.h"

#define LED1 GPIO_NUM_2
#define LED2 GPIO_NUM_4

void tareaLed1(void *pvParameters) {
    for(;;) {
        gpio_set_level(LED1, 1);
        vTaskDelay(pdMS_TO_TICKS(500));  // Espera 500 ms
        gpio_set_level(LED1, 0);
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void tareaLed2(void *pvParameters) {
    for(;;) {
        gpio_set_level(LED2, 1);
        vTaskDelay(pdMS_TO_TICKS(200));  // Espera 200 ms
        gpio_set_level(LED2, 0);
        vTaskDelay(pdMS_TO_TICKS(200));
    }
}

void app_main() {
    gpio_reset_pin(LED1);
    gpio_set_direction(LED1, GPIO_MODE_OUTPUT);

    gpio_reset_pin(LED2);
    gpio_set_direction(LED2, GPIO_MODE_OUTPUT);

    xTaskCreate(tareaLed1, "Tarea LED1", 2048, NULL, 1, NULL);
    xTaskCreate(tareaLed2, "Tarea LED2", 2048, NULL, 1, NULL);
}
```

🔎 **Explicación**:

* Se crean **dos tareas**, cada una tiene su propio bucle infinito.
* `vTaskDelay()` cede el control al planificador y deja que otra tarea use la CPU.
* El sistema alterna entre tareas automáticamente → parece que corren en paralelo.

---

## 2. **Colas (Queues)**

Las **colas** en FreeRTOS sirven para que las tareas se **comuniquen entre sí** (o con interrupciones) pasando mensajes de manera **segura y sincronizada**.

* Son estructuras FIFO (First In – First Out).
* Una tarea puede **enviar datos** con `xQueueSend()` o `xQueueSendFromISR()` (si es desde una interrupción).
* Otra tarea puede **recibir datos** con `xQueueReceive()`.
* Si la cola está vacía y alguien hace `xQueueReceive()`, la tarea queda **bloqueada** hasta que llegue un dato (o hasta un timeout).

👉 **Idea clave**: te evitan usar variables globales con `volatile` y problemas de concurrencia.

---

### Ejemplo sencillo

Un ejemplo clásico: una tarea produce números y otra los consume.

```c
#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "driver/gpio.h"

QueueHandle_t cola;  // Cola global

void productor(void *pvParameters) {
    int valor = 0;
    for(;;) {
        valor++;
        xQueueSend(cola, &valor, portMAX_DELAY);  // Enviar número a la cola
        vTaskDelay(pdMS_TO_TICKS(1000));          // Cada 1 segundo
    }
}

void consumidor(void *pvParameters) {
    int recibido;
    for(;;) {
        if(xQueueReceive(cola, &recibido, portMAX_DELAY)) {
            printf("Recibido: %d\n", recibido);   // Procesa el dato
        }
    }
}

void app_main() {
    cola = xQueueCreate(5, sizeof(int));  // Cola de 5 enteros

    xTaskCreate(productor, "Productor", 2048, NULL, 1, NULL);
    xTaskCreate(consumidor, "Consumidor", 2048, NULL, 1, NULL);
}
```

🔎 **Explicación**:

* La cola puede almacenar hasta 5 enteros.
* El **productor** envía un número nuevo cada segundo.
* El **consumidor** queda esperando (`xQueueReceive`) hasta que llegue un dato y lo imprime.

Así lográs que las tareas trabajen de forma independiente pero coordinada.

---

## 3. **Semáforos**

En FreeRTOS, los **semáforos** se usan principalmente para dos cosas:

1. **Sincronización** → por ejemplo, que una tarea espere a que ocurra un evento (una interrupción, un pulso, etc.).
2. **Exclusión mutua** → evitar que dos tareas usen al mismo tiempo un recurso compartido (como un puerto serie o una variable global).

👉 Hay distintos tipos:

* **Semáforo binario** → solo tiene dos estados: tomado o libre (como una “llave”).
* **Semáforo contador** → lleva la cuenta de varios recursos disponibles.
* **Mutex** → parecido al semáforo binario, pero pensado específicamente para proteger recursos (lo vemos después).

---

### Ejemplo sencillo con semáforo binario

Una tarea espera a que ocurra un evento (por ejemplo, que una ISR lo libere).

```c
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include "driver/gpio.h"

#define BOTON GPIO_NUM_0

SemaphoreHandle_t semaforo;

void IRAM_ATTR boton_isr_handler(void* arg) {
    xSemaphoreGiveFromISR(semaforo, NULL);  // Libera el semáforo desde la ISR
}

void tareaEvento(void *pvParameters) {
    for(;;) {
        if (xSemaphoreTake(semaforo, portMAX_DELAY)) {
            printf("¡Botón presionado!\n");
        }
    }
}

void app_main() {
    // Configurar botón como entrada con interrupción
    gpio_reset_pin(BOTON);
    gpio_set_direction(BOTON, GPIO_MODE_INPUT);
    gpio_set_intr_type(BOTON, GPIO_INTR_NEGEDGE);  // Flanco descendente
    gpio_install_isr_service(0);
    gpio_isr_handler_add(BOTON, boton_isr_handler, NULL);

    // Crear semáforo binario
    semaforo = xSemaphoreCreateBinary();

    // Crear tarea que espera el evento
    xTaskCreate(tareaEvento, "TareaEvento", 2048, NULL, 1, NULL);
}
```

🔎 **Explicación**:

* El **ISR del botón** libera el semáforo (`xSemaphoreGiveFromISR`).
* La tarea se queda bloqueada en `xSemaphoreTake()`.
* Cuando alguien aprieta el botón, la tarea se desbloquea y ejecuta su acción.

---

## 4. **Mutex (Mutual Exclusion)**

Un **mutex** es muy parecido a un semáforo binario, pero está diseñado específicamente para **proteger recursos compartidos**.

👉 Diferencias con semáforo binario:

* El mutex tiene el concepto de **“propietario”**: solo la tarea que lo toma (`xSemaphoreTake`) puede liberarlo (`xSemaphoreGive`).
* Implementa **herencia de prioridad** → si una tarea de baja prioridad tiene el mutex y una tarea de alta prioridad lo necesita, la de baja prioridad hereda temporalmente la prioridad alta para evitar problemas de *inversión de prioridad*.
* Se usan siempre para cosas como **UART, I2C, SPI, memoria compartida, printf**, etc.

---

### Ejemplo sencillo con Mutex

Dos tareas intentan imprimir por consola, pero queremos que no se mezclen los mensajes.

```c
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>

SemaphoreHandle_t mutex;

void tareaA(void *pvParameters) {
    for(;;) {
        if(xSemaphoreTake(mutex, portMAX_DELAY)) {
            printf("Tarea A escribiendo...\n");
            vTaskDelay(pdMS_TO_TICKS(500));  // Simula trabajo
            printf("Tarea A terminó.\n");
            xSemaphoreGive(mutex);
        }
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

void tareaB(void *pvParameters) {
    for(;;) {
        if(xSemaphoreTake(mutex, portMAX_DELAY)) {
            printf("Tarea B escribiendo...\n");
            vTaskDelay(pdMS_TO_TICKS(500));  // Simula trabajo
            printf("Tarea B terminó.\n");
            xSemaphoreGive(mutex);
        }
        vTaskDelay(pdMS_TO_TICKS(800));
    }
}

void app_main() {
    mutex = xSemaphoreCreateMutex();

    xTaskCreate(tareaA, "TareaA", 2048, NULL, 1, NULL);
    xTaskCreate(tareaB, "TareaB", 2048, NULL, 1, NULL);
}
```

🔎 **Explicación**:

* Ambas tareas intentan imprimir mensajes.
* Si no usamos mutex, los `printf` se pueden intercalar (caos en consola).
* Con mutex, solo una tarea a la vez puede usar el recurso compartido.

---

## 5. **Timers de Software**

Los **timers de software** en FreeRTOS son objetos que ejecutan una función callback **después de un tiempo definido** o de manera **periódica**.

👉 Características:

* Se crean con `xTimerCreate()`.
* Se inician con `xTimerStart()`.
* Pueden ser de **una sola vez** o **periódicos**.
* No necesitan una tarea dedicada con `vTaskDelay()`, el kernel los maneja internamente.

Sirven para:

* Ejecutar acciones periódicas (ej: leer sensores cada 1s).
* Generar “timeouts” (ej: si no llegó un dato en 5s, disparar evento).

---

### Ejemplo sencillo con Timer

Un timer que prende y apaga un LED cada 1 segundo.

```c
#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include "driver/gpio.h"

#define LED GPIO_NUM_2

TimerHandle_t timer;

void callbackTimer(TimerHandle_t xTimer) {
    static int estado = 0;
    estado = !estado;
    gpio_set_level(LED, estado);
    printf("LED %s\n", estado ? "ON" : "OFF");
}

void app_main() {
    gpio_reset_pin(LED);
    gpio_set_direction(LED, GPIO_MODE_OUTPUT);

    // Crear timer: período 1000 ms, periódico (pdTRUE)
    timer = xTimerCreate("TimerLED", pdMS_TO_TICKS(1000), pdTRUE, NULL, callbackTimer);

    if (timer != NULL) {
        xTimerStart(timer, 0);  // Arranca el timer
    }
}
```

🔎 **Explicación**:

* El **timer** se dispara cada 1 segundo.
* Llama a la función `callbackTimer()`.
* Alterna el estado del LED y escribe en consola.
* Todo esto sin crear una tarea extra → más eficiente.

---

## 6. **Notificaciones de Tarea (Task Notifications)**

Las **notificaciones de tarea** son la forma más **ligera y rápida** de comunicación en FreeRTOS.

* Cada tarea tiene un “contador de notificación” interno.
* Una tarea puede esperar a una notificación con `ulTaskNotifyTake()` o `xTaskNotifyWait()`.
* Otra tarea (o una ISR) puede enviarla con `xTaskNotifyGive()` o `xTaskNotifyFromISR()`.
* Se usan como alternativa **más eficiente** a semáforos o colas cuando solo querés **señalar un evento** o **pasar un valor simple**.

👉 Ventaja: menos consumo de RAM y CPU que colas/semáforos.

---

### Ejemplo sencillo

Una ISR de botón notifica a una tarea para que prenda un LED.

```c
#include "FreeRTOS.h"
#include "task.h"
#include "driver/gpio.h"

#define BOTON GPIO_NUM_0
#define LED   GPIO_NUM_2

TaskHandle_t tareaHandle = NULL;

void IRAM_ATTR boton_isr_handler(void* arg) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    vTaskNotifyGiveFromISR(tareaHandle, &xHigherPriorityTaskWoken);
    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}

void tareaLed(void *pvParameters) {
    for(;;) {
        // Espera notificación (bloqueado hasta que ISR avise)
        ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
        gpio_set_level(LED, 1);
        vTaskDelay(pdMS_TO_TICKS(200));
        gpio_set_level(LED, 0);
    }
}

void app_main() {
    gpio_reset_pin(LED);
    gpio_set_direction(LED, GPIO_MODE_OUTPUT);

    gpio_reset_pin(BOTON);
    gpio_set_direction(BOTON, GPIO_MODE_INPUT);
    gpio_set_intr_type(BOTON, GPIO_INTR_NEGEDGE);
    gpio_install_isr_service(0);
    
    xTaskCreate(tareaLed, "TareaLed", 2048, NULL, 1, &tareaHandle);

    gpio_isr_handler_add(BOTON, boton_isr_handler, NULL);
}
```

🔎 **Explicación**:

* La **ISR del botón** avisa con `vTaskNotifyGiveFromISR`.
* La tarea queda esperando (`ulTaskNotifyTake`) hasta que llega la notificación.
* Al recibirla, prende el LED 200 ms y vuelve a esperar.

---