# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

from itertools import count
import math

def get_factors(tnum):
    factors = set([1, tnum])
    for factor in range(2, int(math.sqrt(tnum))):
        if tnum % factor == 0:
            factors.add(factor)
            factors.add(tnum/factor)
    return factors

triangle = 1
for i in count(2, 1):
    triangle += i
    factors = get_factors(triangle)
    if len(factors) > 500:
        print("%s has %s factors" % (triangle, len(factors)))
        break
