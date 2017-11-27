# Evaluate the sum of all the amicable numbers under 10000.
import math


def proper_divisors(tnum):
    factors = set([1])
    for factor in range(2, int(math.sqrt(tnum))):
        if tnum % factor == 0:
            factors.add(factor)
            factors.add(tnum/factor)
    return factors


def sum_divisors(tnum):
    return sum(proper_divisors(tnum))

amicable = {}
for i in range(2, 10000):
    s1 = sum_divisors(i)
    s2 = sum_divisors(s1)
    if i == s2 and i != s1 and s1 not in amicable:
        amicable[i] = s1

print sum([i+k for i, k in amicable.items()])
