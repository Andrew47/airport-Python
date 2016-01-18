import unittest

import sys
sys.path.append('../lib')

from airport import Airport

class FeatureTestCase(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()
        self.airport = Airport()

    def test_planes_can_land(self):
        self.plane(self.airport)
        self.assertEqual(self.airport.planes(),[self.plane])



if __name__ == '__main__':
    unittest.main()
