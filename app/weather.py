import random

class Weather(object):
    def _number_generator(self):
        return random.randrange(0,4)

    def _weather_generator(self):
        weather_possibilities = ['storm', 'no_storm', 'no_storm', 'no_storm']
        return weather_possibilities[self._number_generator()];

    def is_stormy(self):
        return self._weather_generator() == 'storm'
