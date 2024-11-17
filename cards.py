from game import choose_opponent, update_cards_played, Game, player_is_out_of_the_round
from players import *
from game import *
from players import Player


class Card:
    # Define card values within the Card class
    card_values = {
        'Princess': 9,
        'Countess': 8,
        'King': 7,
        'Prince': 6,
        'Baron': 5,
        'Priest': 4,
        'Handmaid': 2,
        'Guard': 1}

    # chatgpt helped me figure out how to organize the values here and add them correctly to the classes below

    def __init__(self):
        # self.card_type = card_type
        # self.__value = value
        # self.player = None

    @property
    def value(self):
        return self.__value

    def general_play_card(self):
        update_cards_played(Player.card_played, Game.cards_played)
        Game.cards_in_play.append(Game.card_played)


class Princess(Card):
    """
    The Princess card is the highest value card. If you play or discard the Princess card, you lose the game.
    If you have the Princess card in your hand at the end of the round, you could win since it has the highest value.
    """
    def __init__(self):
        super().__init__()
        self.__value = self.card_values['Princess']

    def play_card(self):
        # Princess-specific play logic
        print("Princess card played!")
        # Trigger player elimination if the Princess is played or discarded
        player_is_out_of_the_round(Player, Game.players)
        card_played = 'Princess'





class Countess(Card):
    """
    You must play the Countess card if you have a king or prince in your hand.
    """
    self = None

    def __init__(self, value, card_type):
        self.__value = self.card_values['Countess']

    def play_card(self):
        if 'King' or 'Prince' in Player.players_hand:
            print("Countess card played!")
            card_played = 'Countess'
            return card_played




class King(Card):
    """
    When played, the King card allows you to trade hands with a player of your choice.
    """
    def __init__(self, value):
        self.__value = self.card_values['King']
    def play_card(self):
        opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        Player.card_knowledge[opponent].append(opponent.players_hand)
        opponent.card_knowledge[Player].append(Player.players_hand)
        Player.players_hand = opponent.players_hand
        opponent.players_hand = Player.players_hand
        return Player.players_hand, opponent.players_hand



class Prince(Card):
    """
    When the prince card is played, an opponent of your choice must discard their hand.
    """
    def __init__(self, value, card_type):
        self.__value = self.card_values['Prince']
    def play_card(self):
        print("Prince card played!")
        #reset opponents hand, and put their cards in the discard pile (cards_played?)
        opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        for card in opponent.players_hand:
            if card == 'Princess':
                player_is_out_of_the_round(opponent, Game.players)
            opponent.players_hand.remove(card)

        card_played = 'Prince'
        return opponent.players_hand


class Handmaid(Card):
    """ When you play the handmaid card, you cannot be chosen for any opponent's card actions during this round."""
    def __init__(self, value, card_type):
        self.__value = self.card_values['Handmaid']
    def play_card(self):
        card_played = 'Handmaid'
        return card_played



class Baron(Card):
        """ Compare card values with an opponent. Whoever has the lower value is out of the round.
    """
    def __init__(self, value, card_type):
        self.__value = self.card_values['Baron']

    def play_card(self):

        opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        opponents_hand = opponent.players_hand
        opp_card = opponents_hand[0]
        your_card = Player.players_hand[0]
        if your_card.value > opp_card.value:
            player_is_out_of_the_round(opponent, Player.players)
        elif opp_card.value > your_card.value:
            player_is_out_of_the_round(Player, Player.players)
            card_played = 'Baron'
            return Player.players



class Priest(Card):
    """ The Priest card allows you to look at an opponent's hand of your choice."""
    def __init__(self, value, card_type):
        self.__value = self.card_values['Priest']

    def play_card(self):
        opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        opponents_hand = opponent.players_hand
        Player.card_knowledge[opponent].append(opponent.players_hand)
        return Player.card_knowledge



class Guard(Card):
    """ When the guard card is played, the player guesses a card that they think is in an opponent of their choice's hand.
    If they are correct, that opponent is out of the round. Otherwise, if their guess is incorrect, nothing happens and the game continues."""

    def __init__(self, __value):
        self.__value = self.card_values['Guard']

    def play_card(self, guess):
        opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        for card in opponent.players_hand:
            if card == guess:
                Player.players = player_is_out_of_the_round(opponent, Player.players)
            card_played = 'Guard'
            return Player.players

            #correct properties of another class instead of parameters for the current game state

