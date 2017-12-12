"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by
3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each
of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

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
    [check_prime(n) for n in range(3, limit+1, 2)]

seed_primes(10000)

primes_to_check = [p for p in primes if p > 1000 and p < 10000]

def is_perm(n1, n2):
    return set([s for s in str(n1)]) == set([s for s in str(n2)])

for p in primes_to_check:
    perm_set = [r for r in primes_to_check if p < r < 10000 and is_perm(p, r)]
    for pdiff in perm_set:
        if pdiff + (pdiff - p) in perm_set:
            print("%s%s%s" % (p, pdiff, pdiff + (pdiff - p)))
