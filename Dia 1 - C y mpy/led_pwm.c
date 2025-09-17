#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/ledc.h"
#include "driver/gpio.h"
#include "esp_timer.h"
#include "esp_log.h"

#define BUTTON              4
#define LEDC_GPIO           2

// LEDC
#define LEDC_CHANNEL        LEDC_CHANNEL_0
#define LEDC_MODE           LEDC_LOW_SPEED_MODE
#define LEDC_TIMER          LEDC_TIMER_0
#define LEDC_DUTY_RES       LEDC_TIMER_10_BIT   // 0..1023
#define LEDC_FREQUENCY      1000                // 1 kHz

// Debounce
#define DEBOUNCE_US         200000              // 200 ms

static const char *TAG = "PWM_BTN_SIMPLE";

// ISR: cambia duty en pasos (25% → 50% → 75% → 100% → 0%)
void IRAM_ATTR button_isr_handler(void *arg) {
    static uint64_t last_us = 0;
    static int idx = -1;                       // arranca en -1 para que el primer press vaya a 25%
    const int niveles[] = {256, 512, 768, 1023, 0};
    const int N = sizeof(niveles) / sizeof(niveles[0]);

    uint64_t now = esp_timer_get_time();
    if ((now - last_us) < DEBOUNCE_US) return; // anti-rebote básico
    last_us = now;

    idx = (idx + 1) % N;                       // siguiente nivel
    ledc_set_duty(LEDC_MODE, LEDC_CHANNEL, niveles[idx]);
    ledc_update_duty(LEDC_MODE, LEDC_CHANNEL);
}

// ==================== FUNCIÓN DE CONFIG ====================
static void pwm_button_init(void) {
    // PWM: timer
    ledc_timer_config_t tcfg = {
        .speed_mode       = LEDC_MODE,
        .duty_resolution  = LEDC_DUTY_RES,
        .timer_num        = LEDC_TIMER,
        .freq_hz          = LEDC_FREQUENCY,
        .clk_cfg          = LEDC_AUTO_CLK
    };
    ledc_timer_config(&tcfg);

    // PWM: canal
    ledc_channel_config_t ccfg = {
        .gpio_num   = LEDC_GPIO,
        .speed_mode = LEDC_MODE,
        .channel    = LEDC_CHANNEL,
        .timer_sel  = LEDC_TIMER,
        .duty       = 0,
        .hpoint     = 0
    };
    ledc_channel_config(&ccfg);

    // Botón
    gpio_config_t io_conf = {
        .intr_type    = GPIO_INTR_NEGEDGE,
        .mode         = GPIO_MODE_INPUT,
        .pin_bit_mask = (1ULL << BUTTON),
        .pull_up_en   = 1,
        .pull_down_en = 0
    };
    gpio_config(&io_conf);

    // ISR
    gpio_install_isr_service(ESP_INTR_FLAG_IRAM);
    gpio_isr_handler_add(BUTTON, button_isr_handler, NULL);

    ESP_LOGI(TAG, "PWM en GPIO %d, botón en GPIO %d", LEDC_GPIO, BUTTON);
}

// ==================== MAIN ====================
void app_main(void) {
    pwm_button_init();   

    while (1) {
        vTaskDelay(pdMS_TO_TICKS(1000));  // loop vacío
    }
}
