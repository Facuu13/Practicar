import machine
import time

contador = 0

# definir un pin como salida para el led
led = machine.Pin(2)

# definir un pin para el pwm
pwm = machine.PWM(led)
pwm.freq(1000)  # frecuencia de 1kHz
pwm.duty(0)  # iniciar con duty cycle en 0%

# definir un pin para el boton
boton = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# funcion de la interrucion
def callback(pin):
    global contador
    boton.irq(handler=None)  # deshabilita
    contador += 1
    if contador == 1:
        pwm.duty(256)
    elif contador == 2:
        pwm.duty(512)
    elif contador == 3:
        pwm.duty(768)
    elif contador == 4:
        pwm.duty(1023)
    elif contador == 5:
        pwm.duty(0)
        contador = 0
    time.sleep_ms(200)  # antirrebote
    boton.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)  # re-habilita

# definir interrucion para el boton
boton.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)







