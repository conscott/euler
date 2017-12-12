"""
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2 so the
first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the
word a triangle word.

Using words.txt a 16K text file containing nearly two-thousand common English words, how
many are triangle words?
"""

import string
import requests

# Generate first 100 triangle numbers
triangle_nums = [(n*(n+1))/2 for n in range(1,100)]

# {a:1, b:2, c:3, ... , z:26}
alpha_weight = {s: i+1 for i, s in enumerate(string.ascii_uppercase)}

def word_weight(word):
    return sum([alpha_weight[a] for a in word])

r = requests.get("https://projecteuler.net/project/resources/p042_words.txt")
words = [str(name.strip('"')) for name in r.text.split(',')]

print(sum([1 for word in words if word_weight(word) in triangle_nums]))
