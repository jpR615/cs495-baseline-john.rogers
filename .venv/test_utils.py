import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_lowercaseString(self):
        self.assertEqual(utils.normalize("CarrOt"), "carrot")

    def test_dashString(self):
        self.assertEqual(utils.normalize("young sheldon"), "young-sheldon")

    def test_lowerCaseString_and_dashString(self):
        self.assertEqual(utils.normalize("Apples and Bananas"), "apples-and-bananas")

if __name__ == '__main__':
    unittest.main()