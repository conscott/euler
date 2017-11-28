# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

primes = [2]
def check_prime(n):
    for p in primes:
        if p**2 > n:
            break
        if n % p == 0:
            return False
    primes.append(n)
    return True

for i in xrange(3, 2000000, 2):
    check_prime(i)

print sum(primes)
