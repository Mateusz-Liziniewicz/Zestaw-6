from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def center(self):
        x_center = (self.pt1.x + self.pt2.x) / 2
        y_center = (self.pt1.y + self.pt2.y) / 2
        return Point(x_center, y_center)

    def area(self):
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
