""" Make your pyboard into a disco! Alternate leds in a cycle """
import pyb

led_list = [pyb.LED(i) for i in range(1, 5)]

def run():
    i = 0
    while True:
        led_list[i].off()
        i += 1
        if i >= len(led_list):
            i = 0
        led_list[i].on()
        pyb.delay(200)

