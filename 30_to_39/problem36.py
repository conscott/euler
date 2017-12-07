# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.

# Get binary string of number
def binary(num):
    return "{0:b}".format(num)

# Check is number is base10 and base2 palindrome
def palindrome(num):
    if str(num) == str(num)[::-1] and binary(num) == binary(num)[::-1]:
        return True
    return False

# Sum of all base10 and base2 palindromes under 1 million.
print sum([n for n in range(1, 1000001) if palindrome(n)])
