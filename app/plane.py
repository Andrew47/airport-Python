from weather import Weather

class Plane(object):

    def __init__(self, is_airborne=True):
        self.is_airborne = is_airborne

    def land(self, airport, weather=Weather()):
        if self.is_airborne == False:
            raise Exception('Plane already landed')
        self._weather_check(weather)
        self.is_airborne = False
        airport.land_plane(self)
        return self

    def take_off(self, airport):
        if self.is_airborne == True:
            raise Exception('Plane already airborne')
        self.is_airborne = True
        airport.take_off_plane(self)
        return self

    def _weather_check(self, weather):
        if weather.is_stormy() == True:
            raise Exception('Weather is stormy')
