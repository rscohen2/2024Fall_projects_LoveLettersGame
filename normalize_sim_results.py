import matplotlib.pyplot as plt
from game import *


def run_the_sim(game):
    return game.play_until_winner()

player_list = ["Player1", "Player2", "Player3", "Player4"]
strategies = ["strategy_1", "strategy_2", "strategy_3", "strategy_4"]

players = create_players(player_list, strategies)
game = Game(players)

win_counts = {player: 0 for player in player_list}
tie_count = 0
results = []

def normalize(wins, num_games):
    return wins/num_games

normalized_results = []

def run_normalization(player_counts, results):
    for player_count in player_counts.items():
        normalized_results.append(normalize(player_count[1], len(results)))
    return normalized_results


# Run for 10,000 simulations

def run_sim(num_games):
    # Reset for the new sims
    game = Game(players)
    win_counts = {player: 0 for player in player_list}
    tie_count = 0
    results = []

    for i in range(0, num_games):
        winner = run_the_sim(game)
        if winner in win_counts:
            win_counts[winner] += 1
            results.append(winner)
        elif winner == "Tie":
            tie_count += 1
            results.append("Tie")
    player_counts = {player: results.count(player) for player in player_list}
    return player_counts, results


player_counts, results = run_sim(1000)
# print(player_counts, results)

normalized_results = run_normalization(player_counts, results)

print(normalized_results)


def run_multiple_sims(num_runs):
    player_counts, results = run_sim(num_runs)
    # print(player_counts, results)

    normalized_results = run_normalization(player_counts, results)
    return normalized_results


player1_results = []
player2_results = []
player3_results = []
player4_results = []
ties_results = []


def aggregate_normalized_result(normalized_result):
        player1 = int(normalized_result[0])
        player2 = int(normalized_result[1])
        player3 = int(normalized_result[2])
        player4 = int(normalized_result[3])
        # ties = int(normalized_result[4])
        player1_results.append(player1)
        player2_results.append(player2)
        player3_results.append(player3)
        player4_results.append(player4)
        player_results = (player1_results, player2_results, player3_results, player4_results)
        # ties_results.append(ties)
        return player_results

def sum_player_results(player_results):
    player_result_sum = 0
    for i in range(len(player_results)):
        player_result = player_results[i]
        player_result_sum += int(player_result[0])
    return player_result_sum


normalized_results = []

import pandas as pd

df = pd.DataFrame()

df['i'] = ""
df['normalized_result'] = ""

for i in range(1, 100):
    normalized_result = run_multiple_sims(i)
    aggregated_normalized_result = aggregate_normalized_result(normalized_result)
    player_results_sum = sum_player_results(aggregated_normalized_result)
    # normalized_results.append(normalized_result)
    df.at[i,'i'] = i
    df.at[i,'normalized_result'] = str(player_results_sum)



# print(normalized_results)


