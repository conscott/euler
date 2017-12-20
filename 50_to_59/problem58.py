"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with
side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what
is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
that is, a ratio of 8/13 ~ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length
9 will be formed. If this process is continued, what is the side length of the square spiral
for which the ratio of primes along both diagonals first falls below 10%?
"""
from itertools import count

primes = [2]
prime_set = set(primes)

def seed_primes(limit):
    [check_prime(n) for n in range(3, limit+1, 2)]

def check_prime(n):
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

seed_primes(100000)

corner = 1
num_corners = 1
num_prime_corners = 0
for layer in count(1):
    for i in range(4):
        corner += layer * 2
        if check_prime(corner):
            num_prime_corners += 1
    num_corners += 4
    if float(num_prime_corners) / num_corners < 0.1:
        print(layer*2+1)
        break
