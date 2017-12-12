# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

done = False
for c in range (1000, 1, -1):
    for b in range (1, 1000-c):
        a = 1000 - c - b
        if a**2 + b**2 == c**2:
            done = True
            print(a, b, c, (a*b*c))
            break
    if done:
        break
