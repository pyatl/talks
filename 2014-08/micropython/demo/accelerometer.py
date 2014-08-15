""" Interact with the accelerometer. Light up different leds
when different axes are not level, within a tolerance. """
import pyb

ledx = pyb.LED(1)
ledy = pyb.LED(2)
ledz = pyb.LED(3)
accel = pyb.Accel()
SENSITIVITY = 5

def run():
    while True:
        x = accel.x()
        y = accel.y()
        z = accel.z()
        if abs(x) > SENSITIVITY:
            ledx.on()
        else:
            ledx.off()
        if abs(y) > SENSITIVITY:
            ledy.on()
        else:
            ledy.off()
        if abs(z) > SENSITIVITY:
            ledz.on()
        else:
            ledz.off()
        pyb.delay(200)

