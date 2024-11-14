
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

def deal_cards():
    Player1.players_hand = []
    card_drawn = draw_a_card(cards_drawn, cards)
    Player1.players_hand.append(card_drawn)

    Player2.players_hand = []
    card_drawn = draw_a_card(cards_drawn, cards)
    Player2.players_hand.append(card_drawn)

    Player3.players_hand = []
    card_drawn = draw_a_card(cards_drawn, cards)
    Player3.players_hand.append(card_drawn)



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

def choose_opponent(opponents, opponent_card_in_play):
    # TODO: check if opponent has handmaid card, then remove them from opponents list?
    for opponent in opponents:
        if opponent_card_in_play == 'Handmaid':
    # TODO: implement opponent_card_in_play somehow in the player class??
            opponents.remove(opponent)
    opponent = random.choice(opponents)
    return opponent

def update_cards_played(card_played, cards_played):
    cards_played.append(card_played)
    return cards_played, cards_played

def clear_cards_in_play(cards_in_play):
    cards_in_play = []
    return cards_in_play

def player_turn(player, player.strategy):
    card_drawn = draw_a_card(cards_drawn, cards)
    player.players_hand.append(card_drawn)
    move = player.strategy(self, opponents_hand)


def round()
    for player in players:
        player_turn(player, player.strategy)


def winner():
    if len(players) == 1:
        return players[0]

    elif len(current_deck) = 0:
        ending_hands = {}

        # players[0] > players [1]
        for player in players:
            ending_hands.append(player: player.players_hand.card_value)
            current_max_value = 0
        for player in ending_hands:
            if player.players_hand.card_value > current_max_value
            current_max_value = player.players_hand.card_value
            #can we access who that player is from the class structure above
    # else:

=


#player knowledge of cards as a dictionary ex: {player1:, player2:,player3}


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
        self.player = None

    @property
    def value(self):
        return self.__value

    def do_something(self, what_to_do):
        pass


class Princess(Card):
    def __init__(self, value):
        super().__init__(player)
        self.__value = self.card_values['Princess']

    def play_card(self, player, players, cards_played, cards_in_play):
        # Princess-specific play logic
        print("Princess card played!")
        # Trigger player elimination if the Princess is played
        player_is_out_of_the_round(player, players)
        card_played = 'Princess'
        update_cards_played(card_played, cards_played)
        cards_in_play.append(card_played)
        # TODO: sort of standardize the output for play_card for each card?





class Countess(Card):
    self = None

    def __init__(self, value, card_type):
        super().__init__(card_type)
        self.__value = self.card_values['Countess']

    def play_card(self, player, players, cards_played, cards_in_play):
        # Princess-specific play logic
        print("Countess card played!")
        card_played = 'Countess'
        update_cards_played(card_played, cards_played, cards_in_play)
        cards_in_play.append(card_played)
        return cards_played



class King(Card):
    def __init__(self, value, card_type):
        super().__init__(card_type)
        self.__value = self.card_values['King']
    #TODO: trade hands with an opponent of choice
    def play_card(self, player, players, cards_played, opponents_hand, cards_in_play, opponent):
        player.card_knowledge[opponent].append(opponents_hand)
        opponent.card_knowledge[player].append(players_hand)
        player.players_hand = opponents_hand
        opponent.players_hand = players_hand
        return players_hand, opponents_hand, cards_in_play, cards_played

    pass


class Prince(Card):
    def __init__(self, value, card_type):
        super().__init__(card_type)
        self.__value = self.card_values['Prince']
    #TODO: choose a player to discard his or her hand
    def play_card(self, player, players, cards_played, opponents_hand, cards_in_play):
        print("Prince card played!")
        #reset opponents hand, and put their cards in the discard pile (cards_played?)
        for card in opponents_hand:
            opponents_hand.remove(card)
            cards_played.append(card)
        card_played = 'Prince'
        update_cards_played(card_played, cards_played)
        cards_in_play.append(card_played)



    pass


class Handmaid(Card):
    def __init__(self, value, card_type):
        super().__init__(card_type)
        self.__value = self.card_values['Handmaid']
    def play_card(self, player, players, cards_played, cards_in_play):
        card_played = 'Handmaid'
        update_cards_played(card_played, cards_played)
        cards_in_play.append(card_played)

    #TODO: make it so that they cannot be chosen as the opponent (for this round only)

    pass


