import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius=radius

    def perimeter(self):
        return self.radius/2 * math.pi

    def area(self):
        return self.radius**2 *math.pi

    def definition(self):
        print('A circle is a plane figure bounded by one curved line, and such that all straight lines drawn from a certain point within it to the bounding line, are equal. The bounding line is called its circumference and the point, its centre.')