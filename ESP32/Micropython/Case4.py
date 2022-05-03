#Importa a biblioteca para definir a função do pino
from machine import Pin

#CONSTANTES PARA O PROGRAMA
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_LIGADO = 0
BOTAO_DESLIGADO = 1

#Define onde está o LED1
led1 = Pin(18, Pin.OUT, value = LED_DESLIGADO)
led2 = Pin(19, Pin.OUT, value = LED_DESLIGADO)
botao1 = Pin(16, Pin.IN, Pin.PULL_UP)
botao2 = Pin(17, Pin.IN, Pin.PULL_UP)

def avalia_entrada(entrada, saida):
    if entrada.value() == BOTAO_LIGADO:
        saida.value(LED_LIGADO)
    else:
        saida.value(LED_DESLIGADO)

while True:
    avalia_entrada(botao1, led1)
    avalia_entrada(botao2, led2)
