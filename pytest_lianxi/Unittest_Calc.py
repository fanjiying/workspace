import unittest

from pytest_lianxi.Calc import Calc


class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        self.assertEqual(3, result)

    def test_div_1(self):
        self.calc = Calc()
        result = self.calc.div(1, 2)
        print(result)
        self.assertEquals()