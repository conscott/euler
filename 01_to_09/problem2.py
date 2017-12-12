#
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.
#

fib_seq = [1, 2]
total = 2
while (fib_seq[-1] < 4000000):
    fib_seq.append(sum(fib_seq))
    fib_seq.pop(0)
    if fib_seq[-1] % 2 == 0:
        total = total + fib_seq[-1]

print(total)
