"""
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def digit_sum(num):
    return sum([int(i) for i in str(num)])

print(max([digit_sum(a**b) for a in range(70, 100) for b in range(70, 100)]))
