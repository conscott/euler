# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.


def len_cycle(n):
    divisor = 10
    remainders = []
    while divisor != 0:
        r = divisor % n
        if r in remainders:
            break
        remainders.append(r)
        divisor = r*10
    return len(remainders)

print(reduce(lambda x, y: x if x[1] > y[1] else y, [(i, len_cycle(i)) for i in range(1, 1000)])[0])
