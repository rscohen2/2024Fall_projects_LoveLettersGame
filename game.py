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
from random import randint

# TODO: used import as syntax (e.g., import pandas as pd) to solve the circular import problem (Mr. Weible's help)
import players as p
import cards as c
import random
from collections import Counter


class Game:

    # TODO: I'm not sure if we need these class attributes (I feel like it is redundant)
    # current_deck = None
    # cards = None
    # card_played = None
    # cards_in_play = []
    # players = None
    # cards_played = None #  not sure about this

    def __init__(self, players):
        self.players = players # creating player objects
        self.cards = [] # deck of cards
        self.remaining_cards = Counter() # Track remaining cards
        self.current_player_index = 0 # tracking turn for current player
        self.new_game()
        # self.cards_played = [] # tracking played cards TODO: isn't this redundant with player.card_played?
        # self.cards_in_play = [] # tracking cards currently in play TODO: not sure if we need this (maybe might need it when we are going to consider card memory/knowledge?)
        # TODO: another property like self.card (for discarded pile) -> this will be even helpful for debugging purposes -> cards_played can be used for this (just give it another name)

    def new_game(self) -> None: # moved this to class function from normal function (outside the class)
        """
        Starts a new game by resetting (shuffling) card and player status
        :return: None
        """
        # Shuffling the deck (deck object obtained)
        self.cards = [c.Guard()] * 5 + [c.Priest()] * 2 + [c.Baron()] * 2 + [c.Handmaid()] * 2 + [c.Prince()] * 2 + [c.King()] + [c.Countess()] + [c.Princess()]
        random.shuffle(self.cards)

        # this part keeps track of the remaining cards
        self.remaining_cards = Counter()
        for card in self.cards: # card is each card (subclass) object
            card_name = card.__class__.__name__  # didn't know how to access subclass names from other class object (referred to https://stackoverflow.com/questions/3314627/get-subclass-name)
            self.remaining_cards[card_name] += 1

        # # resetting player status
        for player in self.players:
            # self.draw_a_card(player)
            player.players_hand = []
            player.player_remaining = True
            player.player_protected = False
            player.card_knowledge = {
                opponent.name: [] for opponent in self.players if opponent != player
            }

        for player in self.players:
            self.draw_a_card(player)

        self.current_player_index = 0

        # for player in self.players:
        #     player.players_hand = [] # empty player's hand
        #     # player.card_knowledge = {} # I changed this to dictionary (it is None in the players class module) TODO: we don't need this yet
        #     player.player_remaining = True   # reset all players to be remained in the game
        #     player.player_protected = False  # reset the protection effect (via Handmaid card)
        #     # player.card_knowledge = {}
        #     # player.card_knowledge.update(self.players.remove(player) : '')
        #     player.card_knowledge = {
        #         opponent.name: [] for opponent in self.players if opponent != player
        #     }
        #     #I gave chatgpt our prior code and error and asked what was wrong
        #
        #     #oh also here we need to deal cards when we start a new game!!
        #     self.draw_a_card(player)

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
            # if (len(player.players_hand)) != 1:
            #     print('potential error?')
            #this should be 1 above...
            #they should draw a card even if they have handmaid tho, so I changed this
            # self.draw_a_card(player) # draw a card
            # sanity check that the player should have 2 cards now
            # if (len(player.players_hand)) != 2:
            #     print('error?')

        # resetting handmaid effect
        player.player_protected = False
        self.draw_a_card(player)

        selected_card = player.card_to_play() # TODO: I changed the variable name card_index to selected_card since it seemed misleading

        if not selected_card:
            print(f"{player.name} has no valid card to play.")
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            return

        # choose opponent (guard, baron, king, priest, prince)
        # Got help from ChapGPT for handling the AttributeError with NoneType
        target = None
        if isinstance(selected_card, (c.Guard, c.Baron, c.King, c.Priest, c.Prince)):
            target = self.choose_opponent(player)

        # Guard card requires a guess
        guess = None
        if isinstance(selected_card, c.Guard) and target:
            #TODO figure out how to fix this with the p.playStrategy1 to make this work
            if p.strategy == 1:
                guess = c.Princess
            if p.playStrategy2:
                guess = player.guess_card(self.get_remaining_card_list())
            if p.playStrategy3:
                result = self.chooseRandomCard()

        if target is None and not isinstance(selected_card, (c.Handmaid, c.Countess, c.Princess)):
            print(f"No valid target for {player.name}. Turn skipped.")
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            return

        selected_card.play_card(player, target, guess)
        player.remove_card(selected_card)

        # target = self.choose_opponent(player) # randomly choose opponent
        # # TODO: I added the guessing logic for strategy 1 in player class
        # guess = player.guess_card(self.get_remaining_card_list())

        # if selected_card:
            # selected_card_name = selected_card.__class__.__name__
            # if target or isinstance(selected_card, c.Handmaid):
            #     player.play_card(selected_card, target, guess)
            # player.play_card(selected_card, target, guess)


            # if player.strategy == "strategy_1": #adding guess for strategy 1 (always guess Princess)
            #     print(self.allcards)
            #     guess = [i for i in self.allcards if "Princess" in str(type(i))][0]
            # else: # else if not strategy1, then the guess will be random from all the cards in the deck
            #     guess = self.remaining_cards[randint(0,len(self.remaining_cards))]
            # print(guess)
            # if target or isinstance(selected_card, c.Handmaid):
            #     player.play_card(selected_card, target, guess) # play the chosen card


        # to next player (make sure the order is properly circulating (e.g., 1 -> 2 -> 3 / 2 -> 3 -> 1 / 3 -> 1 -> 2)
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0

    # Added this function to properly get the remaining card list
    def get_remaining_card_list(self):
        """Returns a list of remaining cards."""
        remaining_cards = []
        for card_name, count in self.remaining_cards.items():
            for _ in range(count):
                remaining_cards.append(card_name)

        for player in self.players:
            if player.player_remaining:
                for card in player.players_hand:
                    remaining_cards.append(card.__class__.__name__)

        return remaining_cards

    # I sort of merged and modified the original game_play_until_winner() and winner() into one function
    # Also I modified it as an instance function from class function
    # I didn't use the dictionary idea since I thought keeping track of remaining players list seemed more simple (implemented in self.track_remaining_players() function)
    def play_until_winner(self) -> p.Player:
        """
        This function is designed to determine the winner of the game in two scenarios:
            1. Last player standing (i.e., other players got eliminated)
            2. Deck out of cards -> player with highest value card wins

        :return: return winner
        """
        self.new_game() # start a new game (reshuffle deck and restart player status)

        # for player in self.players:
        #     self.draw_a_card(player)
        #     player.player_remaining = True
        #     player.player_protected = False

        # # deal one card each for players
        # for player in self.players:
        #     self.draw_a_card(player)

        # keep playing turns until there is only one player standing OR until the deck is empty
        while self.count_remaining_players() > 1 and len(self.cards) > 0:
            self.play_turn()

        # determine winner (2 cases)
        remaining_players = self.track_remaining_players()

        # 1. last player standing
        if len(remaining_players) == 1:
            return remaining_players[0]

        # 2. player with highest card
        return self.get_player_with_highest_card(remaining_players)


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

            # return card
        # return None


    # moved to instance function
    # this might have to be in players class
    def choose_opponent(self, current_player: p.Player): # TODO: not sure how to type annotate this function (specifically the return value)
        """
        This function randomly selects opponent who are 1) remaining in the game and 2) is not protected by handmaid card
        :param current_player:
        :return: opponent player or None
        """
        available_opponent = []
        for player in self.players:
            if player != current_player and player.player_remaining and not player.player_protected and len(player.players_hand) > 0:
                available_opponent.append(player)

        # if len(available_opponent) > 0:
        if available_opponent:
            return random.choice(available_opponent) # TODO: maybe we can modify this later when we are going to consider card knowledge?

        print("No available opponents to target")
        return None

    def count_remaining_players(self):
        count = 0
        for player in self.players:
            if player.player_remaining:
                count += 1
        return count

    def track_remaining_players(self) -> list[p.Player]:
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
    # players should be in a different name
    def get_player_with_highest_card(self, players: list[p.Player]) -> p.Player:
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


