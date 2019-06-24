import random
from deck import Deck
from war_player import Player

class War:
    def __init__(self, human=True):
        self.human = human
        self.winner = None
        self.draw = False
        self.player1 = self.create_player('Player 1')
        self.player2 = self.create_player('Player 2')
    
    def create_player(self, name):
        if self.human:
            name = input("Enter {}'s name:".format(name))
        return Player(name)
    
    def the_deal(self):
        deck = Deck()
        deck.shuffle()
        while not deck.is_empty():
            self.player1.add_card(deck.draw_card())
            self.player2.add_card(deck.draw_card())
    
    def empty_table(self):
        self.player1.empty_hand()
        self.player2.empty_hand()
        self.winner = None
        self.draw = False

    def play_game(self):
        while True:
            self.empty_table()
            self.the_deal()
            while not self.winner and not self.draw:
                self.play_round()
            if self.draw:
                self.display_draw()
            else:
                self.display_winner()
            choice = input("Do you want to play another game: Yes(Y) or No(N): ")
            if choice in {'N','n'}:
                break

    def war(self, card_pool):
        print('It is war time!')
        print('Cards in the pool right now:', card_pool)
        if self.player1.is_empty():
            if self.player2.is_empty():
                self.display_draw()
                self.draw = True
                return
            print('{} ran out of cards during the war!'.format(self.player1))
            self.winner = self.player2
            return
        elif self.player1.cards_in_hand()==1:
            if self.player2.cards_in_hand()==1:
                self.display_draw()
                self.draw = True
                return
            elif self.player2.is_empty():  # This case actually won't happen, since they are in total even number of cards
                print('{} ran out of cards during the war!'.format(self.player2))
                self.winner = self.player1
                return
            print('{} ran out of cards during the war!'.format(self.player1))
            self.winner = self.player2
            return
        elif len(self.player2.hand)<2:
                print('{} ran out of cards during the war!'.format(self.player2))
                self.winner = self.player1
                return
        print('Each player places a card into the card pool before the next round.')
        card_pool.append(self.player1.display_card())
        card_pool.append(self.player2.display_card())
        self.play_round(card_pool)        

    def play_round(self, card_pool = []):
        print('Currently, {} has {} cards, and {} has {} cards'.format(self.player1.name, self.player1.cards_in_hand(),
                                                                       self.player2.name, self.player2.cards_in_hand()))
        card1 = self.player1.display_card()
        card2 = self.player2.display_card()
        print('{} places card {}, and {} places card {}'.format(self.player1.name, card1, self.player2.name, card2))
        card_pool.extend([card1,card2])
        random.shuffle(card_pool)
        if card1<card2: # Player 2 is the winner of this round
            while card_pool:
                self.player2.add_card(card_pool.pop())
            if self.player1.is_empty():
                print('{} ran out of cards!'.format(self.player1))
                self.winner = self.player2
        elif card1==card2:
            self.war(card_pool)
        else: # Player 1 is the winner for this round
            while card_pool:
                self.player1.add_card(card_pool.pop())
            if self.player2.is_empty():
                print('{} ran out of cards!'.format(self.player2))
                self.winner = self.player1
             
    def display_draw(self):
        print('It is a draw! Both players ran out of cards at the same time!')
    
    def display_winner(self):
        print('The winner of the game is:', self.winner.name)
    

    
    