from machine import Pin
from time import sleep

def ligar(saida):
    saida.value(1)

def desligar(saida):
    saida.value(0)
    
PINO_LED = 2
TEMPO_DELAY = 1

pino_led = Pin(PINO_LED, Pin.OUT)

try:
    while True:
        ligar(pino_led)
        sleep(TEMPO_DELAY)
        desligar(pino_led)
        sleep(TEMPO_DELAY)
except KeyboardInterrupt:
    desligar(pino_led)

