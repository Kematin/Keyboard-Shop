from django.test import TestCase


class Arichmetic:
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return b - a


class TestsArithmetic(TestCase):
    Ar = Arichmetic()

    def test_add(self) -> None:
        assert self.Ar.add(1, 1) == 2

    def test_subtract(self) -> None:
        assert self.Ar.subtract(2, 5) == 3
