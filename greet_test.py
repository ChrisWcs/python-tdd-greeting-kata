import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')