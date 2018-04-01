# Problem 54 - Poker Hand - https://projecteuler.net/problem=54

def straight(hand):
    seq = []
    for card in hand:
        if card[0] == "T":
            value = 10
        elif card[0] == "J":
            value = 11
        elif card[0] == "Q":
            value = 12
        elif card[0] == "K":
            value = 13
        elif card[0] == "A":
            value = 14
        else:
            value = int(card[0])
        seq.append(value)

    seq = sorted(seq)
    is_straight = 0
    for i, v in enumerate(seq):
        if i < (len(seq) - 1):
            if seq[i+1] - v == 1:
                is_straight += 1

    if is_straight == 4:
        return True
    else:
        return False


def check_hand(hand):
    pairs = []
    points = 1
    flush = 0

    for card in hand:
        for card2 in hand:
            if card[1] == card2[1]:
                flush += 1

    if flush == 25:
        flush = True
    else:
        flush = False

    for card in hand:
        for card2 in hand:
            if card[0] == card2[0] and card != card2:
                pairs.append(card)

    if len(pairs) == 4:
        four = 0
        for card in pairs:
            if pairs[0][0] == card[0]:
                four += 1
        if four == 4:  # Four of a Kind: Four cards of the same value.
            points = 8
        else:
            points = 3  # Two Pairs: Two different pairs.
    elif len(pairs) == 2:
        points = 2
    elif len(pairs) == 6:
        points = 4
    elif len(pairs) == 8:
        points = 7

    is_straight = straight(hand)

    if points < 6:
        if flush and not is_straight:
            points = 6
            pairs = hand
        elif flush and is_straight:
            points = 9
            pairs = hand

    if len(pairs) == 0:
        if is_straight:
            points = 5
            pairs = hand
        else:
            points = 1
            pairs = hand

    return points, pairs


def higher_card(point_cards):
    value = 0
    for card in point_cards: 
        if card[0] == "T":
            if value < 10:
                value = 10
        elif card[0] == "J":
            if value < 11:
                value = 11
        elif card[0] == "Q":
            if value < 12:
                value = 12
        elif card[0] == "K":
            if value < 13:
                value = 13
        elif card[0] == "A":
             if value < 14:
                value = 14
        else:
            if value < int(card[0]):
                value = int(card[0])
    return value


with open("cards.txt") as cards:
    p1_wins = 0
    p2_wins = 0
    ties = 0
    for hand in cards:
        hand = hand.replace("\n", "").split(" ")
        p1_hand = hand[:int(len(hand)/2)]
        p2_hand = hand[int(len(hand)/2):]

        points_p1, point_cards_p1 = check_hand(p1_hand)
        points_p2, point_cards_p2 = check_hand(p2_hand)

        if points_p1 == points_p2:
            card_value_p1 = higher_card(point_cards_p1)
            card_value_p2 = higher_card(point_cards_p2)
            if card_value_p1 > card_value_p2:
                p1_wins += 1
            elif card_value_p1 < card_value_p2:
                p2_wins += 1
            else:
                ties += 1
        elif points_p1 > points_p2:
            p1_wins += 1
        elif points_p1 < points_p2:
            p2_wins += 1


    print("Player one wins: ", p1_wins)
    print("Player two wins: ", p2_wins)
    print("Ties: ", ties)
