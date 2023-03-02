import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_multiply(self):
        assert self.calculator.multiply(self, 2, 2) == 4

    def test_substration(self):
        assert self.calculator.substration(self, 5, 3) == 2

    def test_division(self):
        assert self.calculator.division(self, 6, 2) == 3
