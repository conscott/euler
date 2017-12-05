# How many different ways can 2 pounds be made using any number of coins?

coin_demon = [1, 2, 5, 10, 20, 50, 100, 200]

# Recuresively check all combinations and store ones
# that add correctly
def comb_to_sum(target, coin_now=0, total=0):
    valid_combos = 0
    if total == target:
        return 1
    for coin in (coin for coin in coin_demon if coin >= coin_now):
        if total + coin <= target:
            valid_combos += comb_to_sum(target, coin, total + coin, valid_combos)
    return valid_combos

print comb_to_sum(200)
