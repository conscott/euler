"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains
21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

primes = [2]
def check_prime(n):
    for p in primes:
        if p**2 > n:
            break
        if n % p == 0:
            return False
    return True

total_map, prime_total, n = {0:2}, 2, 3
while n < 1000000:
    if check_prime(n):
        primes.append(n)
        prime_total += n
        total_map[len(primes)-1] = prime_total
    n += 2

# Allow faster inclusive check
prime_set = set(primes)

max_cnt = max_total = 0
for i in range(len(primes)):
    if i > len(primes) - max_cnt:
        break
    for j in range(i+max_cnt, len(primes)):
        total = (total_map[j] - total_map[i-1]) if i > 0 else total_map[j]
        streak = j-i+1
        if total > 1000000:
            break
        if streak > max_cnt and total in prime_set:
            max_cnt, max_total = streak, total

print(max_total)
