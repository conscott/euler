# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.
import math
from itertools import combinations_with_replacement

def proper_divisors(tnum):
    factors = set([1])
    for factor in range(2, int(math.sqrt(tnum)) + 1):
        if tnum % factor == 0:
            factors.add(factor)
            factors.add(tnum/factor)
    return factors


def sum_divisors(tnum):
    return sum(proper_divisors(tnum))

# Abundant numbers are > sum of proper divisors
abundant_numbers = [i for i in range(12, 28123, 1) if sum_divisors(i) > i]

# Remove all abundant number pairs from list
possible_integers = set(range(1, 28124))
for abundant_pair in combinations_with_replacement(abundant_numbers, 2):
    try:
        possible_integers.remove(abundant_pair[0] + abundant_pair[1])
    except:
        pass

print sum(possible_integers)
