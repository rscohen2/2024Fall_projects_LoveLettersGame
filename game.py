"""
IS 597PR Final Project (Love Letter Card Game)

Description: Module for game class. In charge of the following behaviors:
    - manages the whole game (start & end of game)
    - manages the deck (shuffling, card distribution)
    - in charge of creating and tracking player objects
    - controls the turns
    - determines winner
    - etc.

Remarks: I try to leave comments next to the actual codes, but I also leave important notes here

    1. I'm moving most of the functions inside the class as an instance method
        --> sorry, this is simply just because I found this more easier
    2. I'm trying to merge or even get rid of unnecessary functions
    3. Parts that I thought need significant attention is commented with a TODO
        --> this doesn't mean that all the TODOs are urgent
    4. Needs more work based on each others' class logic
        --> for instance, I might use or need attributes and/or functions from different classes
    5. I think I'm about 60% done with my rough draft (not FINAL DRAFT) as of 6:30pm Nov.19 Tuesday
"""

from players import *
from cards import *
import random
from collections import Counter

class Game:

    current_deck = None
    cards = None
    card_played = None
    cards_in_play = []
    players = None
    cards_played = None #  not sure about this

    def __init__(self, players):
        self.players = self.create_players(players) # creating player objects
        self.cards = [] # deck of cards
        self.remaining_cards = Counter() # Track remaining cards
        # self.cards = current_deck(self.cards, self.cards_drawn)
        self.current_player_index = 0 # tracking turn for current player
        self.new_game()
        # self.cards_played = [] # tracking played cards
        # self.cards_in_play = []

    def new_game(self): # moved this to class function from normal function (outside the class)
        """
        Starts a new game by resetting (shuffling) card and player status
        :return: cards
        """
        # Shuffling the deck (deck object obtained)
        self.cards = [Guard()] * 5 + [Priest()] * 2 + [Baron()] * 2 + [Handmaid()] * 2 + [Prince()] * 2 + [King()] + [Countess()] + [Princess()]
        random.shuffle(self.cards)

        # this part keeps track of the remaining cards
        self.remaining_cards = Counter()
        for card in self.cards:
            self.remaining_cards[card.__class__.__name__] += 1

        # resetting player status
        for player in self.players:
            player.players_hand = [] # empty player's hand
            player.card_knowledge = {} # I changed this to dictionary (it is None in the players class module)
            player.player_remaining = True   # This property isn't yet implemented in player class module
            player.player_protected = False  # This property isn't yet implemented in player class module


    def create_players(self, players_names: list[str]) -> list[Player]:
        """
        Function that creates players objects based on their names
        :param players_names:
        :return:
        # TODO: write a DocTest
        """
        strategies = ["strategy_1", "strategy_2", "strategy_3"]
        player_objects = []
        for i, name in enumerate(players_names):
            player = Player(name = name, strategy = strategies[i])
            player_objects.append(player)

        return player_objects


    def play_turn(self):
        """
        This function represents an individual player's turn as follows:
        1. draw a card
        2. choose card to play
        3. play the card
        :return:
        """
        player = self.players[self.current_player_index]
        if player.player_remaining and not player.player_protected: # TODO: need these two player class attributes (will be implemented soon)
            self.draw_a_card(player) # draw a card
            card_index = player.card_to_play() # TODO: not sure if player.card_to_play() is accessible (maybe need a card_to_play function)
            target = self.choose_opponent(player) # randomly choose opponent
            player.play_card(card_index, target) # play the chosen card TODO: not sure if player.play_card() is accessible maybe need a play_card function

        # to next player
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0


    # I sort of merged and modified the original game_play_until_winner() and winner() into one function
    # Also I modified it as an instance function from class function
    def play_until_winner(self):
        """

        :return:
        """
        self.new_game() # start a new game (reshuffle deck and restart player status)

        # deal one card each for players
        for player in self.players:
            self.draw_a_card(player)

        # TODO: complete the winner logic below
        # play until either 1.one player standing or 2.deck gets empty
        # if len(Game.players) != 1 or len(Game.cards) != 0:  # if no winner yet
        #     round()
        #
        # # recursion of rounds until a winner is identified for that game
        # else:
        #     winner = Game.winner()

            pass


    # moved to instance function
    def draw_a_card(self, player):
        """
        Draws a card randomly from the current deck
        :param player:
        :return:
        """
        if self.cards: # this is the deck of cards
            card = self.cards.pop() # removes drawn card from deck (i.e., deck decreases)
            player.players_hand.append(card)


    # moved to instance function
    def choose_opponent(self, current_player):
        available_opponent = []
        for player in self.players:
            if player != current_player and player.player_remaining and not player.player_protected:
                available_opponent.append(player)

        if available_opponent:
            return random.choice(available_opponent) # TODO: maybe we can modify this later when we are going to consider card knowledge?

        return None


    # @classmethod
    # def game_play_until_winner(cls):
    #     if len(Game.players) != 1 or len(Game.cards) != 0:  # if no winner yet
    #         round()
    #     # recursion of rounds until a winner is identified for that game
    #     else:
    #         winner = Game.winner()
    #     return winner
    #
    # @classmethod
    # def winner(cls):
    #     if len(Player.players) == 1:
    #         return Player.players[0]
    #
    #     elif len(Game.current_deck) == 0:
    #         ending_hands = {}
    #         for player in Player.players:
    #             ending_hands[player].append(Player.players_hand.card_value)
    #
    #             # TODO : find correct syntax for adding to dict, its not the above pseudo code
    #             current_max_value = 0
    #             for player in ending_hands:
    #                 if player.players_hand.card_value > current_max_value:
    #                     current_max_value = player.players_hand.card_value
    #                 # can we access who that player is from the class structure above
    #                 winner = current_max_value
    #                 return winner


