"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine
possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is
the first example having seven primes among the ten generated numbers, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the
first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent
digits) with the same digit, is part of an eight prime value family.
"""
from collections import Counter

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

seed_primes(1000000)

# Need to find a prime that has at least 3
# of the same digits ignoring the last digit
max_occur_map = {}
def digit_check(p):
    occur = Counter([int(s) for s in str(p)[:-1]])
    for i, count in occur.items():
        if count >= 3:
            max_occur_map[p] = i
            return True
    return False

p_possible = set(p for p in primes if p > 100000 and p < 1000000 and digit_check(p))
p_possible_small = (p for p in p_possible if max_occur_map[p] <= 2)

# Replace 'repeat' digit in p with wildcard
# 171120233, 1 =>
# [171120233, 272220233, 373320233, 474420233, 575520233,
#  676620233, 777720233, 878820233, 979920233]
def gen_wildcard(p, repeat):
    strp = str(p)
    index = [i for i, j in enumerate(str(p)) if int(j) == repeat]
    start_range = 0 if 0 not in index else 1
    return [int(''.join([str(replace) if i in index else s for i, s in enumerate(strp)]))
            for replace in range(start_range, 10)]

for p in p_possible_small:
    family = [p for p in gen_wildcard(p, max_occur_map[p]) if p in p_possible]
    if len(family) == 8:
        print(family[0])
        break
