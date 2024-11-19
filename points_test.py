import unittest
from points import Point

class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(2, 3)), "(2, 3)")

    def test_repr(self):
        self.assertEqual(repr(Point(2, 3)), "Point(2, 3)")

    def test_eq(self):
        self.assertTrue(Point(2, 3) == Point(2, 3))
        self.assertFalse(Point(2, 3) == Point(3, 2))

    def test_add(self):
        self.assertEqual(Point(2, 3) + Point(1, 1), Point(3, 4))

    def test_sub(self):
        self.assertEqual(Point(2, 3) - Point(1, 1), Point(1, 2))

    def test_mul(self):
        self.assertEqual(Point(2, 3) * Point(1, 1), 5)  # 2*1 + 3*1

    def test_cross(self):
        self.assertEqual(Point(2, 3).cross(Point(1, 1)), -1)  # 2*1 - 3*1

    def test_length(self):
        self.assertAlmostEqual(Point(3, 4).length(), 5.0)  # sqrt(3^2 + 4^2)

    def test_hash(self):
        self.assertEqual(hash(Point(2, 3)), hash(Point(2, 3)))
        self.assertNotEqual(hash(Point(2, 3)), hash(Point(3, 2)))
if __name__ == '__main__':
    unittest.main()