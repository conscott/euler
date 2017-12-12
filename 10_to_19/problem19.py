# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# 1 Jan 1900 was Monday
# 30 days Sept, April, June, November
# 28 for Feb
# 31 for the rest
# Leap year when divisble by 4, but not on century unless divisible by 400

MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# count through each year
total_days = 0
total_sundays = 0
for y in range(1901, 2001):
    if y == 1918:
        MONTHS[1] = 15
    elif y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0):
        MONTHS[1] = 29
    else:
        MONTHS[1] = 28
    for i, m in enumerate(MONTHS):
        total_days += m
        if total_days % 7 == 6:
            total_sundays += 1

print("Total Sundays on the first is %s" % total_sundays)
