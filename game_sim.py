from game import *

if __name__ == '__main__':

    # This is a new test execution code
    # this player creation part changed due to the create_players() function (moved outside the game class)
    player_list = ["Sarah", "Becca", "Andrew"]
    strategies = ["strategy_1", "strategy_2", "strategy_3"]
    players = create_players(player_list, strategies)

    game = Game(players)

    # this is just a simple execution code to see if game.py is working (not a monte carlo)

    Andrew_win_count = 0
    Sarah_win_count = 0
    Becca_win_count = 0
    for i in range(1, 1000000):
        winner = run_the_sim(Sarah_win_count, Becca_win_count, Andrew_win_count)
        if winner == "Sarah":
            Sarah_win_count += 1
        if winner == "Becca":
            Becca_win_count += 1
        if winner == "Andrew":
            Andrew_win_count += 1
    print(f"Sarah_wins: {Sarah_win_count} Andrew_wins: {Andrew_win_count},'Becca_wins: {Becca_win_count}")

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
