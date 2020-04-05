import random
import numpy as np 

class Card: 
    def __init__(self,rank,suit):
        """
        Initialize a single card with given rank and suit
        """
        self.rank = rank
        self.suit = suit

    def print_card(self):
        """
        Print rank and suit of a single card object
        """
        print(self.rank2str(), ' of ', self.suit2str())

    def suit2str(self):
        switch = {
            0: 'clubs',
            1: 'spades',
            2: 'diamonds', 
            3: 'hearts'
        }
        return switch.get(self.suit)
    
    def rank2str(self):

        switch = {
            0: 'two',
            1: 'three',
            2: 'four', 
            3: 'five', 
            4: 'six', 
            5: 'seven', 
            6: 'eight', 
            7: 'nine', 
            8: 'ten', 
            9: 'jack', 
            10: 'queen', 
            11: 'king', 
            12: 'ace' 
        }
        return switch.get(self.rank)

        

class CardDeck:
    def __init__(self):
        """
        initialize a deck of cards
        """
        self.cards = [0]*52
        self.suits = [i for i in range(4)]
        self.ranks = [i for i in range(13)]
        i = 0
        for s in self.suits:
            for r in self.ranks:
                self.cards[i] = Card(r,s)
                i += 1

    def print_deck(self):
        """
        print the value of every single card in the deck
        """
        for i in range(len(self.cards)):
            self.cards[i].print_card()

    def shuffle_deck(self):
        """
        Shuffle the deck of cards
        """
        random.shuffle(self.cards)

    def draw_and_remove(self):
        """
        Draw and remove a random card from the deck
        """
        index = np.random.randint(len(self.cards))
        return self.cards.pop(index)

    def get_length(self):
        """
        returns the number of cards left in the deck
        """
        return len(self.cards)


if __name__ ==  '__main__':

    deck = CardDeck()
    print('Initialized: ')
    deck.print_deck()

    deck.shuffle_deck()
    print('Shuffled: ')
    deck.print_deck()

    print('Random card: ')
    random_card = deck.draw_and_remove()
    random_card.print_card()
    
    
    