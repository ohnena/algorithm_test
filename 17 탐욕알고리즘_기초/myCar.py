import unittest

# myCalc.py
def add(a, b):
    return a + b


def substract(a, b):
    return a - b

class TestCal(unittest.TestCase):
    def test_add(self):
        result = add(3,4)
        self.assertTrue(result==6)