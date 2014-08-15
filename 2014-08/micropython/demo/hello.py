""" Hello World on the pyboard.  Just turn on the blue LED """
import pyb

led_blue = pyb.LED(4)
led_blue.on()
