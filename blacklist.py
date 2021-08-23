from appliable import *

class SimpleBlacklist:
    def __init__(self):
        self.elements = []

    def _add(self,sens_field_rad, dx, dy):
        self.elements.append([dx, dy, sens_field_rad])

    def add(self, node):
        if isinstance(node, BinaryUnit) or isinstance(node, NonBinaryUnit):
            self._add(node.sensor_field_radius+node.u_radius, node.dx, node.dy)


    def is_in(self, node):
        for element in self.elements:
            if element[0] == node.dx and \
                    element[1] == node.dy and element[2]==node.sens_field_rad + node.u_radius:
                return True
        return False

