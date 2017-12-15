from collections import Counter
import requests

# Card rank {2: 2, 3: 3,..., A: 14}
crank = {str(i): i for i in range(2, 10)}
crank.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

# Inverse of Card Rank {2: 2, 3: 3,..., 14: A}
inv_crank = {j: i for i, j in crank.items()}

# Set of all available straight combos
straight_combos = [set([inv_crank[i] for i in range(i, i+5)]) for i in range(2, 11)]

def is_straight(cards):
    return set(cards.keys()) in straight_combos

def max_rank(cards):
    return reduce(lambda x, y: x if x[1] > y[1] else y, [(k, crank[k]) for k in cards])

def remove_cards_from_hand(card, hand):
    [hand.remove(i) for i in hand[:] if i[0] == card[0]]

def score(hand):
    cards = Counter(c[0] for c in hand)
    suits = Counter(c[1] for c in hand)

    # Get a map of most frequent cards and suit
    try:
        max_card, second_max_card = cards.most_common(2)
    except:
        max_card = cards.most_common(1)[0]
    max_suit = suits.most_common(1)[0]

    if max_card[1] == 1 and len(hand) > 1:
        card, max_card_rank = max_rank(cards)
        max_card = (card, 1)
    elif max_card[1] == 2 and second_max_card[1] == 2:
        card, max_card_rank = max_rank([max_card[0], second_max_card[0]])
        max_card = (card, 2)
    else:
        max_card_rank = crank[max_card[0]]

    # Royal Flush
    if all((a in cards for a in ['T', 'J', 'Q', 'K', 'A'])) and max_suit[1] == 5:
        return 10, max_card_rank, []
    # Straight Flush
    elif is_straight(cards) and max_suit[1] == 5:
        return 9, max_card_rank, []
    # Four of a kind
    elif max_card[1] == 4:
        remove_cards_from_hand(max_card, hand)
        return 8, max_card_rank, hand
    # Full House
    elif max_card[1] == 3 and second_max_card[1] == 2:
        remove_cards_from_hand(max_card, hand)
        return 7, max_card_rank, hand
    # Flush
    elif max_suit[1] == 5:
        return 6, max_card_rank, []
    # Straight
    elif is_straight(cards):
        return 5, max_card_rank, []
    # Three of Kind
    elif max_card[1] == 3:
        remove_cards_from_hand(max_card, hand)
        return 4, max_card_rank, hand
    # Two Pair
    elif max_card[1] == 2 and second_max_card[1] == 2:
        remove_cards_from_hand(max_card, hand)
        return 3, max_card_rank, hand
    # Pair
    elif max_card[1] == 2:
        remove_cards_from_hand(max_card, hand)
        return 2, max_card_rank, hand
    # High card
    elif max_card[1] == 1:
        remove_cards_from_hand(max_card, hand)
        return 1, max_card_rank, hand
    raise Exception("No choice")

def compare_hands(p1_hand, p2_hand):
    p1_score, p1_max_card, p1_hand_left = score(p1_hand)
    p2_score, p2_max_card, p2_hand_left = score(p2_hand)
    if p1_score != p2_score:
        return True if p1_score > p2_score else False
    if p1_max_card != p2_max_card:
        return True if p1_max_card > p2_max_card else False
    else:
        return compare_hands(p1_hand_left, p2_hand_left)

def get_winner(test):
    player1, player2 = test.split(' ')[:5], test.split(' ')[5:]
    return compare_hands(player1, player2)

rounds = requests.get('https://projecteuler.net/project/resources/p054_poker.txt').text.split('\n')[:-1]
print(sum([1 for r in rounds if get_winner(r)]))
