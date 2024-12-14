from game import *

def run_the_sim(game):
    print("========================Starting a new game!========================")
    return game.play_until_winner()

if __name__ == '__main__':

    player_list = ["Sarah", "Becca", "Andrew", "newPlayer", "player5"]
    strategies = ["strategy_1", "strategy_2", "strategy_3", "strategy_4", "strategy_5"]

    # for win and tie counts
    win_counts = {player: 0 for player in player_list}
    tie_count = 0
    num_games = 10000

    # Run simulations
    for i in range(0, num_games):
        players = create_players(player_list, strategies)
        random.shuffle(players) # shuffle order of players
        game = Game(players)

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