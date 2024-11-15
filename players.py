# test
from random import random


class Player:
    """A competitor in the game."""

    player_count = 0  # Initialize count of all players.
    all_players = []  # automatically track all players

    def __init__(self, strategy, name):
        Player.player_count += 1
        Player.all_players.append(self)


        self.name = name
        self.strategy = strategy
        # self.randmax = None
        self.players_hand = []
        # track player stats:
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.opponents = Counter()
        self.choices = Counter()
        self.player = None
        self.players_hand = None


    #TODO : incoporate the strategies into one function?

    def strategy_1(self, opponents_hand):
        if 'Guard' in self.players_hand:
            opponent = choose_opponent(self.opponents, opponent_card_in_play)
            opponents_hand = players_hand(opponent)
            guess = cards.unique().count().max()  # guess the most frequent card left in deck?
            move = Guard.play_card(Guard.self, guess, opponents_hand, opponent)
            return move
        #        return players_hand, opponents_hand, cards_in_play, cards_played
        else:
            i = random.randint(0, 2)
            card_to_play = Player1.players_hand[i]
            move = play_card(card_to_play, opponents_hand, opponent)
            return move

    def strategy_2(self):

        if 'Guard' in self.players_hand:
                    opponent = choose_opponent(self.opponents, opponent_card_in_play)
                    opponents_hand = players_hand(opponent)
                    guess = 'Princess' #guess the most frequent card left in deck?
                    move = Guard.play_card(Guard.self, guess, opponents_hand, opponent)
                    return move
                #        return players_hand, opponents_hand, cards_in_play, cards_played
                else:
                    i = random.randint(0, 2)
                    card_to_play = Player2.players_hand[i]
                    move = play_card(card_to_play, opponents_hand, opponent)
                    return move
                return

    def strategy_3(self):
        i = random.randint(0, 2)
                card_to_play = Player.players_hand[i]
                move = play_card(card_to_play, opponents_hand, opponent)
                return move

    def check_hand_for_countess(self, cards_played):
        if 'Countess' in players_hand:
            if 'King' or 'Prince' in players_hand:
                move = Countess.play_card(Countess.self, self.player, players, cards_played)
                return move


# class Player1(Player):
#     #strat for player 1
#     # def __init__(self, self.strategy, players_hand = None):
#     def __init__(self, strategy):
#         super().__init__(strategy)
#         self.strategy = self.strategy_1
#         self.player = 'player1'
#         self.opponents = ['player2', 'player3']
#         self.card_knowledge = {'player2':[], 'player3':[]}
#         self.players_hand = []
# # def strategy_1(self, opponents_hand):
# #     if 'Guard' in self.players_hand:
# #         opponent = choose_opponent(self.opponents, opponent_card_in_play)
# #         opponents_hand = players_hand(opponent)
# #         guess = cards.unique().count().max() #guess the most frequent card left in deck?
# #         move = Guard.play_card(Guard.self, guess, opponents_hand, opponent)
# #         return move
# #     #        return players_hand, opponents_hand, cards_in_play, cards_played
# #     else:
# #         i = random.randint(0, 2)
# #         card_to_play = Player1.players_hand[i]
# #         move = play_card(card_to_play, opponents_hand, opponent)
# #         return move
#
#
#
# class Player2(Player):
#     def __init__(self, strategy):
#         super().__init__(strategy)
#         self.strategy = strategy_2
#         self.players_hand = []
#         self.player = 'player2'
#         self.opponents = ['player1', 'player3']
#         self.card_knowledge = {'player1':[], 'player3':[]}
#
#     def strategy_2(self):
#         if 'Guard' in self.players_hand:
#             opponent = choose_opponent(self.opponents, opponent_card_in_play)
#             opponents_hand = players_hand(opponent)
#             guess = 'Princess' #guess the most frequent card left in deck?
#             move = Guard.play_card(Guard.self, guess, opponents_hand, opponent)
#             return move
#         #        return players_hand, opponents_hand, cards_in_play, cards_played
#         else:
#             i = random.randint(0, 2)
#             card_to_play = Player2.players_hand[i]
#             move = play_card(card_to_play, opponents_hand, opponent)
#             return move
#         return
#
#     pass
#
# class Player3(Player):
#
#     def __init__(self, strategy):
#         super().__init__(strategy)
#         self.strategy = self.strategy_3
#         self.players_hand = self.players_hand
#         self.player = 'player3'
#         self.opponents = ['player1', 'player2']
#         self.card_knowledge = {'player1':[], 'player2':[]}
#
#     def strategy_3(self):
#         i = random.randint(0, 2)
#         card_to_play = Player3.players_hand[i]
#         move = play_card(card_to_play, opponents_hand, opponent)
#         return move
#
#
#         # pre-calculate and store these values for randomization of turns:
#         # r, p, s = self.strategy
#         # self.randmax = r + p + s
