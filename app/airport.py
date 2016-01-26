class Airport(object):

    def __init__(self, capacity=20, planes=[]):
        self._DEFAULTCAPACITY = capacity
        self.capacity = self._DEFAULTCAPACITY
        self.planes = planes

    def is_full(self):
        return True if len(self.planes) == self.capacity else False

    def land_plane(self, plane):
        if self.is_full() == True:
            raise Exception('Airport is Full')
        else:
            self.planes.append(plane)

    def take_off_plane(self, plane):
        self.planes.remove(plane)
