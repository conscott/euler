"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater
than one-million?
"""

fact_cache = {}
def factorial(n):
    try:
        return fact_cache[n]
    except:
        t = reduce(lambda x, y: x*y, range(2, n+1))
        fact_cache[n] = t
        return t

def combo(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

print sum((1 for n in range(23, 101)
           for r in range(4, n-3)
           if combo(n, r) > 1000000))
