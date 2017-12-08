# What is the largest n-digit pandigital prime that exists?
import math
from itertools import permutations

primes = [2]
def add_prime(n):
    for p in primes:
        if p**2 > n:
            break
        if n % p == 0:
            return False
    primes.append(n)
    return True

# Seed primes needed to check primes under max pandigital
[add_prime(n) for n in range(3, int(math.sqrt(987654321))+1, 2)]

# (1,2,3,4,5,6,7,8) => '12345678'
def join_perm(perm):
    return int(''.join([str(n) for n in perm]))

# Generate pandigitals from 3-9 digits and prime largest one that is prime
print max([join_perm(i) for j in range(3, 10) for i in permutations(range(1, j)) if add_prime(join_perm(i))])
