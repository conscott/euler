# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
# 1 through 5 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
from itertools import permutations

# Set of all valid pandigital products
products = set()

# Array of numbers to integer
# (1, 2, 3) -> 123
def a_to_n(a):
    return a if type(a) is int else int(''.join([str(i) for i in a]))

# Pandigital of for a * b = c in range [1,9]
# only works if c is 4 digit number and
# a is 1 digit and b is 5 digit or
# a is 2 digit and b is 3 digit
def check_perm(perm):
    ab, c = perm[:-4], a_to_n(perm[-4:])
    for i in range(1, 3):
        if a_to_n(ab[:i]) * a_to_n(ab[i:]) == c:
            products.add(c)


# All permutations of 1-9 are pandigital, just need to check
# if they are valid in form a * b = c
for i in permutations(list(range(1,10)), 9):
    check_perm(i)

print(sum(products))
