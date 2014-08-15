""" Use the USR switch on the pyboard to toggle the blue led on and off """
import pyb

led = pyb.LED(4)

def run():
    switch = pyb.Switch()
    switch.callback(lambda: led.toggle())
