from game import *

if __name__ == '__main__':

    # This is a new test execution code
    # this player creation part changed due to the create_players() function (moved outside the game class)
    player_list = ["Sarah", "Becca", "Andrew"]
    strategies = ["strategy_1", "strategy_2", "strategy_3"]
    players = create_players(player_list, strategies)

    game = Game(players)

    winner = game.play_until_winner()

    if winner:
        print(f"{winner.name} wins!")
    else:
        print("\nSomething went wrong with the code")

    # The below execution code is the original version
    # # control = Player('control')
    # players = [Player('Strategy1', 'Sarah'), Player('Strategy2','Becca'), Player('Strategy3','Andrew')]
    # game = Game(players)
    #
    # winners = []
    #
    # for i in range(1,10000):
    #     winner = Game.game_play_until_winner()
    #     winners.append(winner)

    #TODO: instead of just winner list count number of times each player wins and graph stat convergence etc
