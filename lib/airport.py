class Airport(object):

    def __init__(self, capacity=20,planes=[]):
        self._DEFAULTCAPACITY = capacity
        self.capacity = self._DEFAULTCAPACITY
        self.planes = planes

    def is_full(self) return True if len(self.planes) == self.capacity else return False
