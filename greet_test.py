import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(greet('Bob'), "Hello, Bob.")
    def test_basic_2(self):
        self.assertEqual(greet(None), "Hello, my friend.")