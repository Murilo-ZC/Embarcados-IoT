from machine import Pin
from time import sleep

def ligar(saida):
    saida.value(1)

def desligar(saida):
    saida.value(0)

def inverter(saida):
    if saida.value() == 1:
        desligar(saida)
    else:
        ligar(saida)
    
PINO_LED1 = 2
PINO_LED2 = 5
TEMPO_DELAY = 0.5
pino_led1 = Pin(PINO_LED1, Pin.OUT)
pino_led2 = Pin(PINO_LED2, Pin.OUT)
contador_led1 = 1
contador_led2 = 2

try:
    while True:
        sleep(TEMPO_DELAY)
        contador_led1 -= 1
        contador_led2 -= 1
        if(contador_led1 == 0):
            contador_led1 = 1
            inverter(pino_led1)
        if(contador_led2 == 0):
            contador_led2 = 2
            inverter(pino_led2)
except KeyboardInterrupt:
    desligar(pino_led1)
    desligar(pino_led2)

