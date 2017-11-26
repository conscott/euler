# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain

cached = {}
def seqlen(n):
    l = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n+1
        l += 1
    return l

m = (1, 1)
for i in range(2**19+1, 1000000, 2):
    l = seqlen(i)
    if l > m[1]:
        m = (i, l)

print "Max seq length is %s for %s" % (m[1], m[0])
