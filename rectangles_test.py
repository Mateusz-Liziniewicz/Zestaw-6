import unittest
from rectangles import (Rectangle)
from points import Point

class TestRectangle(unittest.TestCase):

    def test_str(self):
        rect = Rectangle(0, 0, 4, 3)
        self.assertEqual(str(rect), "[(0, 0), (4, 3)]")

    def test_repr(self):
        rect = Rectangle(0, 0, 4, 3)
        self.assertEqual(repr(rect), "Rectangle(0, 0, 4, 3)")

    def test_eq(self):
        rect1 = Rectangle(0, 0, 4, 3)
        rect2 = Rectangle(0, 0, 4, 3)
        rect3 = Rectangle(1, 1, 5, 4)
        self.assertTrue(rect1 == rect2)
        self.assertFalse(rect1 == rect3)

    def test_center(self):
        rect = Rectangle(0, 0, 4, 6)
        center = rect.center()
        self.assertEqual(center, Point(2, 3))

    def test_area(self):
        rect = Rectangle(0, 0, 4, 3)
        self.assertEqual(rect.area(), 12)

    def test_move(self):
        rect = Rectangle(0, 0, 4, 3)
        rect.move(2, 1)
        self.assertEqual(str(rect), "[(2, 1), (6, 4)]")
        rect.move(-2, -1)
        self.assertEqual(str(rect), "[(0, 0), (4, 3)]")
if __name__ == '__main__':
    unittest.main()