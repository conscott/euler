"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and
66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations
of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import collections

# Check if two numbers are class of same permutation
def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in str(a):
        d[x] += 1
    for x in str(b):
        d[x] -= 1
    return not any(d.itervalues())

# Generate some big cubes
cubes = [i**3 for i in range(1002, 10000)]

# Setup len of digit brackets to reduce search space
cube_dict = {}
for c in cubes:
    l = len(str(c))
    if l in cube_dict:
        cube_dict[l].append(c)
    else:
        cube_dict[l] = [c]

for cube in cubes:
    cnt = 1
    for cube_higher in (c for c in cube_dict[len(str(cube))] if c > cube):
        if same_permutation(cube, cube_higher):
            cnt += 1
            if cnt > 4:
                print cube
                exit(1)
