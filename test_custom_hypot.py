"""Main task is to test hypot() function from math module.
It should return length of hypotenuse
by using length of base and parendicular"""
import unittest
from main_function import custom_hypot


class TestCustomHypotenuse(unittest.TestCase):

    """Test Cases for the function with correct,
    incorrect and null parameters"""

    def test_parameters_are_incorrect(self):
        """Testing with all possible incorrect parameters"""
        with self.assertRaises(TypeError):
            custom_hypot(-3, 0)
        with self.assertRaises(TypeError):
            custom_hypot(0, -4)
        with self.assertRaises(TypeError):
            custom_hypot(-3, -4)
        with self.assertRaises(TypeError):
            custom_hypot(-3.90, 0)
        with self.assertRaises(TypeError):
            custom_hypot(-3.90, -8.9)
        with self.assertRaises(TypeError):
            custom_hypot("one", "two")
        with self.assertRaises(TypeError):
            custom_hypot("one", "")
        with self.assertRaises(TypeError):
            custom_hypot("one", "two")
        with self.assertRaises(TypeError):
            custom_hypot("", "two")
        with self.assertRaises(TypeError):
            custom_hypot(9, "zero")
        with self.assertRaises(TypeError):
            custom_hypot("one", 90)
        with self.assertRaises(TypeError):
            custom_hypot(1, [1, 2, 3, 4])
        with self.assertRaises(TypeError):
            custom_hypot([1, 2, 3, 4], 90)
        with self.assertRaises(TypeError):
            custom_hypot([1, 4, 8], [1, 2, 3, 4])
        with self.assertRaises(TypeError):
            custom_hypot(1, (1, 2, 2, 3))
        with self.assertRaises(TypeError):
            custom_hypot((1, 2, 2, 3), 8)
        with self.assertRaises(TypeError):
            custom_hypot((4, 5, 6), (1, 2, 2, 3))
        with self.assertRaises(TypeError):
            custom_hypot({2: 78}, {7: 98})
        with self.assertRaises(TypeError):
            custom_hypot(5, {7: 98})
        with self.assertRaises(TypeError):
            custom_hypot({2: 78}, 90)

    def test_parameters_are_null(self):
        """Testing with all possible correct parameters"""
        with self.assertRaises(TypeError):
            custom_hypot()
        with self.assertRaises(TypeError):
            custom_hypot({}, {})
        with self.assertRaises(TypeError):
            custom_hypot([], [])
        with self.assertRaises(TypeError):
            custom_hypot("", "")
        self.assertEqual(custom_hypot(0, 0), 0)

    def test_parameters_are_correct(self):
        """Testing with all possible correct parameters"""
        self.assertEqual(custom_hypot(3, 4), 5)
        self.assertEqual(custom_hypot(9, 12), 15)
        self.assertEqual(custom_hypot(3.0, 4.0), 5.0)
        self.assertNotEqual(custom_hypot(20, 30), 40)
        self.assertNotEqual(custom_hypot(3.89, 4.90), 25)


if __name__ == "__main__":
    unittest.main()
