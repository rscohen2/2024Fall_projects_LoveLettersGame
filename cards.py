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

    def do_something(self, what_to_do):
        pass


class Princess(Card):
    def __init__(self):
        super().__init__()
        self.__value = self.card_values['Princess']

    def play_card(self, player, players, cards_played, cards_in_play):
        # Princess-specific play logic
        print("Princess card played!")
        # Trigger player elimination if the Princess is played
        # player_is_out_of_the_round(player, players)
        card_played = 'Princess'
        # update_cards_played(card_played, cards_played)
er345        # TODO: sort of standardize the output for play_card for each card?





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
            #TODO move update_cards_played to Card class instead of subclass
            #correct properties of another class instead of parameters for the current game state

