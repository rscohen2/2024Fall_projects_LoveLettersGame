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
    6. Rough draft finished (11:35 Nov.20)
        --> there are still parts that need modification
        --> currently have a import issue in the test execution code at the bottom (not sure how to handle this yet)
"""

from players import *
from cards import *
import random
from collections import Counter

class Game:

    # TODO: I'm not sure if we need these class attributes (I feel like it is redundant)
    # current_deck = None
    # cards = None
    card_played = None
    cards_in_play = []
    players = None
    cards_played = None #  not sure about this

    def __init__(self, players):
        self.players = self.create_players(players) # creating player objects
        self.cards = [] # deck of cards
        self.remaining_cards = Counter() # Track remaining cards
        self.current_player_index = 0 # tracking turn for current player
        self.new_game()
        self.cards_played = [] # tracking played cards TODO: isn't this redundant with player.card_played?
        self.cards_in_play = [] # tracking cards currently in play TODO: not sure if we need this (maybe might need it when we are going to consider card memory/knowledge?)


    def new_game(self) -> None: # moved this to class function from normal function (outside the class)
        """
        Starts a new game by resetting (shuffling) card and player status
        :return: None
        """
        # Shuffling the deck (deck object obtained)
        self.cards = [Guard()] * 5 + [Priest()] * 2 + [Baron()] * 2 + [Handmaid()] * 2 + [Prince()] * 2 + [King()] + [Countess()] + [Princess()]
        random.shuffle(self.cards)

        # this part keeps track of the remaining cards
        self.remaining_cards = Counter()
        for card in self.cards: # card is each card (subclass) object
            self.remaining_cards[card.__class__.__name__] += 1 # didn't know how to access subclass names from other class object (referred to https://stackoverflow.com/questions/3314627/get-subclass-name)

        # resetting player status
        for player in self.players:
            player.players_hand = [] # empty player's hand
            # player.card_knowledge = {} # I changed this to dictionary (it is None in the players class module) TODO: we don't need this yet
            player.player_remaining = True   # reset all players to be remained in the game
            player.player_protected = False  # reset the protection effect (via Handmaid card)
            player.card_played = None # reset played card TODO: should this be an empty list or None?


    def create_players(self, players_names: list[str]) -> list[Player]:
        """
        Function that creates players objects based on their names
        :param players_names:
        :return: player objects
        """
        strategies = ["strategy_1", "strategy_2", "strategy_3"]
        player_objects = []
        for i, name in enumerate(players_names):
            player = Player(name = name, strategy = strategies[i])
            player_objects.append(player)

        return player_objects


    def play_turn(self) -> None:
        """
        This function represents an individual player's turn as follows:
        1. draw a card
        2. choose card to play
        3. play the card
        4. to the next player
        :return: None
        """
        player = self.players[self.current_player_index]
        if player.player_remaining and not player.player_protected:
            self.draw_a_card(player) # draw a card
            selected_card = player.card_to_play() # TODO: I changed the variable name card_index to selected_card since it seemed misleading
            target = self.choose_opponent(player) # randomly choose opponent
            player.play_card(selected_card, target) # play the chosen card

        # to next player (make sure the order is properly circulating (e.g., 1 -> 2 -> 3 / 2 -> 3 -> 1 / 3 -> 1 -> 2)
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0


    # I sort of merged and modified the original game_play_until_winner() and winner() into one function
    # Also I modified it as an instance function from class function
    # I didn't use the dictionary idea since I thought keeping track of remaining players list seemed more simple (implemented in self.track_remaining_players() function)
    def play_until_winner(self) -> Player:
        """
        This function is designed to determine the winner of the game in two scenarios:
            1. Last player standing (i.e., other players got eliminated)
            2. Deck out of cards -> player with highest value card wins

        :return: return winner
        """
        self.new_game() # start a new game (reshuffle deck and restart player status)

        # deal one card each for players
        for player in self.players:
            self.draw_a_card(player)

        # keep playing turns until there is only one player standing OR until the deck is empty
        while len(self.track_remaining_players()) > 1 and len(self.cards) > 0:
            self.play_turn()

        # determine winner (2 cases)
        remaining_players = self.track_remaining_players()

        # 1. last player standing
        if len(remaining_players) == 1:
            return remaining_players[0]

        # 2. player with highest card
        return self.get_player_with_highest_card(remaining_players)


    # moved to instance function
    def draw_a_card(self, player) -> None:
        """
        This function draws a card from the current deck
        :param player:
        :return: None
        """
        if self.cards: # this is the deck of cards
            card = self.cards.pop() # removes drawn card from deck (i.e., deck decreases)
            player.players_hand.append(card)


    # moved to instance function
    def choose_opponent(self, current_player: Player): # TODO: not sure how to type annotate this function (specifically the return value)
        """
        This function randomly selects opponent who are 1) remaining in the game and 2) is not protected by handmaid card
        :param current_player:
        :return: opponent player or None
        """
        available_opponent = []
        for player in self.players:
            if player != current_player and player.player_remaining and not player.player_protected:
                available_opponent.append(player)

        if available_opponent:
            return random.choice(available_opponent) # TODO: maybe we can modify this later when we are going to consider card knowledge?

        return None


    def track_remaining_players(self) -> list[Player]:
        """
        This function tracks down the remaining players in the game
        :param self
        :return: list of remaining players
        """
        remaining_players = []
        for player in self.players:
            if player.player_remaining:
                remaining_players.append(player)

        return remaining_players


    # just modified a bit of our original winner() function
    def get_player_with_highest_card(self, players: list[Player]) -> Player:
        """
        This function determines the player with the highest card
        :return: player that has the card with the highest value
        """
        player_with_highest_card = None
        highest_card_value = 0
        for player in self.players:
            if player.players_hand and player.players_hand[0].value > highest_card_value: # TODO: not sure if this is how accessing the card values works but I'm going to believe pycharm's autocompletion for now haha
                highest_card_value = player.players_hand[0].value
                player_with_highest_card = player

        return player_with_highest_card

# this is just a simple execution code to see if game.py is working (not a monte carlo)
if __name__ == "__main__":
    player_names = [Player('playStrategy1', 'Sarah'), Player('playStrategy2','Becca'), Player('playStrategy3','Andrew')]
    game = Game(player_names)

    winner = game.play_until_winner()

    if winner:
        print(f"{winner.name} wins!")
    else:
        print("\nSomething went wrong with the code")

    # TODO: Currently getting the following error:
    # ImportError: cannot import name 'choose_opponent' from partially initialized module 'game' (most likely due to a circular import)
    # (C:\Users\namdi\PycharmProjects\IS597\2024Fall_projects_LoveLettersGame\game.py)
    # I think this has to do with the game class and player class modules getting into a circular import