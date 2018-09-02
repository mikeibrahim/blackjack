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
colors = ['diamonds', 'clubs', 'heart', 'spades']

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        

def main():
    print("")
    print("------------")
    print(" Blackjack!")
    print("------------")
    print("")

    for color in colors:
        print("Color: " + color)
        
    deck = [Card(value, color) for value in range(1, 14) for color in colors]
    

    return 0
    
if __name__ == '__main__':
	main()
