# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

# Only going to need factorial of 0-9
fact_cache = {i: fact(i) for i in range(10)}

# Sum of factorial of digits
# 143 => 1! + 4! + 3!
def fact_digits(num):
    return sum([fact_cache[int(i)] for i in str(num)])

# Upper limit is 7 * 9!
print(sum([i for i in range(3, 1000000) if fact_digits(i) == i]))
