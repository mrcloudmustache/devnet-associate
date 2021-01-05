import unittest
from cube import *

class TestCube(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(3),9)
    
    def test_string(self):
        response = cube("test")
        self.assertNotEqual(type(response),str)


if __name__ == '__main__':
    unittest.main()

