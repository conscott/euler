"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number,
134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from itertools import count

total = 0
for power in range(1, 100):
    i = int(10**((power-1.0)/power))
    while True:
        nlen = len(str(i**power))
        if nlen > power:
            break
        if nlen == power:
            total += 1
        i += 1

print total
