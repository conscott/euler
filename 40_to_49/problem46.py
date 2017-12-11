"""
It was proposed by Christian Goldbach that every odd composite number can be written as
the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice
a square?
"""

import math
from itertools import count

primes = [2]
def seed_primes(limit):
    def check_prime(n):
        for p in primes:
            if p**2 > n:
                break
            if n % p == 0:
                return False
        primes.append(n)
        return True
    [check_prime(n) for n in range(3, limit, 2)]

seed_primes(100000)

def is_perfect_square(n):
    nsqrt = math.sqrt(n)
    return nsqrt == math.trunc(nsqrt)

def verify_condition(n):
    if n in primes:
        return True
    for s in range(1, int(math.sqrt(n/2+1))+1):
        if (n-2*s*s) in primes:
            return True
    return False

for n in count(33, 2):
    if not verify_condition(n):
        print n
        break
