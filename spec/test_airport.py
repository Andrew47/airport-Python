import unittest

import sys
sys.path.append('../lib')

from airport import Airport

class AirportTestCase(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()

    def test_planes_default_empty(self):
        self.assertEqual(self.airport.planes,[])

    def test_capacity_default(self):
        self.assertEqual(self.airport.capacity, self.airport._DEFAULTCAPACITY)

    def test_capacity_can_be_overriden(self):
        self.random_capacity = 100
        self.airport = Airport(self.random_capacity)
        self.assertEqual(self.airport.capacity, self.random_capacity)


if __name__ == '__main__':
  # suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
  # unittest.TextTestRunner(verbosity=2).run(suite)
  unittest.main()
