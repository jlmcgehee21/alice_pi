"""
A Measurer's responsibility is to interact with the sensor
hardware and take a measurement, then return that measurement
"""
from w1thermsensor import W1ThermSensor

class TemperatureMeasurer(object):
    unit_dict = {'F': W1ThermSensor.DEGREES_F,
                 'C': W1ThermSensor.DEGREES_C}

    def __init__(self, unit='F', n_decimals=2):
        self.unit = self.unit_dict[unit]
        self.n_decimals = n_decimals

    def measure(self):
        sensor = W1ThermSensor()
        temp = sensor.get_temperature(self.unit)

        return round(temp, self.n_decimals)

class MotionMeasurer(object):
    pass
