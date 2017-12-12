"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""
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

seed_primes(1000000)

factor_cache = {}
def prime_factors(n):
    if n in factor_cache:
        return factor_cache[n]
    pfactors = set()
    for factor in primes:
        if factor > n/2:
            break
        if n % factor == 0:
            pfactors.add(factor)
    factor_cache[n] = pfactors
    return pfactors

consective_limit = 4
for i in count(15, 1):
    factorsets = []
    success = True
    for j in range(consective_limit):
        pf = prime_factors(i+j)
        if len(pf) < consective_limit or pf in factorsets:
            success = False
            break
        factorsets.append(pf)
    if success:
        print(i)
        break
