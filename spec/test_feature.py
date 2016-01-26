import unittest

import sys
sys.path.append('../lib')

class FeatureTestCase(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()
        self.airport = Airport()

    def test_planes_can_land(self):
        self.plane(self.airport)
        self.assertEqual(self.airport.planes,[self.plane])

    def test_planes_can_take_off(self):
        self.plane(self.airport)
        self.plane.take_off()
        self.assertEqual(self.airport.planes, [])



if __name__ == '__main__':
    unittest.main()
