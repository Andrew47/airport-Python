from helper import *

from plane import Plane

class PlaneTestCase(unittest.TestCase):
    def setUp(self):
        self.plane = Plane()
        self.airport = MagicMock()

    def test_plane_default_airborne(self):
        self.assertTrue(self.plane.is_airborne)

    def test_not_stormy_land_means_airborne_false(self):
        self.plane.land(self.airport)
        self.assertFalse(self.plane.is_airborne)

    def test_not_stormy_land_returns_plane(self):
        self.assertEqual(self.plane.land(self.airport), self.plane)

    def test_not_stormy_land_calls_land_plane_on_airport(self):
        self.plane.land(self.airport)
        self.airport.land_plane.assert_called_with(self.plane)
