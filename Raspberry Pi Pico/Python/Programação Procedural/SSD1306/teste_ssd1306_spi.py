#Interface SPI
from machine import Pin, SPI  
from ssd1306 import SSD1306_SPI  

spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
#display = SSD1306_SPI(WIDTH, HEIGHT, spi, dc,rst, cs) use GPIO PIN NUMBERS
display = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16)) 

display.fill(0)
display.text( "IMT MAUA!!", 0, 0)
display.show()
