"""
It is possible to show that the square root of two can be expressed as an infinite
continued fraction.

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds the
number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more
digits than denominator?
"""

def add_num_to_fraction(num, numer, denom):
    numer += num*denom
    return numer, denom

def test_condition(it):
    numer, denom = 5, 2
    while it > 1:
        num_to_add = 1 if it == 2 else 2
        numer, denom = add_num_to_fraction(num_to_add, denom, numer)
        it -= 1
    return len(str(numer)) > len(str(denom))

print sum((1 for it in xrange(2, 1000) if test_condition(it)))
