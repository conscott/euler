# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# Seed prime list with
primes = [2]
def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    primes.append(n)
    return True

i = 3
while len(primes) < 10001:
    is_prime(i)
    i += 2

print primes[-1]
