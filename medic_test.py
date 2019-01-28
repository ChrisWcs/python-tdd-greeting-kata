import unittest
from medic import Medic

class TestGreet(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(Medic(10).health(), 100)