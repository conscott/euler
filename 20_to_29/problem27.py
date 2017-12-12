# Find the product of the coefficients, a and b, for the
# quadratic expression that produces the maximum number of
# primes for consecutive values of nn, starting with n=0n=0.


primes = [2]
def add_prime(n):
    for p in primes:
        if p**2 > n:
            break
        if n % p == 0:
            return False
    primes.append(n)
    return True

def consec_p(a, b):
    n = 0
    while (n*n + a*n + b) in primes:
        n += 1
    return n

# seed primes less than 10000000
[add_prime(i) for i in range(3, 100000, 2)]

# b must be positive for case where n = 0
b_range = [p for p in primes if p < 1000]

consec_max = 0
consec_a_b = 0, 0
for b in b_range:
    # when n = 1, 1 + a + b > 0
    for a in [a for a in range(-999, 1000) if (1 + a + b) > 0]:
        consec = consec_p(a, b)
        if consec > consec_max:
            consec_max = consec
            consec_a_b = a, b

print("Max at %s with product %s" % (consec_a_b, consec_a_b[0] * consec_a_b[1]))
