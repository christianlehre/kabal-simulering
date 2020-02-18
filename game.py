from cards import CardDeck, Card

class game:
    def __init__(self,cards_drawn = 4):
        self.cards_drawn = cards_drawn

        self.deck = CardDeck()
        self.deck.shuffle_deck()

        # initialize the stacks with a single card in each stack
        self.stack1 = [self.deck.draw_and_remove()]
        self.stack2 = [self.deck.draw_and_remove()]
        self.stack3 = [self.deck.draw_and_remove()]
        self.stack4 = [self.deck.draw_and_remove()]
    
    def print_stacks(self):
        print('Stack 1: \n')
        [self.stack1[i].print_card() for i in range(len(self.stack1))]
        print('\nStack 2: \n')
        [self.stack2[i].print_card() for i in range(len(self.stack2))]
        print('\nStack 3: \n')
        [self.stack3[i].print_card() for i in range(len(self.stack3))]
        print('\nStack 4: \n')
        [self.stack4[i].print_card() for i in range(len(self.stack4))]

    def drawFour(self):
        if self.cards_drawn <= 48:
            self.stack1.append(self.deck.draw_and_remove())
            self.stack2.append(self.deck.draw_and_remove())
            self.stack3.append(self.deck.draw_and_remove())
            self.stack4.append(self.deck.draw_and_remove())
            self.cards_drawn += 4
        else: 
            print('Deck is empty')
        

    def removeCard(self): #TODO: fix to handle empty lists
        """
        removes the lowest rank of each suit if more than 1 are present
        """
        if len(self.stack1) == 0:
            card1 = Card(-1,-1)
        else:
            card1 = self.stack1[-1]

        if len(self.stack2) == 0:
            card2 = Card(-2,-2)
        else:
            card2 = self.stack2[-1]
        
        if len(self.stack3) == 0:
            card3 = Card(-3,-3)
        else:
            card3 = self.stack3[-1]
        
        if len(self.stack4) == 0:
            card4 = Card(-4,-4)
        else:
            card4 = self.stack4[-1]
    
        if card1.suit == card2.suit and card1.suit == card3.suit and card1.suit == card4.suit: # 4 equals
            if card1.suit > card2.suit and card1.suit > card3.suit and card1.suit > card4.suit:
                self.stack2.pop()
                self.stack3.pop()
                self.stack4.pop()

            elif card2.suit > card1.suit and card2.suit > card3.suit and card2.suit > card4.suit:
                self.stack1.pop()
                self.stack3.pop()
                self.stack4.pop()
            
            elif card3.suit > card1.suit and card3.suit > card2.suit and card3.suit > card4.suit:
                self.stack1.pop()
                self.stack2.pop()
                self.stack4.pop()

            else:
                self.stack1.pop()
                self.stack2.pop()
                self.stack3.pop()

        elif card1.suit == card2.suit and card1.suit == card3.suit:# 3 equals: 1=2=3
            if card1.rank > card2.rank and card1.rank > card3.rank:
                self.stack2.pop()
                self.stack3.pop()

            elif card2.rank > card1.rank and card2.rank > card3.rank:
                self.stack1.pop()
                self.stack3.pop()

            else:
                self.stack1.pop()
                self.stack2.pop()

        elif card1.suit == card2.suit and card1.suit == card4.suit: # 1=2=4
            if card1.rank > card2.rank and card1.rank > card4.rank:
                self.stack2.pop()
                self.stack4.pop()
            
            elif card2.rank > card1.rank and card2.rank > card4.rank:
                self.stack1.pop()
                self.stack4.pop()

            else:
                self.stack1.pop()
                self.stack2.pop()

        elif card2.suit == card3.suit and card2.suit == card4.suit: # 2=3=4
            if card2.rank > card3.rank and card2.rank > card4.rank:
                self.stack3.pop()
                self.stack4.pop()
            
            elif card3.rank > card2.rank and card3.rank > card4.rank:
                self.stack2.pop()
                self.stack4.pop()
            
            else: 
                self.stack2.pop()
                self.stack3.pop()
        elif card1.suit == card3.suit and card1.suit == card4.suit: # 1=3=4
            if card1.rank > card3.rank and card1.rank > card4.rank:
                self.stack3.pop()
                self.stack4.pop()

            elif card3.rank > card1.rank and card3.rank > card4.rank:
                self.stack1.pop()
                self.stack4.pop()

            else:
                self.stack1.pop()
                self.stack3.pop()

        elif card1.suit == card2.suit: # 2 equals: 1=2
            if card1.rank > card2.rank:
                self.stack2.pop()
            else: 
                self.stack1.pop()
        elif card1.suit == card3.suit:  # 1 = 3
            if card1.rank > card3.rank:
                self.stack3.pop()
            else:
                self.stack1.pop()
        elif card1.suit == card4.suit: # 1 = 4
            if card1.rank > card4.rank:
                self.stack4.pop()
            else:
                self.stack1.pop()
        elif card2.suit == card3.suit: # 2 = 3
            if card2.rank > card3.rank:
                self.stack3.pop()
            else:
                self.stack2.pop()
        elif card2.suit == card4.suit: # 2 = 4
            if card2.rank > card4.rank:
                self.stack4.pop()
            else:
                self.stack2.pop()
        elif card3.suit == card4.suit: # 3 = 4
            if card3.rank > card4.rank:
                self.stack4.pop()
            else:
                self.stack4.pop()
        else:  
            print("No cards removed")

    def isWon(self):
        """
        game is won when there are only aces left in the stacks, and no cards left in the deck
        """
        if len(self.stack1) < 1 or len(self.stack2) < 1 or len(self.stack3) < 1 or len(self.stack4) < 1:
            return False

        card1 = self.stack1[-1] 
        card2 = self.stack2[-1]
        card3 = self.stack3[-1]
        card4 = self.stack4[-1]

        if card1.rank == 12 and card2.rank == 12 and card3.rank == 12 and card4.rank == 12:
            if self.cards_drawn == 52 and len(self.stack1) == 1 and len(self.stack2) == 1 and len(self.stack3) == 1 and len(self.stack4) == 1: 
                #print('Game is won!')
                return True
            else: 
                #print('Game is lost')
                return False
        

    def freePositions(self):
        """
        returns number of free positions
        """
        free = 0
        if len(self.stack1) == 0:
            free += 1
        if len(self.stack2) == 0:
            free += 1
        if len(self.stack3) == 0:
            free += 1
        if len(self.stack4) == 0:
            free += 1
        return free

    def isEqualSuits(self):
        """
        returns true if there are equal suits present in the stacks
        Brute force
        """
        if len(self.stack1) > 0 and len(self.stack2) > 0 and len(self.stack3) > 0 and len(self.stack4) > 0: # no free slots
            if self.stack1[-1].suit == self.stack2[-1].suit or self.stack1[-1].suit == self.stack3[-1].suit or self.stack1[-1].suit == self.stack4[-1].suit or self.stack2[-1].suit == self.stack3[-1].suit or self.stack2[-1].suit == self.stack4[-1].suit or self.stack3[-1].suit == self.stack4[-1].suit:
                return True
            else:
                return False
        elif len(self.stack2) > 0 and len(self.stack3) > 0 and len(self.stack4) > 0 and len(self.stack1) == 0: # free slot in position 1
            if self.stack2[-1].suit == self.stack3[-1].suit or self.stack2[-1].suit == self.stack4[-1].suit or self.stack3[-1].suit == self.stack4[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) > 0 and len(self.stack3) > 0 and len(self.stack4) > 0 and len(self.stack2) == 0: # free slot in position 2
            if self.stack1[-1].suit == self.stack3[-1].suit or self.stack1[-1].suit == self.stack4[-1].suit or self.stack3[-1].suit == self.stack4[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) > 0 and len(self.stack2) > 0 and len(self.stack4) > 0 and len(self.stack3) == 0: # free slot in position 3
            if self.stack1[-1].suit == self.stack2[-1].suit or self.stack1[-1].suit == self.stack4[-1].suit or self.stack2[-1].suit == self.stack4[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) > 0 and len(self.stack2) > 0 and len(self.stack3) > 0 and len(self.stack4) == 0: # free slot in position 4
            if self.stack1[-1].suit == self.stack2[-1].suit or self.stack1[-1].suit == self.stack3[-1].suit or self.stack2[-1].suit == self.stack3[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) > 0 and len(self.stack2) > 0 and len(self.stack3) == 0 and len(self.stack4) == 0: # free slots in position 3 and 4
            if self.stack1[-1].suit == self.stack2[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) > 0 and len(self.stack2) == 0 and len(self.stack3) > 0 and len(self.stack4) == 0: # free slots in position 2 and 4
            if self.stack1[-1].suit == self.stack3[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) > 0 and len(self.stack2) == 0 and len(self.stack3) == 0 and len(self.stack4) > 0: # free slots in position 2 and 3
            if self.stack1[-1].suit == self.stack4[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) == 0 and len(self.stack2) > 0 and len(self.stack3) > 0 and len(self.stack4) == 0: # free slots in position 1 and 4
            if self.stack2[-1].suit == self.stack3[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) == 0 and len(self.stack2) > 1 and len(self.stack3) == 0 and len(self.stack4) > 0: # free slots in position 1 and 3
            if self.stack2[-1].suit == self.stack4[-1].suit:
                return True
            else:
                return False
        elif len(self.stack1) == 0 and len(self.stack2) == 0 and len(self.stack3) > 0 and len(self.stack4) > 0: # free slots in position 1 and 2
            if self.stack3[-1].suit == self.stack4[-1].suit:
                return True
            else:
                return False
        else:
            return False

    def moveCards(self): 
        """
        move cards into free slots. Greedy approach in terms of always moving the greatest rank, independent of suit, to an open slot
        """
        if len(self.stack1) < 1: # free position in stack 1
            if len(self.stack2) >= 2 and len(self.stack3) >=2 and len(self.stack4) >=2: # move from stack 2,3 or 4
                if self.stack2[-1].rank >= self.stack3[-1].rank and self.stack2[-1].rank >= self.stack4[-1].rank: 
                    self.stack1.append(self.stack2[-1])
                    self.stack2.pop()
                elif self.stack3[-1].rank >= self.stack4[-1].rank:
                    self.stack1.append(self.stack3[-1])
                    self.stack3.pop()
                else:
                    self.stack1.append(self.stack4[-1])
                    self.stack4.pop()

            elif len(self.stack2) >= 2 and len(self.stack3) >=2: # move from stack 2 or 3
                if self.stack2[-1].rank >= self.stack3[-1].rank:
                    self.stack1.append(self.stack2[-1])
                    self.stack2.pop()
                else:
                    self.stack1.append(self.stack3[-1])
                    self.stack3.pop()

            elif len(self.stack2) >= 2 and len(self.stack4) >=2: # move from stack 2 or 4
                if self.stack2[-1].rank >= self.stack4[-1].rank:
                    self.stack1.append(self.stack2[-1])
                    self.stack2.pop()
                else:
                    self.stack1.append(self.stack4[-1])
                    self.stack4.pop()

            elif len(self.stack3) >= 2 and len(self.stack4) >=2: # move from stack 3 or 4
                if self.stack3[-1].rank >= self.stack4[-1].rank:
                    self.stack1.append(self.stack3[-1])
                    self.stack3.pop()
                else:
                    self.stack1.append(self.stack4[-1])
                    self.stack4.pop()

            elif len(self.stack2) >= 2: # move from stack 2
                self.stack1.append(self.stack2[-1])
                self.stack2.pop()

            elif len(self.stack3) >= 2: # move from stack 3
                self.stack1.append(self.stack3[-1])
                self.stack3.pop()

            elif len(self.stack4) >= 2: # move from stack 4
                self.stack1.append(self.stack4[-1])
                self.stack4.pop()

        if len(self.stack2) < 1: # free position in stack 2 
            if len(self.stack1) >= 2 and len(self.stack3) >=2 and len(self.stack4) >=2: # move from stack 1,3 or 4
                if self.stack1[-1].rank >= self.stack3[-1].rank and self.stack1[-1].rank >= self.stack4[-1].rank:
                    self.stack2.append(self.stack1[-1])
                    self.stack1.pop()
                elif self.stack3[-1].rank >= self.stack4[-1].rank:
                    self.stack2.append(self.stack3[-1])
                    self.stack3.pop()
                else:
                    self.stack2.append(self.stack4[-1])
                    self.stack4.pop()


            elif len(self.stack1) >= 2 and len(self.stack3) >=2: # move from stack 1 or 3
                if self.stack1[-1].rank >= self.stack3[-1].rank:
                    self.stack2.append(self.stack1[-1])
                    self.stack1.pop()
                else:
                    self.stack2.append(self.stack3[-1])
                    self.stack3.pop()

            elif len(self.stack1) >= 2 and len(self.stack4) >=2: # move from stack 1 or 4
                if self.stack1[-1].rank >= self.stack4[-1].rank:
                    self.stack2.append(self.stack4[-1])
                    self.stack4.pop()
                else:
                    self.stack2.append(self.stack1[-1])
                    self.stack1.pop()

            elif len(self.stack3) >= 2 and len(self.stack4) >=2: # move from stack 3 or 4
                if self.stack3[-1].rank >= self.stack4[-1].rank:
                    self.stack2.append(self.stack3[-1])
                    self.stack3.pop()
                else:
                    self.stack2.append(self.stack4[-1])
                    self.stack4.pop()

            elif len(self.stack1) >=2: # move from stack 1
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()

            elif len(self.stack3) >=2: # move from stack 3
                self.stack2.append(self.stack3[-1])
                self.stack3.pop()

            elif len(self.stack4) >=2: # move from stack 4
                self.stack2.append(self.stack4[-1])
                self.stack4.pop()

        if len(self.stack3) < 1: # free position in stack 3 
            if len(self.stack1) >= 2 and len(self.stack2) >=2 and len(self.stack4) >=2: # move from stack 1, 2 or 4
                if self.stack1[-1].rank >= self.stack2[-1].rank and self.stack1[-1].rank >= self.stack4[-1].rank:
                    self.stack3.append(self.stack1[-1])
                    self.stack1.pop()
                elif self.stack2[-1].rank >= self.stack4[-1].rank:
                    self.stack3.append(self.stack2[-1])
                    self.stack2.pop()
                else:
                    self.stack3.append(self.stack4[-1])
                    self.stack4.pop()

            elif len(self.stack2) >= 2 and len(self.stack4) >=2: # move from stack 2 or 4
                if self.stack2[-1].rank >= self.stack4[-1].rank:
                    self.stack3.append(self.stack2[-1])
                    self.stack2.pop()
                else:
                    self.stack3.append(self.stack4[-1])
                    self.stack4.pop()

            elif len(self.stack1) >= 2 and len(self.stack2) >=2: # move from stack 1 or 2
                if self.stack1[-1].rank >= self.stack2[-1].rank:
                    self.stack3.append(self.stack1[-1])
                    self.stack1.pop()
                else:
                    self.stack3.append(self.stack2[-1])
                    self.stack2.pop()

            elif len(self.stack1) >= 2 and len(self.stack4) >=2: # move from stack 1 or 4
                if self.stack1[-1].rank >= self.stack4[-1].rank:
                    self.stack3.append(self.stack1[-1])
                    self.stack1.pop()
                else:
                    self.stack3.append(self.stack4[-1])
                    self.stack4.pop()

            elif len(self.stack1) >= 2: # move from stack 1
                self.stack3.append(self.stack1[-1])
                self.stack1.pop()

            elif len(self.stack2) >= 2: # move from stack 2
                self.stack3.append(self.stack2[-1])
                self.stack2.pop()

            elif len(self.stack4) >= 2: # move from stack 4
                self.stack3.append(self.stack4[-1])
                self.stack4.pop()

        if len(self.stack4) < 1: #free position in stack 4 
            if len(self.stack1) >= 2 and len(self.stack2) >=2 and len(self.stack3) >=2: # move from stack 1, 2 or 3
                if self.stack1[-1].rank >= self.stack2[-1].rank and self.stack1[-1].rank >= self.stack3[-1].rank:
                    self.stack4.append(self.stack1[-1])
                    self.stack1.pop()
                elif self.stack2[-1].rank >= self.stack3[-1].rank:
                    self.stack4.append(self.stack2[-1])
                    self.stack2.pop()
                else:
                    self.stack4.append(self.stack3[-1])
                    self.stack3.pop()

            elif len(self.stack1) >= 2 and len(self.stack2) >=2: # move from stack 1 or 2
                if self.stack1[-1].rank >= self.stack2[-1].rank:
                    self.stack4.append(self.stack1[-1])
                    self.stack1.pop()
                else:
                    self.stack4.append(self.stack2[-1])
                    self.stack2.pop()

            elif len(self.stack1) >= 2 and len(self.stack3) >=2: # move from stack 1 or 3
                if self.stack1[-1].rank >= self.stack3[-1].rank:
                    self.stack4.append(self.stack1[-1])
                    self.stack1.pop()
                else:
                    self.stack4.append(self.stack3[-1])
                    self.stack3.pop()

            elif len(self.stack2) >= 2 and len(self.stack3) >=2: # move from stack 2 or 3
                if self.stack2[-1].rank >= self.stack3[-1].rank:
                    self.stack4.append(self.stack2[-1])
                    self.stack2.pop()
                else:
                    self.stack4.append(self.stack3[-1])
                    self.stack3.pop()


            elif len(self.stack1) >= 2: # move from stack 1
                self.stack4.append(self.stack1[-1])
                self.stack1.pop()

            elif len(self.stack2) >= 2: # move from stack 2
                self.stack4.append(self.stack2[-1])
                self.stack2.pop()

            elif len(self.stack3) >= 2: # move from stack 3
                self.stack4.append(self.stack3[-1])
                self.stack3.pop()
        

        

if __name__ == '__main__':

    game = game()
    print('Initial: ')
    game.print_stacks()
    print('\n')
    
    game.won = False
 
    while not game.won:

        # Remove card when equal suits
        while game.isEqualSuits():
            game.removeCard()
            game.print_stacks()

        # move around cards when free slots
        while game.freePositions() > 0:
            game.moveCards()
            game.print_stacks()


            if len(game.stack1) <= 1 and len(game.stack2) <= 1 and len(game.stack3) <= 1 and len(game.stack4) <= 1:
                break

        # Draw new cards if any left in the deck
        if game.cards_drawn < 52:
            game.drawFour()
            game.print_stacks()


        if game.isWon():
            print('Holy shit you won')
            win += 1
            break

        if not game.isWon() and game.cards_drawn > 48:
            print('you lost')
            break

        

        
        


