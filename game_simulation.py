
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

def choose_opponent(opponents):
    opponent = random.choice(opponents)
    return opponent

def update_cards_played(card_played, cards_played):
    cards_played.append(card_played)
    return cards_played, cards_played


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

    def __init__(self, card_type, color=None, location=None):
        self.card_type = card_type
        self.__value = None

    @property
    def value(self):
        return self.__value

    def do_something(self, what_to_do):
        pass


class Princess(Card):
    def __init__(self, value):
        self.__value = self.card_values['Princess']

    def play_card(self, player, players, cards_played):
        # Princess-specific play logic
        print("Princess card played!")
        # Trigger player elimination if the Princess is played
        player_is_out_of_the_round(player, players)
        card_played = 'Princess'
        update_cards_played(card_played, cards_played)




class Countess(Card):
    self = None

    def __init__(self, value, card_type):
        super().__init__(card_type)
        self.__value = self.card_values['Countess']

    def play_card(self, player, players, cards_played):
        # Princess-specific play logic
        print("Countess card played!")
        card_played = 'Countess'
        update_cards_played(card_played, cards_played)
        return card_played



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
    self = None
    #this is because I am using it later in the players strategy class bit but don't think I am doing this right

    def __init__(self, __value):
        self.__value = self.card_values['Guard']

    def play_card(self, guess, opponents_hand, opponent):
        for card in opponents_hand:
            if card == guess:
                player_is_out_of_the_round(opponent, players)
        return players


class Player:
    """A competitor in the game."""

    player_count = 0  # Initialize count of all players.
    all_players = []  # automatically track all players

    def __init__(self, strategy):
        Player.player_count += 1
        Player.all_players.append(self)



        self.strategy = strategy
        self.randmax = None
        self.players_hand = []
        # track player stats:
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.opponents = Counter()
        self.choices = Counter()
        self.player = None
        self.players_hand = None

    def check_hand_for_countess(self, cards_played):
        if 'Countess' in players_hand:
            if 'King' or 'Prince' in players_hand:
                move = Countess.play_card(Countess.self, self.player, players, cards_played)
                return move


class Player1(Player):
    #strat for player 1
    # def __init__(self, self.strategy, players_hand = None):
    def __init__(self, strategy):
        super().__init__(strategy)
        self.strategy = self.strategy_1
        self.players_hand = self.players_hand
        self.player = 'player1'
    def strategy_1(self, opponents_hand):
        if 'Guard' in self.players_hand:
            opponent = choose_opponent(players)
            opponents_hand = players_hand(opponent)
            guess = cards.unique().count().max() #guess the most frequent card left in deck?
            move = Guard.play_card(Guard.self, guess, opponents_hand, opponent)
            return move


class Player2(Player):
    def strategy_2(self):
        return

    def __init__(self, strategy):
        self.strategy = self.strategy_2()

    pass

class Player3(Player):
    def strategy_3(self):

    def __init__(self, strategy):
        self.strategy = self.strategy_3()

    pass

        # pre-calculate and store these values for randomization of turns:
        # r, p, s = self.strategy
        # self.randmax = r + p + s

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





