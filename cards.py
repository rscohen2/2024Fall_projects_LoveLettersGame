from players import *
from game import *
# from players import Player
# The logic for switching hands (when the King card is played) needs to be updated slightly,
# Current:
#         player.players_hand = opponent.players_hand
#         opponent.players_hand = player.players_hand
#
# Suggested update (or something like this):
#       tempHand = opponent.players_hand
#       opponent.players_hand = player.players_hand
#       player.players_hand = tempHand

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

    # self.card_type = card_type
        # self.__value = value
        # self.player = None

    @property
    def value(self):
        return self.__value

    # def general_play_card(self):
    #     """
    #     This function updates the cards played in the Player and Game class, and also keeps track of cards_in_play using the Game class.
    #     :return:
    #     """
    #     # update_cards_played(Player.card_selected_to_play_, Game.cards_played)
    #     ##I think this is already done in Andrews work
    #     Game.cards_in_play.append(Game.card_played)


class Princess(Card):
    """
    The Princess card is the highest value card. If you play or discard the Princess card, you lose the game.
    If you have the Princess card in your hand at the end of the round, you could win since it has the highest value.
    """
    # def __init__(self):
    #     super().__init__()
    #     self.__value = self.card_values['Princess']

    def play_card(self, player, target, guess):
        # # Princess-specific play logic
        # # print("Princess card played!")
        # # Trigger player elimination if the Princess is played or discarded
        # player.player_remaining = False  # I think this is an easier way of indicating someone is out of the round
        # #player_is_out_of_the_round(Player, Game.players)
        # card_played = 'Princess'

        # TODO: NEWLY MODIFIED
        # print("Princess card played!")
        player.players_hand.clear()  # Explicitly clear the hand
        player.player_remaining = False
        print(f"{player.name} eliminated for discarding the Princess!")


class Countess(Card):
    """
    You must play the Countess card if you have a king or prince in your hand.
    """
    self = None

    # def __init__(self, value, card_type):
    #     self.__value = self.card_values['Countess']

    def play_card(self, player, target, guess):
        if 'King' or 'Prince' in Player.players_hand:
            # print("Countess card played!")
            card_played = 'Countess'
            return card_played




class King(Card):
    """
    When played, the King card allows you to trade hands with a player of your choice.
    """
    # def __init__(self, value):
    #     self.__value = self.card_values['King']
    def play_card(self, player, target, guess):
        # print("King card played!")
        #opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        opponent = target
        # Player.card_knowledge[opponent].append(opponent.players_hand)
        # opponent.card_knowledge[Player].append(Player.players_hand)
        # Player.players_hand = opponent.players_hand
        # opponent.players_hand = Player.players_hand
        # return Player.players_hand, opponent.players_hand
        player.card_knowledge[opponent.name].append(opponent.players_hand)
        opponent.card_knowledge[player.name].append(player.players_hand)
        # player.players_hand = opponent.players_hand
        # opponent.players_hand = player.players_hand
        tempHand = opponent.players_hand
        opponent.players_hand = player.players_hand
        player.players_hand = tempHand
        return player.players_hand, opponent.players_hand



class Prince(Card):
    """
    When the prince card is played, an opponent of your choice must discard their hand.
    """
    # def __init__(self, value, card_type):
    #     self.__value = self.card_values['Prince']
    def play_card(self, player, target, guess):
        # # print("Prince card played!")
        # #reset opponents hand, and put their cards in the discard pile (cards_played?)
        # #opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        # opponent = target
        # for card in opponent.players_hand:
        #     if card == 'Princess':
        #         player.player_remaining = False #I think this is an easier way of indicating someone is out of the round
        #         #player_is_out_of_the_round(opponent, Game.players)
        #     opponent.players_hand.remove(card)
        #
        # card_played = 'Prince'
        # return opponent.players_hand
        # TODO: NEWLY MODIFIED
        # print("Prince card played!")
        for card in target.players_hand[:]:  # it seems that an Index out of range error was happening here. Asked ChatGPT what the problem is an it suggested iteration through slicing
            target.players_hand.remove(card)
            if card.__class__.__name__ == "Princess":
                target.player_remaining = False
                print(f"{target.name} eliminated by discarding the Princess!")
            # else:
            #     target.players_hand = game.draw_a_card(target)
        # if player.game.cards:
        #     player.game.draw_a_card(target)

class Handmaid(Card):
    """ When you play the handmaid card, you cannot be chosen for any opponent's card actions during this round."""
    # def __init__(self):
    #     self.__value = self.card_values['Handmaid']
    def play_card(self, player, target, guess):
        # print("Handmaid card played!")
        card_played = 'Handmaid'
        player.player_protected = True # TODO: I added this part since we weren't implementing handmaid protection effect anywhere in our code
        return card_played



class Baron(Card):
    """ Compare card values with an opponent. Whoever has the lower value is out of the round."""
    # def __init__(self):
    #     self.__value = self.card_values['Baron']

    def play_card(self, player, target, guess):

        # opponent = target
        # #opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        # opponents_hand = opponent.players_hand
        # try:
        #     opp_card = opponents_hand[0]
        #     your_card = player.players_hand[0]
        #     if your_card.value > opp_card.value:
        #         opponent.player_remaining = False  # I think this is an easier way of indicating someone is out of the round
        #         # player_is_out_of_the_round(opponent, Player.players)
        #     elif opp_card.value > your_card.value:
        #         player.player_remaining = False  # I think this is an easier way of indicating someone is out of the round
        #         # player_is_out_of_the_round(Player, Player.players)
        #         card_played = 'Baron'
        #         return card_played
        # except IndexError:
        #     print(opponent.name, player.name)
        #     print(opponent.player_remaining)
        #     print(player.players_hand)
        #     print('IndexError to review for debugging')
        # TODO: NEWLY MODIFIED
        # print("Baron card played!")
        # Check whether both players have cards in hand
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
    # def __init__(self, value, card_type):
    #     self.__value = self.card_values['Priest']

    def play_card(self, player, target, guess):
        # print("Priest card played!")
        #opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        opponent = target
        opponents_hand = opponent.players_hand
        player.card_knowledge[opponent.name].append(opponent.players_hand)
        return player.card_knowledge



class Guard(Card):
    """ When the guard card is played, the player guesses a card that they think is in an opponent of their choice's hand.
    If they are correct, that opponent is out of the round. Otherwise, if their guess is incorrect, nothing happens and the game continues."""

    # def __init__(self, __value):
    #     self.__value = self.card_values['Guard']

    def play_card(self, player, target, guess):
        # #opponent = choose_opponent(Player.opponents, Game.cards_in_play)
        # opponent = target
        # for card in opponent.players_hand:
        #     if card == guess:
        #         player.player_remaining = False #I think this is an easier way of indicating someone is out of the round
        #         #Player.players = player_is_out_of_the_round(opponent, Player.players)
        #     card_played = 'Guard'
        #     return player.player_remaining
        #
        #     #correct properties of another class instead of parameters for the current game state
        # TODO: NEWLY MODIFIED
        # print("Guard card played!")
        for card in target.players_hand:
            if card.__class__.__name__ == guess:
                print(f"{player.name} guessed correctly! {target.name} had the {guess} card.")
                target.player_remaining = False  # Eliminate the target
                return

        # If no match, the guess is incorrect
        print(f"{player.name} guessed wrong! {target.name} does not have the {guess} card.")

