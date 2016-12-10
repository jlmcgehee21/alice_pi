import unittest2 as unittest
import mock
from alice_pi import measurers
import random


class TestTemperatureMeasurer(unittest.TestCase):

    @mock.patch('alice_pi.measurers.W1ThermSensor')
    def test_measure(self, mock_get_temp):
        test_temp = 10 + random.random()

        mock_get_temp = mock_get_temp.return_value
        mock_get_temp.get_temperature = mock.MagicMock()
        mock_get_temp.get_temperature.return_value = test_temp

        meas = measurers.TemperatureMeasurer('F', n_decimals=2)

        temp = meas.measure()

        self.assertEquals(temp, round(test_temp, 2))


if __name__ == '__main__':
    unittest.main()
