
import random
# import Counter
from cards import *
from players import *
from game import *

if __name__ == '__main__':
    # control = Player('control')
    players = [Player('Strategy1', 'Sarah'), Player('Strategy2','Becca'), Player('Strategy3','Andrew')]
    game = Game(players)

    winners = []

    for i in range(1,10000):
        winner = game_play_until_winner()
        winners.append(winner)

    #TODO: instead of just winner list count number of times each player wins and graph stat convergence etc
