#Importa a biblioteca para definir a função do pino
from machine import Pin

#CONSTANTES PARA O PROGRAMA
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_LIGADO = 0
BOTAO_DESLIGADO = 1

#Define onde está o LED1
led1 = Pin(18, Pin.OUT, value = LED_DESLIGADO)
botao1 = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    if botao1.value() == BOTAO_LIGADO:
        led1.value(LED_LIGADO)
    else:
        led1.value(LED_DESLIGADO)
