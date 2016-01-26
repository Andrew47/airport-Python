from helper import *

from plane import Plane

class PlaneTestCase(unittest.TestCase):
    def setUp(self):
        plane = Plane ()
        airport = MagicMock ()
