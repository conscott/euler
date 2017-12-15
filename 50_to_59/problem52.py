"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""

from collections import Counter

def digit_set(num):
    return Counter((s for s in str(num)))

for success in (i for exp in range(1, 10)
                for i in range(10**exp+1, 10**(exp+1)/6)
                if all(digit_set(j*i) == digit_set(i) for j in range(2, 7))):
    print success
    break
