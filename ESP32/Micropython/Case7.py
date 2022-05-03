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


#Tira uma foto do estado do botão (ligado ou desligado)
foto_do_botao_1 = botao1.value()
foto_do_botao_2 = botao2.value()
#Conta a quantidade de vezes que o botão foi acionado
contagem_de_pulsos = 0
while True:
    #Verifica se o botão mudou em relação a foto
    if botao1.value() != foto_do_botao_1:
        #Atualiza a foto
        foto_do_botao_1 = botao1.value()
        #verifica se o botão está ligado
        if foto_do_botao_1 == BOTAO_LIGADO:
            contagem_de_pulsos = contagem_de_pulsos + 1
    #Verifica se o botão mudou em relação a foto
    if botao2.value() != foto_do_botao_2:
        #Atualiza a foto
        foto_do_botao_2 = botao2.value()
        #verifica se o botão está ligado
        if foto_do_botao_2 == BOTAO_LIGADO:
            contagem_de_pulsos = 0
    #Verifica o estado da contagem
    if contagem_de_pulsos == 0:
        led1.value(LED_DESLIGADO)
        led2.value(LED_DESLIGADO)
    elif contagem_de_pulsos == 1:
        led1.value(LED_LIGADO)
    elif contagem_de_pulsos == 2:
        led2.value(LED_LIGADO)
    else:
        contagem_de_pulsos = 0
