# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

print sum(range(101))**2 - sum([i*i for i in xrange(101)])
