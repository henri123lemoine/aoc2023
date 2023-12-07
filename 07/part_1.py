import sys
data = sys.stdin.readlines()

def score(hand: str):
    cards = "AKQJT98765432"
    hand_score = sum((14 - cards.index(card))*10**(2*(5-i)) for i, card in enumerate(hand))

    hand = sorted(hand)

    # Check for five of a kind
    if hand[0] == hand[4]:
        return 7e15 + hand_score
    # Check for four of a kind
    elif hand[0] == hand[3] or hand[1] == hand[4]:
        return 6e15 + hand_score
    # Check for full house
    elif (hand[0] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[4]):
        return 5e15 + hand_score
    # Check for three of a kind
    elif hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]:
        return 4e15 + hand_score
    # Check for two pair
    elif (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[0] == hand[1] and hand[3] == hand[4]) or (hand[1] == hand[2] and hand[3] == hand[4]):
        return 3e15 + hand_score
    # Check for one pair
    elif hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
        return 2e15 + hand_score
    # Check for high card
    else:
        return 1e15 + hand_score


hands = []
for line in data:
    line = line.strip()
    hand, bid = line.split(" ")
    hands.append((hand, int(bid)))

hands = sorted(hands, key=lambda x: score(x[0]))

sol = 0
for i, (hand, bid) in enumerate(hands, start=1):
    sol += bid * i

print(sol)
