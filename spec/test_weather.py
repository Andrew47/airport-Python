from helper import *

from weather import Weather

class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_is_stormy_can_be_True(self):
        self.weather._number_generator = MagicMock(return_value=0)
        self.assertTrue(self.weather.is_stormy())

    def test_is_stormy_can_be_False(self):
        self.weather._number_generator = MagicMock(return_value=3)
        self.assertFalse(self.weather.is_stormy())
