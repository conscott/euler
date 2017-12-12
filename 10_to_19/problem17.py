# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

m = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

# Sum 1-9
t_1_to_9 = sum([len(m[i]) for i in range(1, 10)])
# Sum 10-19
t_10_to_19 = sum([len(m[i]) for i in range(10, 20)])
# Sum 20-99
t_20_to_99 = sum([(len(m[i*10])*10 + t_1_to_9) for i in range(2, 10)])
# Sum 1-99
t_1_to_99 = t_1_to_9 + t_10_to_19 + t_20_to_99
# Sum 100-99 (3*99 = 'and')
t_100_999 = sum([(len(m[i]+m[100])*100 + t_1_to_99 + 3 * 99) for i in range(1, 10)])
# Sum [1,99] + [100,999] + [1000]
print(t_1_to_99 + t_100_999 + len(m[1]+m[1000]))
