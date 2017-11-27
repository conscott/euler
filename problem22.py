# Using names.txt, a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply
# this value by its alphabetical position in the list to obtain a name score.
#
# What is the total of all the name scores in the file?

import requests
import string

# Fetch name list online
r = requests.get('https://projecteuler.net/project/resources/p022_names.txt')

# Load in name list
names = [str(name.strip('"')) for name in r.text.split(',')]
names.sort()

# Rank name by index in list
name_rank = {name:i+1 for i, name in enumerate(names)}
print name_rank

# Make dictorary of letter -> score (A=1, B=2, C=3,...., Z=26)
score_map = {a:i+1 for i, a in enumerate(string.ascii_uppercase)}

def get_name_score(name):
    return sum([score_map[letter] for letter in name])

# Total = SUM of all name scores
print sum([get_name_score(name) * name_rank[name] for name in names])
