#Uso do display SSD1306 - interface I2C
from machine import Pin, I2C, SoftI2C
import ssd1306

#Pega o I2C do canal 1 - Pinos GPIO6 e GPIO7
i2c = I2C(1,sda=Pin(6),scl= Pin(7),freq= 400000)
#i2c = SoftI2C(sda=Pin(6),scl= Pin(7),freq= 400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.text( "Sergiao Roludo!!", 0, 0)
display.show()