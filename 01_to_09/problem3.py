#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#

import math

# Seed prime list with
primes = [2]
def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    primes.append(n)
    return True

NUMBER = 600851475143
i = 3
while i < int(math.sqrt(NUMBER)):
    if is_prime(i) and NUMBER % i == 0:
        NUMBER /= i
    i += 2

print(NUMBER)
