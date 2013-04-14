# coding=utf-8
import random

suits = u'♠♣♥♦'
ranks = 'A23456789TJQK'

deck = [rank + suit for suit in suits 
                    for rank in ranks]

def print_cards(cards):
    for index, card in enumerate(cards, 1):
        print card,

        if index % 13 == 0:
            print
    
    print

print_cards(deck)

copied = deck[:]
copied2 = list(deck)

# pick a card, any card
print random.choice(deck)
print random.choice(deck)
print random.choice(deck)
print

# shuffle, without embarrassment
random.shuffle(deck)

# deal some cards, but remember...
hand = deck[:5]
print_cards(hand)

# slice makes a *copy*
print len(deck)

# so you have to remove the dealt cards
deck = deck[5:]
print len(deck)

# that's a teeny bit icky, lets fix it
def deal(n, cards):
    hand = [cards.pop(0) for _x in range(n)]
    return hand

hand2 = deal(5, deck)
print_cards(hand2)
print len(deck)

