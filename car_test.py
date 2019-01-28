import unittest
from car import Car

class TestGreet(unittest.TestCase):
    def test_basic(self):
        test_car = Car(20000)
        self.assertEqual(test_car.getTotalCost(), 20000)