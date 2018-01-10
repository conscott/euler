"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and
concatenating them in any order the result will always be prime. For example, taking
7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents
the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to
produce another prime.
"""

from itertools import permutations

primes = [2]
prime_set = set(primes)

def check_prime(n, pnt=False):
    if n in prime_set:
        return True
    for p in primes:
        if p**2 > n:
            break
        if n % p == 0:
            return False
    primes.append(n)
    prime_set.add(n)
    return True

def seed_primes(limit):
    [check_prime(n) for n in range(3, limit+1, 2)]

LIMIT = 10000
seed_primes(LIMIT)
set_size = 5
primes_copy = primes[:]

def make_chain(chain):
    if len(chain) == set_size:
        return chain
    for p in primes_copy:
        if p > chain[-1] and all_prime(chain+[p]):
            new_chain = make_chain(chain+[p])
            if new_chain:
                return new_chain
    return False

def all_prime(chain):
    return all(check_prime(int(str(p[0])+str(p[1])), pnt=True) for p in permutations(chain, 2))

chain = False
while not chain:
    chain = make_chain([primes_copy.pop(0)])

print sum(chain)
