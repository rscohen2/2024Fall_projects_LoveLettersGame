
import random
import Counter

# cards = ['Princess', 'Countess', 'King','Prince','Prince','Handmaid','Handmaid','Baron','Baron','Priest','Priest','Guard','Guard','Guard','Guard','Guard']

def new_game():
    """
    Starts a new game by resetting cards to have the entire deck, and resets cards_drawn to empty since no cards have been drawn yet.
    :return: cards_drawn, cards
    """
    cards_drawn = []
    cards = ['Princess', 'Countess', 'King', 'Prince', 'Prince', 'Handmaid', 'Handmaid', 'Baron', 'Baron', 'Priest',
             'Priest', 'Guard', 'Guard', 'Guard', 'Guard', 'Guard']

    return cards_drawn, cards


def current_deck(cards, cards_drawn):
    """

    :param cards:
    :param cards_drawn:
    :return: cards that are in play
    """
    for card in cards:
        if card in cards_drawn:
            cards.remove(card)
    return cards

def players_hand(player):
    players_hand = []
    return players_hand

def draw_a_card(cards_drawn, cards, players_hand):
    """

    :param cards_drawn:
    :param cards:
    :return: card that is drawn
    """
    i = random.randint(0, 15)
    card_drawn = cards[i]
    cards_drawn.append(card_drawn)
    players_hand.append(card_drawn)
    return card_drawn, cards_drawn, players_hand

def play_card():
    """

    :return:
    """

def player_is_out_of_the_round(player_out, players):
    """
    removes a player who is out of the round from the players list, and returns the players who are still in that round
    :return: players who are still in the round
    """
    players = players.remove(player_out)
    return players






class Player:
    """A competitor in the game."""

    player_count = 0  # Initialize count of all players.
    all_players = []  # automatically track all players

    def __init__(self, ):
        Player.player_count += 1
        Player.all_players.append(self)

        self.strategy = None
        self.randmax = None
        self.players_hand = []
        # track player stats:
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.opponents = Counter()
        self.choices = Counter()


class Player1(Player):
    #strat for player 1
    # def __init__(self, self.strategy, players_hand = None):

    pass

class Player2(Player):
    pass

class Player3(Player):
    pass

        # pre-calculate and store these values for randomization of turns:
        # r, p, s = self.strategy
        # self.randmax = r + p + s
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


    #chatgpt helped me figure out how to organize the values here and add them correctly to the classes below

    def __init__(self, card_type, color=None, location=None):
        self.card_type = card_type
        self.__value = self.card_values.get(card_type, 0)  # Default to 0 if card_type not in card_values

    @property
    def value(self):
        return self.__value

    def do_something(self, what_to_do):
        pass



class Princess(Card):
    def __init__(self, value):
        self.__value = self.card_values['Princess']

    def play_card(self, player, players):
        # Princess-specific play logic
        print("Princess card played!")
        # Trigger player elimination if the Princess is played
        player_is_out_of_the_round(player, players)



class Countess(Card):
    def __init__(self, value):
        self.__value = self.card_values['Countess']

    def play_card(self, player, players):
            # Princess-specific play logic
            print("Countess card played!")
            players_hand - card_played
        if 'King' or 'Prince' in players_hand:
            self.play_card()





class King(Card):
    def __init__(self, value):
        self.__value = 7
    pass


class Prince(Card):
    def __init__(self, value):
        self.__value = 6
    pass

class Handmaid(Card):
    def __init__(self, value):
        self.__value = 2
    pass

class Baron(Card):
    def __init__(self, value):
        self.__value = 4
    pass

class Priest(Card):
    def __init__(self, value):
        self.__value = 5
    pass

class Guard(Card):
    def __init__(self, value):
        self.__value = 1
    def guess(self, guess, opponents_hand, opponent):
        for card in opponents_hand:
            if card == guess:
                player_is_out_of_the_round(opponent, players)

if __name__ == '__main__':
    players = [1,2,3,4]
    # control = Player('control')

    cards_drawn, cards = new_game()
    # print(len(cards))

    for player in players:
        players_hand = []
        cards = current_deck(cards, cards_drawn)
        card_drawn = draw_a_card(cards_drawn, cards)
        print(card_drawn)
        players_hand.append(card_drawn)



#Princess
    #(1) Lose if discarded


#Countess
    #(1) discard if caught with king or prince

#King
    #(1) trade hands

#Prince
    #(2) one player discards his or her hand

#Handmaid
    #(2) protection until your next turn


#Baron
    #(2) compare hands, lower hand is out


#Priest
    #(2) Look at a hand


#Guard
    #(5) Guess a player's hand


########




########
#Player classes
########


