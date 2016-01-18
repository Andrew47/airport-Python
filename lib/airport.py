class Airport:

    def __init__(self, capacity=20,planes=[]):
        self._DEFAULTCAPACITY = capacity
        self.capacity = self._DEFAULTCAPACITY
        self.planes = planes
