# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
#
# If dn represents the nth digit of the fractional part, find the value of the
# following expression.
# d1 X d10 X d100 X d1000 X d10000 X d100000 X d1000000

digit_array = []
num = 1
while len(digit_array) < 1000000:
    digit_array.extend([int(i) for i in str(num)])
    num += 1

print reduce(lambda x, y: x*y, [digit_array[10**i-1] for i in range(7)])
