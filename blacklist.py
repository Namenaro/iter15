from appliable import *

class SimpleBlacklist:
    def __init__(self):
        self.elements = []

    def _add(self,sens_field_rad, dx, dy):
        self.elements.append([dx, dy, sens_field_rad])

    def add(self, node):
        if isinstance(node, BinaryUnit):
            self._add(node.sensor_field_radius, node.dx, node.dy)

    def is_in(self, sens_field_rad, dx, dy):
        for element in self.elements:
            if element[0]==dx and element[1]==dy and element[2]==sens_field_rad:
                return True
        return False

