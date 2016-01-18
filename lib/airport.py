class Airport:

    def __init__(self, capacity=20):
        self._DEFAULTCAPACITY = capacity
        self.capacity = self._DEFAULTCAPACITY
        self.planes = []
