from helper import *
from plane import Plane
from airport import Airport

class FeatureTestCase(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()
        self.airport = Airport(20,[])
        self.weather = MagicMock()

    def test_planes_can_land(self):
        self.plane.land(self.airport, self.weather)
        self.assertEqual(self.airport.planes,[self.plane])

    def test_planes_can_take_off(self):
        self.plane.land(self.airport, self.weather)
        self.plane.take_off(self.airport)
        self.assertEqual(self.airport.planes, [])
