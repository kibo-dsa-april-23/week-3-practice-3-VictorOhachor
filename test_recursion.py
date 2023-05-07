import unittest
from recursion import Recursion

class TestRecursion(unittest.TestCase):
    def test_exponent(self):
        r = Recursion()
        result = r.exponent(10, 3)
        assert result == 1000

    def test_handshakes(self):
        r = Recursion()
        result = r.handshakes(3)
        assert result == 3

    def test_is_divisible(self):
        r = Recursion()
        evenly_divides = r.is_divisible(10, 5)
        assert evenly_divides

    def test_is_prime(self):
        r = Recursion()
        is_prime_number = r.is_prime(7)
        assert not is_prime_number

    # add more unit tests below
