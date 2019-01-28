import unittest
from soldier import Soldier

class TestGreet(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(Soldier(10).health(), 100)