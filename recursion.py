class Recursion:

    def exponent(self, c, n):
        if n == 0:
            return 1
        return c * self.exponent(c, n-1)

    def handshakes(self, n):
        if n <= 1:
            return 1

        return 1 + self.handshakes(n-1)

    def is_divisible(self, n, d):
        if n == 0:
            return True
        elif n < 0:
            return False
        
        return self.is_divisible(n - d, d)

    def is_prime_helper(self, n, d):
        if n == d:
            return True
        elif not n % d:
            return False
        
        return self.is_prime_helper(n, d + 1)

    def is_prime(self, n):
        return self.is_prime_helper(n, 2)


if __name__ == '__main__':
    r = Recursion()
    print(r.exponent(10, 3))
    print(r.handshakes(3))
    print(r.is_divisible(10, 3))
    print(r.is_divisible(10, 2))
    print(r.is_prime(7))
    print(r.is_prime(10))
