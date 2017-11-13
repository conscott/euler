# A palindromic number reads the same both ways.
# Find the largest palindrome made from the product of two 3-digit numbers.

MAX = 1

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print max([i*j for i in range(1, 999) for j in range(i, 999) if is_palindrome(i*j)])
