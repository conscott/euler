# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.
# There are exactly four non-trivial examples of this type of fraction, less than one
# in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find
# the value of the denominator.
import math

# 98 -> ['9', '8']
def num_to_str_array(num):
    return [i for i in str(num)]

def digit_cancel(num, denom):
    sarray_num = num_to_str_array(num)
    sarray_denom = num_to_str_array(denom)
    # Name name in numerator and denominator and fraction with repeated number removed
    # must be reduction of original fraction
    if ((sarray_denom[1] is not '0' and
         float(sarray_num[0]) / float(sarray_denom[1]) == (float(num) / denom) and
         sarray_num[1] == sarray_denom[0]) or
        (sarray_denom[0] is not '0' and
         float(sarray_num[1]) / float(sarray_denom[0]) == (float(num) / denom) and
         sarray_num[0] == sarray_denom[1])):
        return True
    return False

def reduce_fraction(num, denom):
    # Reduce the fraction
    reducer = 2
    while num > 1 and reducer <= num:
        while num % reducer == 0 and denom % reducer == 0:
            num /= reducer
            denom /= reducer
        reducer += 1
    return num, denom

# Get the numerator / denominator of all franctions that can be cancelled by digits
num, denom = reduce(lambda x, y: (x[0] * y[0], x[1] * y[1]),
                    [(i, j) for i in range(10, 100) for j in range(i, 100) if i !=j and digit_cancel(i, j)])

print reduce_fraction(num, denom)[1]
