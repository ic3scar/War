# Use deque to store player's hand
from collections import deque
import random

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = deque()
    
    def empty_hand(self):
        self.hand = deque()

    def shuffle(self):
        if not self.is_empty():
            random.shuffle(self.hand)

    def add_card(self,card):
        self.hand.append(card)

    def display_card(self): # For war game
        if not self.is_empty():
            return self.hand.popleft()

    def cards_in_hand(self):
        return len(self.hand)

    def is_empty(self):
        return not self.hand

    def __repr__(self):
        return self.name