#!/usr/bin/env python
#
# Author: Mike Ibrahim
# Date: 9/01/18
# Version 1.0
#
# Repository: https://github.com/mikeibrahim/blackjack
#
#  blackjack.py
#  
#  Black jack card game: AKA 21
#

# Import Libraries needed
import time

# Array of Cards
suits = ['Diamonds', 'Clubs', 'Heart', 'Spades']
ranks = [["A",1], ["2",2], ["3",3], ["4",4], ["5",5], ["6",6], ["7",7], ["8",8], ["9",9], ["10",10], ["J",10], ["Q",10], ["K",10]]

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank[0]
        self.suit = suit
        self.value = rank[1]
#        print(self.rank + " " + self.suit + ": " + str(self.value))
        
    def show(self):
        print(self.rank + " " + self.suit)
        


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def show(self):
        print("Deck size: " + str(len(self.cards)))
        for c in self.cards:
            c.show()

def main():
    print("")
    print("------------")
    print(" Blackjack!")
    print("------------")
    print("")

#    deck = [Card(rank, suit) for rank in ranks for suit in suits]
    deck = Deck()  
    deck.show()
    

    return 0
    
if __name__ == '__main__':
	main()
