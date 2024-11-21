from random import random

from game import *
from cards import *


class Player:
    """A competitor in the game."""
    # TODO: Leave these in? Put in the game class?
    players_hand = None
    players = None # TODO: what is difference between this and all_players?
    opponents = None
    card_knowledge = None
    card_played = None
    player_count = 0  # Initialize count of all players. # TODO: moved up to game class?
    all_players = []  # automatically track all players # TODO: moved up to game class?

    def __init__(self, strategy, name):
        Player.player_count += 1 # TODO: add this to the game class
        Player.all_players.append(self) # TODO: add this to the game class
        self.name = name
        self.strategy = strategy
        # self.randmax = None
        self.players_hand = []
        # track player stats:
        # self.wins = 0 --> for game class?
        # self.losses = 0 --> for game class?
        # self.ties = 0 --> for game class?
        self.opponents = Counter()
        self.choices = Counter()
        self.player = None
        self.card_knowledge = {}
        self.card_selected_to_play = None # Renamed this from card_played to card_selected_to_play, for clarity.
        self.player_remaining = True
        self.player_protected = False


    # TODO: We need a card index
    # TODO: for Guard card subclass, add target (opponent) to parameters

    def checkGuard(self):
        for card in self.players_hand:
            if "Guard" in type(card):
                return(card)
    def checkCountessCondition(self):
        cardTypes = [type(i) for i in self.players_hand]
        if "Countess" in cardTypes:
            if "Prince" in cardTypes:
                return True
            elif "King" in cardTypes:
                return True
        else:
            return False

    def chooseRandomCard(self):
        card = self.players_hand[random.randint(0,len(self.players_hand))]
        return(card)
    def playStrategy1(self):
        result = ""
        while len(result) == 0:
            result = self.checkGuard()
            result = self.chooseRandomCard()
        return (result)
    def playStrategy2(self):
        return(self.chooseRandomCard())
    def card_to_play(self):
        if self.checkCountessCondition() == False:
            if self.name == "Player 1":
                cardSelected = self.playStrategy1()
            if self.name == "Player 2":
                cardSelected = self.playStrategy2()
            if self.name == "Player 3":
                cardSelected = self.playStrategy3()
        else:
            cardSelected = [card for card in self.players_hand if "Countess" in type(card)][0]
        self.card_selected_to_play = cardSelected
        return(cardSelected)

    def play_card(self, card_selected_to_play, target):
        #Depending on how we revise the parameters for cards, we will want to add
        #more logic here. I.E. if "Guard" in type(cardIndex) then take cardTarget
        #for first parameter and choose random name from list of cards for
        #parameter 2. If a card only has one parameter, like a target,
        #we'll want to account for that.
        # if "Guard" in type(cardIndex):
        #   cards_avail = ["Baron", "Handmaiden",etc...]
        #   cardIndex.play_card(cardTarget, cards_avail[random.randint(0,len(cards_avail))
        # else if "Handmaiden" in type(cardIndex):
        #   self.player_protected =True
        #   OR, PENDING CHANGES
        #   cardIndex.play_card(self)


        ######
        #from Becca: isn't cardTarget and opponent the same variable? or no?
            #if so, then maybe the parameter should be opponent...
            #I structured it so opponent is chosen from the list of opponents
            #and opponents is a list of players - player in question

        if "Baron" in type(card_selected_to_play):
            card_selected_to_play.play_card(self, target)
        elif "King" in type(card_selected_to_play):
            card_selected_to_play.play_card(self, target)
        elif "Handmaiden" in type(card_selected_to_play):
            card_selected_to_play.play_card(self)
        elif "Prince" in type(card_selected_to_play):
            card_selected_to_play.play_card(target)
        elif "Princess" in type(card_selected_to_play):
            card_selected_to_play.play_card(self)
        elif "Guard" in type(card_selected_to_play):
            card_selected_to_play.play_card(target)
        elif "Priest" in type(card_selected_to_play):
            card_selected_to_play.play_card(target)
        self.players_hand = [card for card in self.players_hand if card != self.card_selected_to_play]
        self.card_selected_to_play = None

    #TODO : incorporate the strategies into one function?
'''
    def strategy_1(self, opponents_hand):
        if 'Guard' in self.players_hand:
            opponent = choose_opponent(self.opponents, opponent_card_in_play)
            opponents_hand = players_hand(opponent)
            guess = Game.cards.unique().count().max()  # guess the most frequent card left in deck?
            move = Guard.play_card(Guard.self, guess, opponents_hand, opponent)
            return move
        #        return players_hand, opponents_hand, cards_in_play, cards_played
        else:
            i = random.randint(0, 2)
            card_to_play = self.players_hand[i]
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
#         # self.randmax = r + p + s '''
