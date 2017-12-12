# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.
# How many circular primes are there below one million?

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

# Seed primes under 1 million
[add_prime(n) for n in range(3, 1000000, 2)]

# Group primes by their number of digits to limit
# set of primes to check
prime_sets = {
    1: [p for p in primes if p < 10],
    2: [p for p in primes if p > 10 and p < 100],
    3: [p for p in primes if p > 100 and p < 1000],
    4: [p for p in primes if p > 1000 and p < 10000],
    5: [p for p in primes if p > 10000 and p < 100000],
    6: [p for p in primes if p > 100000 and p < 1000000]
}

# Permuations of rotation
# [1, 2, 3, 4] =>
#   [1, 2, 3, 4]
#   [2, 3, 4, 1]
#   [3, 4, 1, 2]
#   [4, 1, 2, 3]
def rotate(nums):
    for i in range(len(nums)):
        nums = nums[1:] + [nums[0]]
        yield nums

# Check if prime is circular
def circular_prime(p):
    num_digits = len(str(p))
    for num in rotate([int(char) for char in str(p)]):
        inum = int(''.join([str(i) for i in num]))
        if inum not in prime_sets[num_digits]:
            return False
    return True

print(sum([1 for p in primes if circular_prime(p)]))
