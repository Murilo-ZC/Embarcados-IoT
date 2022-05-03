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

def inverter_led(led):
    if led.value() == 1:
        led.value(0)
    else:
        led.value(1)

#Tira uma foto do estado do botão (ligado ou desligado)
foto_do_botao_1 = botao1.value()
while True:
    #Verifica se o botão mudou em relação a foto
    if botao1.value() != foto_do_botao_1:
        #Atualiza a foto
        foto_do_botao_1 = botao1.value()
        #verifica se o botão está ligado
        if foto_do_botao_1 == BOTAO_LIGADO:
            inverter_led(led1)
