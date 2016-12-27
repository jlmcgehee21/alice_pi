"""
A Measurer's responsibility is to interact with the sensor
hardware and take a measurement, then return that measurement
"""
import os
import sys
import inspect
from w1thermsensor import W1ThermSensor


if os.environ.get('PLATFORM', 'dev') == 'prod':
    import RPi.GPIO as GPIO


class Measurer(object):
    pass


class TemperatureMeasurer(Measurer):
    unit_dict = {'F': W1ThermSensor.DEGREES_F,
                 'C': W1ThermSensor.DEGREES_C}

    def __init__(self, unit='F', n_decimals=2):
        self.unit = self.unit_dict[unit]
        self.n_decimals = n_decimals

    def measure(self):
        sensor = W1ThermSensor()
        temp = sensor.get_temperature(self.unit)

        return round(temp, self.n_decimals)


class MotionMeasurer(Measurer):
    def measure():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN)  # Read output from PIR motion sensor

        return bool(GPIO.input(11))

classes = inspect.getmembers(sys.modules[__name__],
                             inspect.isclass)

MEASURERS = dict([tuple(item) for item in classes
                  if item[1].__module__ == __name__])

