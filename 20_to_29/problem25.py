# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

fibs = [1, 1]
idx = 2

while len(str(fibs[0])) < 1000:
    fibs = fibs[0] + fibs[1], fibs[0]
    idx += 1

print(idx)
