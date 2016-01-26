import unittest

from mock import MagicMock

import sys
sys.path.append('../lib')

from airport import Airport

class AirportTestCase(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = MagicMock()

    def test_planes_default_empty(self):
        self.assertEqual(self.airport.planes,[])

    def test_planes_can_be_overriden(self):
        self.airport = Airport(20, [self.plane])
        self.assertEqual(self.airport.planes,[self.plane])

    def test_capacity_default(self):
        self.assertEqual(self.airport.capacity, self.airport._DEFAULTCAPACITY)

    def test_capacity_can_be_overriden(self):
        self.random_capacity = 100
        self.airport = Airport(self.random_capacity)
        self.assertEqual(self.airport.capacity, self.random_capacity)

    def test_isFull_returns_true_when_airport_at_capacity(self):
        self.airport = Airport(1, [self.plane])
        self.assertTrue(self.airport.is_full())

    def test_isFull_returns_false_when_airport_not_full(self):
        self.assertFalse(self.airport.is_full())

    def test_land_plane_stores_plane_in_airport(self):
        self.airport.land_plane(self.plane)
        self.assertEqual(self.airport.planes, [self.plane])

if __name__ == '__main__':
    unittest.main()
