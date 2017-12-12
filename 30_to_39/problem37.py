# The number 3797 has an interesting property. Being prime itself, it is possible to
# continuously remove digits from left to right, and remain prime at each stage:
# 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

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

# Check if a prime remains prime removing digits from
# the left and from the right
def check_condition(p):
    strp = str(p)
    return all(int(num) in prime_sets[len(num)] for num in set([strp[:i+1] for i in range(len(strp))] + [strp[i:] for i in range(len(strp))]))

total = 0
found = 0
for p in primes:
    if p > 10 and check_condition(p):
        total += p
        found += 1
        if found >= 11:
            break

print(total)
