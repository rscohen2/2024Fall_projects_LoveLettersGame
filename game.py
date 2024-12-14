"""
IS 597PR Final Project (Love Letter Card Game)

Description: Module for game class. In charge of the following behaviors:
    - manages the whole game (start & end of game)
    - manages the deck (shuffling, card distribution)
    - in charge of creating and tracking player objects
    - controls the turns
    - determines winner
    - etc.
"""
# used import as syntax (e.g., import pandas as pd) to solve the circular import problem (Mr. Weible's help)
import players as p
import cards as c
import random
from numba import jit

class Game:
    """
    This Game Class represents the game state of the Love Letter card game and manages the following behaviors:
      - Initializing and shuffling the deck
      - Managing player and their states
      - Controlling turns and enforcing game rules
      - Determining the winner (or tie) of the game

    # TODO: add valid doctest for game class
    """

    def __init__(self, players):
        self.players = players # creating player objects
        self.cards = [] # deck of cards
        self.current_player_index = 0 # tracking turn for current player
        self.tie_games = 0 # we should also track tie games (same value cards)
        self.new_game()


    @staticmethod # pycharm's suggestion
    def initialize_deck() -> list:
        """
        Initializes and shuffles the deck with the standard Love Letter composition.
        Deck consists of the following cards (number of cards):
        - Guard (5)
        - Priest (2)
        - Baron (2)
        - Handmaid (2)
        - Prince (2)
        - King (1)
        - Countess (1)
        - Princess (1)

        :return: list of shuffled cards

        >>> deck = Game.initialize_deck()
        >>> len(deck)
        16
        """
        # deck = [c.Guard()] * 5 + [c.Priest()] * 2 + [c.Baron()] * 2 + [c.Handmaid()] * 2 + [c.Prince()] * 2 + [
        #     c.King()] + [c.Countess()] + [c.Princess()]
        deck = [c.Guard() for _ in range(5)] + [c.Priest() for _ in range(2)] + [c.Baron() for _ in range(2)] + [
            c.Handmaid() for _ in range(2)] + [c.Prince() for _ in range(2)] + [c.King()] + [c.Countess()] + [
                   c.Princess()]
        random.shuffle(deck)
        return deck

    # separated the player reset function as its own method from new_game()
    def reset_players(self):
        """
        This function rests the state (players_hand, player_remaining, player_protected, and card knowledge) of all players in the game

        >>> from players import *
        >>> player_1 = Player("strategy_3", "Andrew")
        >>> player_1.players_hand = ["Baron"]
        >>> player_1.player_remaining = False
        >>> player_1.player_protected = True
        >>> game = Game([player_1])
        >>> game.reset_players()
        >>> player_1.players_hand
        []
        >>> player_1.player_remaining
        True
        >>> player_1.player_protected
        False
        """
        for player in self.players:
            player.players_hand = []
            player.player_remaining = True
            player.player_protected = False
            player.card_knowledge = {}
            for opponent in self.players:
                if opponent != player:
                    player.card_knowledge[opponent.name] = []

    def new_game(self) -> None: # moved this to class function from normal function (outside the class)
        """
        Starts a new game by resetting (shuffling) card and player status in the following sequence:
        1. Initialize new shuffled deck (initialize_deck())
        2. Reset all player status (reset_players())
        3. Deal one card to each player
        4. Reset current player index to 0 (to the first player)

        >>> from players import *
        >>> player_1 = Player("strategy_3", "Andrew")
        >>> player_2 = Player("strategy_1", "Sarah")
        >>> game = Game([player_1, player_2])
        >>> game.new_game()
        >>> len(game.cards) # checking if the dealing of one card is done
        14
        """
        self.cards = Game.initialize_deck()  # get a shuffled deck
        self.reset_players()  # Reset all player statuses

        for player in self.players:
            self.draw_a_card(player)

        self.current_player_index = 0

    # moved to instance function
    def draw_a_card(self, player):
        """
        This function draws a card from the current deck
        :param player: the current player

        >>> from players import *
        >>> from cards import *
        >>> player_1 = Player("strategy_3", "Andrew")
        >>> game = Game([player_1])
        >>> game.cards = [Guard(), King(), Prince(), Princess()] # manual deck
        >>> player_1.players_hand = []
        >>> game.draw_a_card(player_1)
        >>> len(game.cards) # checking if drawing a card results the deck to decrease one card
        3
        >>> len(player_1.players_hand) # check if the player successfully drew a card
        1
        """
        if len(player.players_hand) < 2 and self.cards: # I modified this line to ensure there are only 2 or less cards in player's hand
            card = self.cards.pop() # removes drawn card from deck (i.e., deck decreases)
            player.players_hand.append(card)

    def play_turn(self) -> None:
        """
        This function represents an individual player's turn as follows:
        1. draw a card
        2. choose card to play
        3. play the card
        4. progress to the next player

        >>> from players import *
        >>> from cards import *
        >>> player_1 = Player("strategy_1", "Sarah")
        >>> player_2 = Player("strategy_2", "Becca")
        >>> game = Game([player_1, player_2])
        >>> game.cards = [Guard(), Priest(), Princess()]
        >>> player_1.players_hand = [Guard()]
        >>> player_2.players_hand = []
        >>> player_1.player_remaining = True
        >>> player_2.player_remaining = True
        >>> game.play_turn()
        Sarah played the Guard card!
        No available opponents to target for Sarah. Turn skip.
        >>> len(game.cards) # checking if drawing a card results the deck to decrease one card
        2
        >>> game.current_player_index # check if the turn progressed to the next player
        1
        """
        # added to determine winner when deck is empty
        if not self.cards:
            print("We're out of cards! Compare cards with each other.")
            return

        player = self.players[self.current_player_index]

        # make sure to skip eliminated players
        if not player.player_remaining:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            return

        # resetting handmaid effect
        player.player_protected = False
        self.draw_a_card(player)

        selected_card = player.card_to_play()

        if not selected_card:
            print(f"{player.name} has no valid card to play.")
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            return

        # print who played which card
        print(f"{player.name} played the {selected_card.__class__.__name__} card!")

        # Got help from ChapGPT for handling the AttributeError with NoneType
        target = None
        if isinstance(selected_card, (c.Guard, c.Baron, c.King, c.Priest, c.Prince)):
            target = self.choose_opponent(player)
            if target is None:  # No valid target
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
                return

        # Guard card requires a guess
        guess = None
        if isinstance(selected_card, c.Guard) and target:
            wholeDeck = Game.initialize_deck()  # need a second variable because self.cards is updated throughout game
            guess = player.guess_card(self.get_remaining_card_list(), wholeDeck)

        selected_card.play_card(player, target, guess, game=self)
        player.remove_card(selected_card)

        # to next player (make sure the order is properly circulating (e.g., 1 -> 2 -> 3 / 2 -> 3 -> 1 / 3 -> 1 -> 2)
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0

        self.clear_eliminated_players_hands()

    # added to make sure eliminated players discard their card
    def clear_eliminated_players_hands(self):
        for player in self.players:
            if not player.player_remaining:
                player.players_hand = []  # clear eliminated player's hand


    def choose_opponent(self, current_player):
        """
        This function randomly selects opponent who are 1) remaining in the game and 2) is not protected by handmaid card
        :param current_player: The player whose turn it is
        :return: opponent player or None
        """
        available_opponent = []
        for player in self.players:
            if player != current_player and player.player_remaining and not player.player_protected and len(player.players_hand) > 0:
                available_opponent.append(player)

        if available_opponent:
            return random.choice(available_opponent)

        print(f"No available opponents to target for {current_player.name}. Turn skip.")
        return None


    # Added this function to properly get the remaining card list
    def get_remaining_card_list(self):
        """
        Function that returns cards in play (cards remaining in deck and players' hand)
        :return:
        """
        remaining_cards_list = [card.__class__.__name__ for card in self.cards]

        # Add the cards currently in each player's hand
        for player in self.players:
            if player.player_remaining:
                remaining_cards_list.extend([card.__class__.__name__ for card in player.players_hand])
        #TODO : I commented this out bc I think we DO want current hands included? -> Thank you for pointing this out. I fixed the code to make sure it contains the players' hand

        return remaining_cards_list


    @staticmethod # pycharm's suggestion
    def get_player_with_highest_card(players: list) -> tuple:
        """
        This function determines the player with the highest card
        :return: player that has the card with the highest value
        """
        highest_card_value = 0
        winners = []

        for player in players:
            if player.players_hand:
                player_card = player.players_hand[0]  # Assuming one card in hand
                if player_card.value > highest_card_value:
                    highest_card_value = player_card.value
                    winners = [player]  # Reset winners to the current player
                elif player_card.value == highest_card_value:
                    winners.append(player)  # Add to the list of winners

        return winners, highest_card_value


    def play_until_winner(self) -> str:
        """
        This function is designed to determine the winner of the game in two scenarios:
            1. Last player standing (i.e., other players got eliminated)
            2. Deck out of cards -> player with the highest value card wins
        This function also tracks the tie games

        :return: return winner
        """
        self.new_game()  # Start a new game

        # Keep playing until only one player remains or the deck is empty
        while self.count_remaining_players() > 1 and self.cards:
            self.play_turn()

        # Determine remaining players
        remaining_players = self.track_remaining_players()

        # Case 1: Only one player remains
        if len(remaining_players) == 1:
            winner = remaining_players[0].name
            print(f"Winner of this round: {winner}!")  # Announce the winner
            return winner

        # Case 2: Deck is out, compare hands
        winners, highest_card_value = Game.get_player_with_highest_card(remaining_players)

        if len(winners) == 1:
            winner = winners[0].name
            print(f"Winner of this round: {winner} with the highest card value ({highest_card_value})!")  # Announce the winner
            return winner  # Single winner
        else:
            self.tie_games += 1  # Increment tie counter
            print(f"Tie game! Players with highest card value ({highest_card_value}): {[player.name for player in winners]}")
            return "Tie"


    def count_remaining_players(self):
        """
        Check Numba helper function (count_remaining_players_numba())
        """
        player_statuses = [player.player_remaining for player in self.players]
        return count_remaining_players_numba(player_statuses)


    def track_remaining_players(self) -> list:
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


def create_players(player_names: list[str], strategies: list[str]) -> list:
    """
    Function that creates players objects based on their names
    :param player_names:
    :param strategies:
    :return: player objects
    """
    player_objects = []
    for i in range(len(player_names)):
        name = player_names[i]
        strategy = strategies[i]
        player_objects.append(p.Player(name=name, strategy=strategy))

    return player_objects


@jit(nopython=True)
def count_remaining_players_numba(player_statuses):
    """
    Count the number of players who are still in the game.

    :param player_statuses: List of booleans representing if players are still in the game.
    :return: Count of remaining players.
    """
    count = 0
    for status in player_statuses:
        if status:
            count += 1
    return count