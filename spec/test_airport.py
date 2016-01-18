import unittest

import sys
sys.path.append('../lib')

from airport import Airport

class AirportTestCase(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()

    def test_planes_default_empty(self):
        self.assertEqual(self.airport.planes(),[])

    def test_capacity_default(self):
        self.assertEqual(self.airport.capacity, self.airport._DEFAULTCAPACITY)


if __name__ == '__main__':
  # suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
  # unittest.TextTestRunner(verbosity=2).run(suite)
  unittest.main()
