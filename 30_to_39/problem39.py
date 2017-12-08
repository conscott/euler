# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# For which value of p <= 1000, is the number of solutions maximised?



def find_solutions(p):
    """
        Have equations,
        p = a + b + c
        c*c = a*a + b*b

        substituing c = p-a-b into c*2 = a*2 + b*2

        b = (p*2 - 2*a*p) / (2*p - 2*a)

        We also know c > a, b so a < p/2
    """
    soln = set()
    for a in range(1, p/2):
        num = p*p - 2*a*p
        denom = 2*p - 2*a
        if num % denom == 0:
            soln.add(p - a - num/denom)
    return len(soln)


print reduce(lambda x, y: x if x[1] > y[1] else y, [(p, find_solutions(p)) for p in range(12, 1001)])[0]
