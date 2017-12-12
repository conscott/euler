# Find the sum of all the numbers that can be written as the sum of
# fifth powers of their digits.

def pow_digits(n, p):
    return sum([int(d)**p for d in str(n)])

print(sum([i for i in range(2, 9**5*6) if pow_digits(i, 5) == i]))
