from game import *

def run_the_sim(game):

    return game.play_until_winner()

if __name__ == '__main__':

    player_list = ["Sarah", "Becca", "Andrew", "newPlayer"]
    strategies = ["strategy_1", "strategy_2", "strategy_3", "strategy_4"]

    # Create players and a single Game instance
    players = create_players(player_list, strategies)
    game = Game(players)

    # for win and tie counts
    win_counts = {player: 0 for player in player_list}
    tie_count = 0
    num_games = 1000

    # Run simulations
    for i in range(0, num_games):
        winner = run_the_sim(game)

        if winner in win_counts:
            win_counts[winner] += 1
        elif winner == "Tie":
            tie_count += 1

    # Display results
    print("####################################################")
    print(f"################ Simulation Results: ###############")
    print("####################################################")
    for player, count in win_counts.items():
        print(f"{player} wins: {count}")
    print(f"Tie games: {tie_count}")


    #TODO: instead of just winner list count number of times each player wins and graph stat convergence etc

    # # This is a new test execution code
    # # this player creation part changed due to the create_players() function (moved outside the game class)
    # player_list = ["Sarah", "Becca", "Andrew"]
    # strategies = ["strategy_1", "strategy_2", "strategy_3"]
    # players = create_players(player_list, strategies)
    #
    # game = Game(players)
    #
    # # this is just a simple execution code to see if game.py is working (not a monte carlo)
    #
    # Andrew_win_count = 0
    # Sarah_win_count = 0
    # Becca_win_count = 0
    # for i in range(1, 1000):
    #     winner = run_the_sim(Sarah_win_count, Becca_win_count, Andrew_win_count)
    #     if winner == "Sarah":
    #         Sarah_win_count += 1
    #     if winner == "Becca":
    #         Becca_win_count += 1
    #     if winner == "Andrew":
    #         Andrew_win_count += 1
    # print(f"Sarah_wins: {Sarah_win_count} Andrew_wins: {Andrew_win_count}, Becca_wins: {Becca_win_count}")