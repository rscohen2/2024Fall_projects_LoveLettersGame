from game import *

def run_the_sim(game):
    print("========================Starting a new game!========================")
    return game.play_until_winner()

# this is our original setup (fixed order + different strategy per player)
def experiment_fix_order(player_list, strategies, num_games):
    """
    Run the vanilla experiment where the player order remains fixed, and each player has their own strategy.
    """
    # Create players with the fixed order
    players = create_players(player_list, strategies)
    game = Game(players)

    # Initialize result tracking
    win_counts = {player: 0 for player in player_list}
    tie_count = 0

    for _ in range(num_games):
        winner = run_the_sim(game)

        # Track results
        if winner in win_counts:
            win_counts[winner] += 1
        elif winner == "Tie":
            tie_count += 1

    # Display results
    print("####################################################")
    print(f"################ Simulation Results: ###############")
    print("####################################################")
    print("Remarks: Player order was fixed for each game.")
    print("----------------------------------------------------")
    for player, count in win_counts.items():
        print(f"{player} wins: {count}")
    print(f"Tie games: {tie_count}")

    return win_counts, tie_count


def experiment_random_order(player_list, strategies, num_games):
    """
    Run the experiment where the player order is randomized for each game.
    """
    win_counts = {player: 0 for player in player_list}
    tie_count = 0

    for _ in range(num_games):
        players = create_players(player_list, strategies) # randomize player order

        random.shuffle(players)

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
    print("Remarks: Player order was randomized for each game.")
    print("----------------------------------------------------")
    for player, count in win_counts.items():
        print(f"{player} wins: {count}")
    print(f"Tie games: {tie_count}")

    return win_counts, tie_count


def experiment_fix_order_same_strategy(player_list, strategy, num_games):
    """
    Run the experiment where all players use the same strategy and the order does NOT change.
    """
    strategies = [strategy] * len(player_list)
    win_counts = {player: 0 for player in player_list}
    tie_count = 0

    players = create_players(player_list, strategies)

    for _ in range(num_games):
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
    print("Remarks: Player order was fixed for each game. Also, all players had the same strategy.")
    print("----------------------------------------------------")
    for player, count in win_counts.items():
        print(f"{player} wins: {count}")
    print(f"Tie games: {tie_count}")

    return win_counts, tie_count


if __name__ == '__main__':

    # Modify the below parameters to process different types of simulations (experiments)
    player_list = ["Sarah", "Becca", "Andrew", "newPlayer", "player5"]
    num_games = 10000 # set number of simulations
    experiment_type = 0      # Options: {"Experiment_1": 0, "Experiment_2": 1, "Experiment_3": 2}

    if experiment_type == 0:
        # Experiment 1: Vanilla Experiment (fixed order + different strategy)
        strategies = ["strategy_1", "strategy_2", "strategy_3", "strategy_4", "strategy_5"]
        experiment_fix_order(player_list, strategies, num_games)

    elif experiment_type == 1:
        # Experiment 2: Randomized Order
        strategies = ["strategy_1", "strategy_2", "strategy_3", "strategy_4", "strategy_5"]
        experiment_random_order(player_list, strategies, num_games)

    elif experiment_type == 2:
        # Experiment 3: Fixed Order with the Same Strategy
        strategy = "strategy_1" # pick one strategy (strategy_1, strategy_2, strategy_3, strategy_4, strategy_5)
        experiment_fix_order_same_strategy(player_list, strategy, num_games)

    else:
        print("Invalid experiment type. Please choose from 0, 1, and 2.")
