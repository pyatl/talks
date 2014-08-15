""" Looping your program - Make the red LED blink on and off every 500 ms """
import pyb

led_red = pyb.LED(1)

def run():
    while True:
        led_red.toggle()
        pyb.delay(500)

