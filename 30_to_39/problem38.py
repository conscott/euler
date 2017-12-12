# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?

from itertools import permutations

max_pandigital = 918273645

# Assume product is a 4 digit number
# Then for n = 1, 2, 3
# pan[:4] / 1 = product
# pan[4:] / 2 = product
def check_pandigital(pan):
    product = int(str(pan)[:4])
    return float(str(pan)[4:]) / product == 2


# We know greatest starts with 9 - so we only have to permute 1-8
# and check if it meets the conditions
for i in permutations(list(range(1, 9))):
    num = int('9' + ''.join([str(n) for n in i]))
    if i < max_pandigital:
        continue
    if check_pandigital(num) and num > max_pandigital:
        max_pandigital = num

print(max_pandigital)
