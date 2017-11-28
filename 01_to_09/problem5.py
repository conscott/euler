# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

primes = [2, 3, 5, 7, 11, 13, 17, 19]
max_factor = {}

# get a map of factors of n with the factors number of occurances
def factor(n):
    facts = {}
    for p in primes:
        while (n%p == 0):
            n /= p
            facts[p] = 1 if p not in facts else facts[p] + 1
        if n == 1:
            return facts

# Find factors of all the numbers 1-20 and keep a totally
# of max occurance of each factor
for i in range(2, 21):
    factors = factor(i)
    for f in factors.items():
        if f[0] not in max_factor or max_factor[f[0]] < f[1]:
            max_factor[f[0]] = f[1]

print reduce(lambda x, y: x*y, [f[0] ** f[1] for f in max_factor.items()])
