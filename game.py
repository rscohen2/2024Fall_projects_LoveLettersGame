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
    7. (241121_Thursday) moved create_player outside the game class (Mr. Weible's recommendation)
        --> accordingly, the self.players property also changed
"""
# from random import randint

# TODO: used import as syntax (e.g., import pandas as pd) to solve the circular import problem (Mr. Weible's help)
import players as p
import cards as c
import random
from collections import Counter


class Game:

    def __init__(self, players):
        self.players = players # creating player objects
        self.cards = [] # deck of cards
        self.remaining_cards = Counter() # Track remaining cards
        self.current_player_index = 0 # tracking turn for current player
        self.tie_games = 0 # we should also track tie games (same value cards)
        self.new_game()
        # self.cards_played = [] # tracking played cards TODO: isn't this redundant with player.card_played?
        # self.cards_in_play = [] # tracking cards currently in play TODO: not sure if we need this (maybe might need it when we are going to consider card memory/knowledge?)
        # TODO: another property like self.card (for discarded pile) -> this will be even helpful for debugging purposes -> cards_played can be used for this (just give it another name)

    @staticmethod # pycharm's suggestion
    def initialize_deck() -> list:
        """
        Initializes and shuffles the deck with the standard Love Letter composition.
        Returns the shuffled deck.
        """
        deck = [c.Guard()] * 5 + [c.Priest()] * 2 + [c.Baron()] * 2 + [c.Handmaid()] * 2 + [c.Prince()] * 2 + [
            c.King()] + [c.Countess()] + [c.Princess()]
        random.shuffle(deck)
        return deck

    # added a new instance method (separated the player reset function as its own method from new_game())
    def reset_players(self):
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
        Starts a new game by resetting (shuffling) card and player status
        :return: None
        """
        print("========================Starting a new game!========================")
        self.cards = Game.initialize_deck()  # get a shuffled deck

        # this part keeps track of the remaining cards
        self.remaining_cards = Counter()
        for card in self.cards: # card is each card (subclass) object
            #card_name = card.__class__.__name__  # didn't know how to access subclass names from other class object (referred to https://stackoverflow.com/questions/3314627/get-subclass-name)
            card_name = card
            self.remaining_cards[card_name] += 1

        self.reset_players()  # Reset all player statuses

        for player in self.players:
            self.draw_a_card(player)

        self.current_player_index = 0


    # moved to instance function
    def draw_a_card(self, player):
        """
        This function draws a card from the current deck
        :param player:
        :return: None
        """
        if len(player.players_hand) < 2 and self.cards: # I modified this line to ensure there are only 2 or less cards in player's hand
            card = self.cards.pop() # removes drawn card from deck (i.e., deck decreases)
            player.players_hand.append(card)

            card_name = card.__class__.__name__
            if self.remaining_cards[card_name] > 0:
                self.remaining_cards[card_name] -= 1


    def play_turn(self) -> None:
        """
        This function represents an individual player's turn as follows:
        1. draw a card
        2. choose card to play
        3. play the card
        4. to the next player
        :return: None

        """
        # added to determine winner when deck is empty (the previous version kept returning an error when a player tried to guess a card when the deck is already empty)
        if not self.cards:
            print("We're out of cards! Compare cards with each other.")
            return

        player = self.players[self.current_player_index]

        #if player.player_remaining and not player.player_protected:
        # make sure to skip eliminated players
        if not player.player_remaining:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            return

        # resetting handmaid effect
        player.player_protected = False
        self.draw_a_card(player)

        selected_card = player.card_to_play() # TODO: I changed the variable name card_index to selected_card since it seemed misleading

        if not selected_card:
            print(f"{player.name} has no valid card to play.")
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            return

        # print who played which card
        print(f"{player.name} played the {selected_card.__class__.__name__} card!")

        # choose opponent (guard, baron, king, priest, prince)
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

        # if target is None and not isinstance(selected_card, (c.Handmaid, c.Countess, c.Princess)):
        #     print(f"No valid target for {player.name}. Turn skipped.")
        #     self.current_player_index = (self.current_player_index + 1) % len(self.players)
        #     return

        # selected_card.play_card(player, target, guess)
        selected_card.play_card(player, target, guess, game=self)
        player.remove_card(selected_card)

        # to next player (make sure the order is properly circulating (e.g., 1 -> 2 -> 3 / 2 -> 3 -> 1 / 3 -> 1 -> 2)
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0


    # moved to instance function
    # this might have to be in players class
    def choose_opponent(self, current_player):
        """
        This function randomly selects opponent who are 1) remaining in the game and 2) is not protected by handmaid card
        :param current_player:
        :return: opponent player or None
        """
        available_opponent = []
        for player in self.players:
            # if player != current_player and player.player_remaining and not player.player_protected:
            if player != current_player and player.player_remaining and not player.player_protected and len(player.players_hand) > 0:
                available_opponent.append(player)

        # if len(available_opponent) > 0:
        if available_opponent:
            return random.choice(available_opponent)

        print(f"No available opponents to target for {current_player.name}. Turn skip.")
        return None


    # Added this function to properly get the remaining card list
    def get_remaining_card_list(self):
        remaining_cards = list(self.remaining_cards.elements())
        for player in self.players:
            if player.player_remaining:
                for card in player.players_hand:
                    remaining_cards.append(card)

        return remaining_cards

    # just modified a bit of our original winner() function
    # players should be in a different name
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
        count = 0
        for player in self.players:
            if player.player_remaining:
                count += 1
        return count


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


# this function was originally under game class (moved here for more flexibility) - Mr.Weible's recommendation
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

# def run_the_sim(Sarah_win_count, Becca_win_count, Andrew_win_count):
#     # this player creation part changed due to the create_players() function (moved outside the game class)
#     player_list = ["Sarah", "Becca", "Andrew"]
#     strategies = ["strategy_1", "strategy_2", "strategy_3"]
#     players = create_players(player_list, strategies)
#
#     game = Game(players) # initialize game
#     # try:
#     #     winner = game.play_until_winner()
#     # except Exception as e:
#     #     print(f"Error during simulation: {str(e)}")
#     #     return "Error"
#
#     winner = game.play_until_winner()
#
#     # Log the winner
#     if winner != "Tie":
#         print(f"{winner} wins!")
#     else:
#         print("It's a tie!")
#     return winner