# def deal_cards():
#     """
#     Deals cards randomly to each player prior to the first round
#     :return:
#     """
#     Player.players_hand = []
#     card_drawn = draw_a_card(cards_drawn, cards)
#     Player1.players_hand.append(card_drawn)
#
#     # Player2.players_hand = []
#     # card_drawn = draw_a_card(cards_drawn, cards)
#     # Player2.players_hand.append(card_drawn)
#     #
#     # Player3.players_hand = []
#     # card_drawn = draw_a_card(cards_drawn, cards)
#     # Player3.players_hand.append(card_drawn)


"""
I'm currently trying to reduce the functions below. I believe some functions can be merged or even unnecessary.
"""

def current_deck(cards, cards_drawn):
    """
    keep track of the current deck, removing cards_played (discard pile) and cards_drawn (currently in players hands)
    :param cards:
    :param cards_drawn:
    :return: cards that are in play
    """
    for card in cards:
        if card in cards_drawn:
            cards.remove(card)
    return cards

def players_hand(player): # Isn't this in Player Class?
    """
    keep track of the players current hand
    :param player:
    :return:
    """
    players_hand = []
    return players_hand

# def draw_a_card(cards_drawn, cards, players_hand):
#     """
#     Draws a card randomly from the current deck
#     :param cards_drawn:
#     :param cards:
#     :return: card that is drawn
#     """
#     i = random.randint(0, 15)
#     card_drawn = cards[i]
#     cards_drawn.append(card_drawn)
#     players_hand.append(card_drawn)
#     return card_drawn, cards_drawn, players_hand


# def deal_cards(self):
#     """
#     Deals cards randomly to each player prior to the first round
#     :return:
#     """
#     for player in self.players:
#         player.players_hand = []
#         card_drawn = draw_a_card(cards_drawn, cards)
#         player.players_hand.append(card_drawn)

# def play_card():
#     """
#
#     :return:
#     """


def player_is_out_of_the_round(player_out, players):
    """
    removes a player who is out of the round from the players list, and returns the players who are still in that round
    :return: players who are still in the round
    """
    players = players.remove(player_out)
    return players


def list_opponents(players, current_player):
    # TODO: check if opponent has handmaid card, then remove them from opponents list?

    opponents = players.remove(current_player)
    return opponents

# def choose_opponent(opponents, opponent_card_in_play):
#     # TODO: check if opponent has handmaid card, then remove them from opponents list?
#     for opponent in opponents:
#         if opponent_card_in_play == 'Handmaid':
#     # TODO: implement opponent_card_in_play somehow in the player class??
#             opponents.remove(opponent)
#     opponent = random.choice(opponents)
#     return opponent

def update_cards_played(card_played, cards_played):
    cards_played.append(card_played)
    return cards_played, cards_played

def clear_cards_in_play(cards_in_play):
    cards_in_play = []
    return cards_in_play

def player_turn(player, Player):
    card_drawn = draw_a_card(cards_drawn, cards)
    player.players_hand.append(card_drawn)
    move = player.strategy(self, opponents_hand)
    return move


def round():
    for player in players:
        player_turn(player, player.strategy)


# def winner():
#     if len(players) == 1:
#         return players[0]
#
#     elif len(current_deck) = 0:
#         ending_hands = {}
#
#         # players[0] > players [1]
#         for player in players:
#             ending_hands.append(player: player.players_hand.card_value)
#             #TODO : find correct syntax for adding to dict, its not the above pseudo code
#             current_max_value = 0
#             for player in ending_hands:
#                 if player.players_hand.card_value > current_max_value:
#                 current_max_value = player.players_hand.card_value
#                 #can we access who that player is from the class structure above
#                 winner = current_max_value
#                 return winner

# #check if there is already a clear winner before implementing a round
# def game_play_until_winner():
#     if len(players) != 1 or len(cards) != 0: #if no winner yet
#         round()
#     #recursion of rounds until a winner is identified for that game
#     else:
#         winner = winner()
#     return winner