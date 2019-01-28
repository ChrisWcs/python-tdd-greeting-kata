import unittest
from unittest.mock import patch
from dummy import dummy

def magic():
    return 1

class TestDummy(unittest.TestCase):
    @patch('dummy.magical', side_effect=magic)
    def test_basic(self):
        self.assertEqual(dummy(), 3)

    