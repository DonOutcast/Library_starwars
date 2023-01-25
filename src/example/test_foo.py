import unittest
from main import my_sum


class T(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(my_sum(2, 3), 5, "should 5")


if __name__ == "__main__":
    unittest.main()
