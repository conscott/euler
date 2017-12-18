"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

How many Lychrel numbers are there below ten-thousand?
"""

def lychrel(num):
    iters = 0
    while True:
        num = num + int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            return True
        iters += 1
        if iters > 50:
            break
    return False

print sum([1 for i in range(1, 10000) if not lychrel(i)])
