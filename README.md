# Recursion Practice

In this exercise you will write a few short recursive functions. The goal is to help you think recursively, and then design and test recursive algorithms.

## Your Task

Your task is to write the following Python functions in `recursion.py`:

### 1. Exponentiation

Implement `exponent(c, n)`, which should use recursion to calculate the exponentiation function, or <code>c<sup>n</sup></code>. For example, `exponent(10, 3)` should return 1000, since <code>10<sup>3</sup> = 1000</code>. Remember that <code>c<sup>n</sup> = c * c<sup>n-1</sup></code>.

### 2. Counting handshakes

Implement `handshakes(n)`, which should use recursion and return the number of handshakes needed in a room of `n` people such that every person shakes hands with every other person exactly once.

For example, in a room of three people X, Y, and Z, X shakes hands with Y and Z. Then, Y and Z shake hands. There are therefore three shakes total, and `handshakes(3) = 3`.

### 3. Checking divisors

Implement `is_divisible(n, d)`, which should use recursion and return a boolean (`True` or `False`) representing whether `n` is evenly divisible by `d`. For example, `is_divisible(10, 2)` should return `True`, but `is_divisible(10, 3)` should return `False`.

Hint: there are *two* base cases for this function: one case where you can be confident that `n` is not divisible by `d` (and can return `False`), and one where you can be confident that `n` *is* divisible by `d` (and can return `True`). To reach these base cases, it might help to repeatedly subtract factors of `d` from `n`.

You should implement this function *without* using the modulus operator (`%`).

### 4. Checking primes

Implement `is_prime(n)`, which should use recursion and return whether `n` is a prime number for all numbers `n > 2`. For example, `is_prime(7)` should return `True`, but `is_prime(12)` should return `False`.

Actually, `is_prime(n)` is already implemented for you; it simply invokes a recursive *helper* function, `is_prime(n, d)`, that checks whether `n` is divisible by any number starting from `d`. Therefore, `is_prime(n)` immediately calls `is_prime(n, 2)`, which should evaluate whether `n` is evenly divisible by any number starting from 2. It is up to you to implement `is_prime(n, d)`.

To do so, you may find it helpful to use the modulus operator (`%`), which returns the remainder of a division operation. For example, `10 % 3` will return 1, since `10 / 3 = 3` with 1 as a remainder.

After checking whether `n` is divisible by 2, you should check whether `n` is divisible by 3, so on and so forth until you can be sure that either `n` is either divisible by some `d` (and is therefore not prime), or `n` is not evenly divisible by any number (and is therefore prime).

Note that `is_prime(n, d)` is different than the function `is_divisible()` above, since `is_prime()` is checking whether `n` is divisible by *any* number `d` starting from 2.

## Consider Efficiency

For each of the above functions, think about how you would express the big-O running time. Some of these functions have multiple parameters, so consider whether you would include either parameter or both in your big-O expression.

## Test Cases

In `test_recursion.py`, add unit tests that test the functionality of your recursive functions. We added some initial tests for you, but you should add more to make sure all edge cases are tested.
