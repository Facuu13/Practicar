//Queremos simular un LED conectado al pin GPIO5 de un microcontrolador. El LED debe seguir este patrón:
//Parpadea 3 veces rápido (100 ms encendido, 100 ms apagado).
//Luego parpadea 1 vez lento (500 ms encendido, 500 ms apagado).
//Repite este ciclo para siempre.
//Usá for para los 3 parpadeos rápidos y estructuras claras.
//Simulá el delay con una función (delay_ms(int tiempo)).

#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED_GPIO           5

void config_led(void) {
    gpio_pad_select_gpio(LED_GPIO);
    gpio_set_direction(LED_GPIO, GPIO_MODE_OUTPUT);
}

void delay_ms(int tiempo) {
    vTaskDelay(tiempo / portTICK_PERIOD_MS);
}

void app_main(void){
    config_led();
    while(1){
        for(int i = 0; i < 3; i++){
            gpio_set_level(LED_GPIO, 1); // Encender LED
            delay_ms(100);               // Esperar 100 ms
            gpio_set_level(LED_GPIO, 0); // Apagar LED
            delay_ms(100);               // Esperar 100 ms
        }
        gpio_set_level(LED_GPIO, 1);     // Encender LED
        delay_ms(500);                   // Esperar 500 ms
        gpio_set_level(LED_GPIO, 0);     // Apagar LED
        delay_ms(500);                   // Esperar 500 ms
    }


}