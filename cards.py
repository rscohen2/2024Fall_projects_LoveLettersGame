from players import *
from game import *

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
        self.__value = Card.card_values[self.__class__.__name__] #this line eliminates the need for individual init functions in each subclass

    @property
    def value(self):
        return self.__value


class Princess(Card):
    """
    The Princess card is the highest value card. If you play or discard the Princess card, you lose the game.
    If you have the Princess card in your hand at the end of the round, you could win since it has the highest value.
    >>> from players import *
    >>> player_1 = Player("strategy_3", "Sarah")
    >>> player_2 = Player("strategy_2", "Becca")
    >>> player_3 = Player("strategy_3", "Andrew")
    >>> game = Game([player_1, player_2, player_3])
    >>> Princess.play_card(Princess(), player_1, target=None, guess=None, game=None)
    Sarah eliminated for discarding the Princess!
    >>> player_1.player_remaining
    False
    >>> player_2.player_remaining
    True
    """


    def play_card(self, player, target=None, guess=None, game=None):
        player.players_hand.clear()  # Explicitly clear the hand
        player.player_remaining = False
        print(f"{player.name} eliminated for discarding the Princess!")


class Countess(Card):
    """
    You must play the Countess card if you have a king or prince in your hand.
    """
    self = None


    def play_card(self, player, target, guess, game=None):
        if 'King' or 'Prince' in Player.players_hand:
            # print("Countess card played!")
            card_played = 'Countess'
            return card_played




class King(Card):
    """
    When played, the King card allows you to trade hands with a player of your choice.
    """

    def play_card(self, player, target, guess, game=None):
        # discard the played King card
        player.players_hand.remove(self)
        opponent = target
        player.card_knowledge[opponent.name].append(opponent.players_hand)
        opponent.card_knowledge[player.name].append(player.players_hand)
        tempHand = opponent.players_hand
        opponent.players_hand = player.players_hand
        player.players_hand = tempHand
        return player.players_hand, opponent.players_hand



class Prince(Card):
    """
    When the prince card is played, an opponent of your choice must discard their hand.
    """
    def play_card(self, player, target, guess, game=None):
        for card in target.players_hand[:]:  # it seems that an Index out of range error was happening here. Asked ChatGPT what the problem is an it suggested iteration through slicing
            target.players_hand.remove(card)
            if card.__class__.__name__ == "Princess":
                target.player_remaining = False
                print(f"{target.name} eliminated by discarding the Princess!")
                return
        game.draw_a_card(target)
        print(f"{target.name} redrew a card.")

class Handmaid(Card):
    """ When you play the handmaid card, you cannot be chosen for any opponent's card actions during this round."""
    def play_card(self, player, target, guess, game=None):
        card_played = 'Handmaid'
        player.player_protected = True
        return card_played



class Baron(Card):
    """ Compare card values with an opponent. Whoever has the lower value is out of the round.
    >>> from players import *
    >>> player_1 = Player("strategy_3", "Sarah")
    >>> player_2 = Player("strategy_2", "Becca")
    >>> player_3 = Player("strategy_3", "Andrew")
    >>> game = Game([player_1, player_2, player_3])
    >>> opponent = player_2
    >>> player_1.players_hand = [Prince(), Princess()]
    >>> Baron.play_card(Baron(), player_1, target=opponent, guess=None, game=None)
    Becca eliminated in a Baron comparison!

    """


    def play_card(self, player, target, guess, game=None):
        if not target.players_hand or not player.players_hand:
            print(f"Cannot play Baron: {target.name} or {player.name} has no cards.")
            return

        opp_card = target.players_hand[0]
        your_card = player.players_hand[0]
        if your_card.value > opp_card.value:
            target.player_remaining = False # target eliminated
            print(f"{target.name} eliminated in a Baron comparison!")
        elif opp_card.value > your_card.value:
            player.player_remaining = False # player emliminated
            print(f"{player.name} eliminated in a Baron comparison!")



class Priest(Card):
    """ The Priest card allows you to look at an opponent's hand of your choice."""

    def play_card(self, player, target, guess, game=None):
        opponent = target
        opponents_hand = opponent.players_hand
        player.card_knowledge[opponent.name].append(opponent.players_hand)
        return player.card_knowledge



class Guard(Card):
    """ When the guard card is played, the player guesses a card that they think is in an opponent of their choice's hand.
    If they are correct, that opponent is out of the round. Otherwise, if their guess is incorrect, nothing happens and the game continues."""


    def play_card(self, player, target, guess, game=None):
        for card in target.players_hand:
            if card.__class__.__name__ == guess:
                print(f"{player.name} guessed correctly! {target.name} had the {guess} card.")
                target.player_remaining = False  # Eliminate the target
                return

        # If no match, the guess is incorrect
        print(f"{player.name} guessed wrong! {target.name} does not have the {guess} card.")

