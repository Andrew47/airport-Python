import unittest
from airport import Airport

class AirportTestCase(unittest.TestCase):
    def test_planes_default_empty(self):
        self.airport = Airport()
        self.assertEqual(self.airport.planes,[])


if __name__ == '__main__':
  # suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
  # unittest.TextTestRunner(verbosity=2).run(suite)
  unittest.main()
