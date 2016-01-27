from helper import *

from mock import patch

from plane import Plane

from weather import Weather

class PlaneTestCase(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()
        self.airport = MagicMock()
        self.weather = MagicMock()
        self.weather.is_stormy = MagicMock(return_value=False)

    def test_plane_default_airborne(self):
        self.assertTrue(self.plane.is_airborne)

    def test_not_stormy_land_means_airborne_False(self):
        self.plane.land(self.airport, self.weather)
        self.assertFalse(self.plane.is_airborne)

    def test_not_stormy_land_returns_plane(self):
        self.assertEqual(self.plane.land(self.airport, self.weather), self.plane)

    def test_not_stormy_land_calls_land_plane_on_airport(self):
        self.plane.land(self.airport, self.weather)
        self.airport.land_plane.assert_called_with(self.plane)

    def test_land_prevented_when_airborne_False(self):
        self.plane.land(self.airport, self.weather)
        with self.assertRaisesRegexp(Exception, 'Plane already landed'):
            self.plane.land(self.airport, self.weather)

    def test_not_stormy_take_off_means_airborne_True(self):
        self.plane.land(self.airport, self.weather)
        self.plane.take_off(self.airport, self.weather)
        self.assertTrue(self.plane.is_airborne)

    def test_not_stormy_take_off_calls_take_off_plane_on_airport(self):
        self.plane.land(self.airport, self.weather)
        self.plane.take_off(self.airport, self.weather)
        self.airport.take_off_plane.assert_called_with(self.plane)

    def test_not_stormy_take_off_returns_plane(self):
        self.plane.land(self.airport, self.weather)
        self.assertEqual(self.plane.take_off(self.airport, self.weather), self.plane)

    def test_take_off_prevented_when_airborne_True(self):
        with self.assertRaisesRegexp(Exception, 'Plane already airborne'):
            self.plane.take_off(self.airport, self.weather)

    def test_stormy_land_prevented(self):
        self.weather.is_stormy = MagicMock(return_value=True)
        with self.assertRaisesRegexp(Exception, 'Weather is stormy'):
            self.plane.land(self.airport, self.weather)

    def test_stormy_take_off_prevented(self):
        self.plane.land(self.airport, self.weather)
        self.weather.is_stormy = MagicMock(return_value=True)
        with self.assertRaisesRegexp(Exception, 'Weather is stormy'):
            self.plane.take_off(self.airport, self.weather)