# this function was originally under game class (moved here for more flexibility) - Mr.Weible's recommendation
def create_players(player_names: list[str], strategies: list[str]) -> list[p.Player]:
    """
    Function that creates players objects based on their names
    :param player_names:
    :param strategies:
    :return: player objects
    """
    player_objects = []
    for i, name in enumerate(player_names):
        strategy = strategies[i]
        player_objects.append(p.Player(name=name, strategy=strategy))

    return player_objects

def run_the_sim(Sarah_win_count, Becca_win_count, Andrew_win_count):
    # this player creation part changed due to the create_players() function (moved outside the game class)
    player_list = ["Sarah", "Becca", "Andrew"]
    strategies = ["strategy_1", "strategy_2", "strategy_3"]
    players = create_players(player_list, strategies)

    game = Game(players)

    # new_game(game)
    winner = game.play_until_winner()

    if winner:
        print(f"{winner.name} wins!")
        # if winner.name == "Sarah":
        #     Sarah_win_count += 1
        # if winner.name == "Becca":
        #     Becca_win_count += 1
        # if winner.name == "Andrew":
        #     Andrew_win_count += 1
        return winner.name
    else:
        print("\nSomething went wrong with the code")
        return "Error"


# # this is just a simple execution code to see if game.py is working (not a monte carlo)
# if __name__ == "__main__":
#
#     Andrew_win_count = 0
#     Sarah_win_count = 0
#     Becca_win_count = 0
#     for i in range(1,1000):
#         run_the_sim(Sarah_win_count, Becca_win_count, Andrew_win_count)
#     print(f"Sarah_wins: {Sarah_win_count} Andrew_wins: {Andrew_win_count},'Becca_wins: {Becca_win_count}")
    # this player creation part changed due to the create_players() function (moved outside the game class)
    # player_list = ["Sarah", "Becca", "Andrew"]
    # strategies = ["strategy_1", "strategy_2", "strategy_3"]
    # players = create_players(player_list, strategies)
    #
    # game = Game(players)
    #
    # winner = game.play_until_winner()
    #
    # if winner:
    #     print(f"{winner.name} wins!")
    # else:
    #     print("\nSomething went wrong with the code")

    # TODO: Currently getting the following error:
    # ImportError: cannot import name 'choose_opponent' from partially initialized module 'game' (most likely due to a circular import)
    # (C:\Users\namdi\PycharmProjects\IS597\2024Fall_projects_LoveLettersGame\game.py)
    # I think this has to do with the game class and player class modules getting into a circular import