import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(greet('Kirk'), "Hello, Kirk.")
    def test_null(self):
        self.assertEqual(greet(None), "Hello, my friend.")
    def test_shout(self):
        self.assertEqual(greet("KHAN"), "HELLO KHAN!")
    def test_many(self):
        self.assertEqual(greet(["Spock", "Bones"]), "Hello, Spock and Bones.")
    def test_lots(self):
        self.assertEqual(greet(["Spock", "Bones", "Scotty"]), "Hello, Spock, Bones, and Scotty.")
    