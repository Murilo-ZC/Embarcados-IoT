#Teste da biblitoeca do Micropython para utilizar o DHT11(Azul)
import dht
import machine
from time import sleep
SENSOR_PIN = 28
sensor = dht.DHT11(machine.Pin(SENSOR_PIN, machine.Pin.IN, machine.Pin.PULL_UP))

sensor.measure()
temperatura = sensor.temperature()
humidade = sensor.humidity()

print('Temperatura', temperatura)
print('Humidade', humidade)