class Baron(Card):
    def __init__(self, value, card_type):
        super().__init__(card_type)
        self.__value = self.card_values['Baron']

    def play_card(self, Player.players_hand, opponent, opponents_hand, cards_in_play):
    """ Compare card values with an opponent. If they have a lower value, they are out of the round
    (double check that it's just the opponent and not whoever has the lower value is out of the round?)
    """
        opp_card = opponents_hand[0]
        your_card = players_hand[0]
        if your_card.value > opp_card.value:
            player_is_out_of_the_round(opponent, players)
            card_played = 'Baron'
            update_cards_played(card_played, cards_played)
            card_played = 'Prince'
            update_cards_played(card_played, cards_played)
            cards_in_play.append(card_played)

    #TODO: how to add the opponent and players_hand from the PLayer class here? but also can't just switch order bc other things from cards needed in player class...




class Priest(Card):
    def __init__(self, value, card_type):
        super().__init__(card_type)
        self.__value = self.card_values['Priest']

    #TODO: encode player knowledge somehow? like AI that was used in chess sim Dr. W made (since you look at a hand)

    pass


class Guard(Card):
    self = None
    #this is because I am using it later in the players strategy class bit but don't think I am doing this right
    #TODO: figure out the correct way to use self above?
    def __init__(self, __value):
        self.__value = self.card_values['Guard']

    def play_card(self, guess, opponents_hand, opponent, cards_played, players):
        for card in opponents_hand:
            if card == guess:
            players = player_is_out_of_the_round(opponent, players)
            card_played = 'Guard'
            update_cards_played(card_played, cards_played)


class Player:
    """A competitor in the game."""

    player_count = 0  # Initialize count of all players.
    all_players = []  # automatically track all players

    def __init__(self, strategy):
        Player.player_count += 1
        Player.all_players.append(self)



        self.strategy = strategy
        # self.randmax = None
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
        self.opponents = ['player2', 'player3']
        self.card_knowledge = {'player2':[], 'player3':[]}
        self.players_hand = []
    def strategy_1(self, opponents_hand):
        if 'Guard' in self.players_hand:
            opponent = choose_opponent(self.opponents, opponent_card_in_play)
            opponents_hand = players_hand(opponent)
            guess = cards.unique().count().max() #guess the most frequent card left in deck?
            move = Guard.play_card(Guard.self, guess, opponents_hand, opponent)
            return move
        #        return players_hand, opponents_hand, cards_in_play, cards_played
        else:
            i = random.randint(0, 15)
            card_to_play = Player1.players_hand[i]
            move = play_card(card_to_play, opponents_hand, opponent)
            return move



class Player2(Player):
    # TODO: write strat 2, always guess Princess if guard card
    def __init__(self, strategy):
        super().__init__(strategy)
        self.strategy = self.strategy_2
        self.players_hand = self.players_hand
        self.player = 'player2'
        self.opponents = ['player1', 'player3']
        self.card_knowledge = {'player1':[], 'player3':[]}

    # TODO : What if they don't have a guard card -- choose randomly to play

    def strategy_2(self):
        return

    pass

class Player3(Player):
    # TODO: write strat 3?

    def strategy_3(self):

    def __init__(self, strategy):
        super().__init__(strategy)
        self.strategy = self.strategy_3
        self.players_hand = self.players_hand
        self.player = 'player3'
        self.opponents = ['player1', 'player2']
        self.card_knowledge = {'player1':[], 'player2':[]}


    pass

        # pre-calculate and store these values for randomization of turns:
        # r, p, s = self.strategy
        # self.randmax = r + p + s


# TODO: write functions for identifying/keeping track of the round winner

# TODO: compare results of rounds and analyze our monte carlo sim results


if __name__ == '__main__':
    players = [1,2,3,4]
    # control = Player('control')

    cards_drawn, cards = new_game()
    # print(len(cards))

    cards = current_deck(cards, cards_drawn)

    deal_cards()

    #player 1 goes first

    # player_turn(Player1, Player1.strategy_1)
    # for player in players:
    #     player_turn(player, player.strategy)
    if len(players) != 1 or len(cards) != 0: #if no winner yet
        round()
    #recursion of rounds until a winner is identified for that game
    else:
        winner()









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





