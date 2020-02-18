from game import game
from tqdm import tqdm


num_simulations = 1000000
wins = 0

for i in tqdm(range(num_simulations)):
    the_game = game()
    
 
    while not the_game.isWon():

        # Remove card when equal suits
        while the_game.isEqualSuits():
            the_game.removeCard()

        # move around cards when free slots
        while the_game.freePositions() > 0:
            the_game.moveCards()

            if len(the_game.stack1) <= 1 and len(the_game.stack2) <= 1 and len(the_game.stack3) <= 1 and len(the_game.stack4) <= 1:
                break

        # Draw new cards if any left in the deck
        if the_game.cards_drawn < 52:
            the_game.drawFour()


        if the_game.isWon():
            print('Holy shit, you won')
            the_game.print_stacks()
            wins += 1
            break

        if the_game.cards_drawn == 52 and not the_game.isEqualSuits():
            #the_game.print_stacks()
            #print('\nyou lost')
            break

print("{:d} wins out of {:d} simulations".format(wins,num_simulations))
print(" percentage = {:.10f}".format( wins/num_simulations ))