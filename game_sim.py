
import random
import Counter
from cards import *
import players
import game

#check if there is already a clear winner before implementing a round
def game_play_until_winner():
    if len(players) != 1 or len(cards) != 0: #if no winner yet
        round()
    #recursion of rounds until a winner is identified for that game
    else:
        winner = winner()
    return winner

if __name__ == '__main__':
    # control = Player('control')
    players = [Player('Strategy1', 'Sarah'), Player('Strategy2','Becca'), Player('Strategy3','Andrew')]
    game = Game(players)

    winners = []

    for i in range(1,10000):
        winner = game_play_until_winner()
        winners.append(winner)

    #TODO: instead of just winner list count number of times each player wins and graph stat convergence etc
