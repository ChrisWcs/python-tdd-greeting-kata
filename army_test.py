import unittest
from unittest.mock import patch
from army import Army

class TestGreet(unittest.TestCase):

    @patch('soldier.Soldier.health')
    @patch('medic.Medic.health')
    def test_basic(self, mock_method, mock_method2):
        mock_method.return_value = 50
        mock_method2.return_value = 50

        a = Army(5, 5)
        self.assertEqual(a.health(), 100)