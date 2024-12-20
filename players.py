import random
# from game import *
from cards import *
from collections import Counter



class Player:
    """A competitor in the game."""
    players_hand = None
    card_played = None
    strategy = None

    def __init__(self, strategy, name):
        self.name = name
        self.strategy = strategy
        self.players_hand = []
        self.opponents = Counter()
        self.choices = Counter()
        self.player = None
        self.card_knowledge = {}
        self.card_selected_to_play = None
        self.player_remaining = True
        self.player_protected = False


    def checkGuard(self):
        """
        This function checks for the Guard card in a player's hand. If the Guard card exists,
        it will be returned (and therefore, played). This is the case for all player strategies.

        :param self: Player in the game
        :return: Guard card object if Guard in the hand

        >>> player = Player("Player1", "strategy_1")
        >>> player.players_hand = [Guard()]
        >>> result = player.checkGuard()
        >>> "Guard" in str(type(result))
        True

        """
        for card in self.players_hand:
            if "Guard" in str(type(card)):
                return(card)

    def checkCountessCondition(self):
        """
        This function checks whether the Countess AND the King AND/OR Prince is in the player's hand.
        If so, it will return True. This is because of the rule that if a player has both the
        Countess and the King or the Prince, they must play the Countess card.

        :param self: Player in the game
        :return: True or False (depending on if the Countess is in the player's hand and the
        King and/or Prince is also in the player's hand)

        >>> player = Player("Player1", "strategy_1")
        >>> player.players_hand = [Countess(), King()]
        >>> player.checkCountessCondition()
        True

        >>> player.players_hand = [Countess(), Prince()]
        >>> player.checkCountessCondition()
        True

        >>> player.players_hand = [Countess(), Princess()]
        >>> player.checkCountessCondition()
        False

        """
        #cardTypes = [type(i) for i in self.players_hand]
        cardTypes = [card.__class__.__name__ for card in self.players_hand]
        if "Countess" in cardTypes:
            if "Prince" in cardTypes and "Princess" not in cardTypes:
                return True
            elif "King" in cardTypes:
                return True
            else:
                return False
        else:
            return False

    def chooseRandomCard(self):
        """
        This function chooses a random card from a player's hand.

        :param self: Player in the game
        :return: card object
        """
        card = self.players_hand[random.randint(0,len(self.players_hand)-1)]
        return(card)


    def card_to_play(self):
        """
        This strategy decides on a card to play. It first checks on whether the Countess Condition
        is true (which would mean the Countess must be played), and then checks for the Guard Card
        (which would mean the Guard must be played). If one of those are true, it returns the
         card for that condition. If neither of those are True, then it plays
        a random card.

        :param self: Player in the game
        :return: Countess card object, Guard card object, or random card object

        >>> player = Player("Player1", "strategy_1")
        >>> guard_card = Guard()
        >>> countess_card = Countess()
        >>> player.players_hand = [guard_card]
        >>> result = player.card_to_play()
        >>> "Guard" in str(type(result))
        True

        """

        if not self.checkCountessCondition():
            guardCard = self.checkGuard()
            if guardCard:
                return guardCard
            else:
                cardSelected = self.chooseRandomCard()
                return cardSelected
        else:
            countessCardList = [card for card in self.players_hand if "Countess" in card.__class__.__name__]
            if countessCardList:
                cardSelected = countessCardList[0]
            else:
                cardSelected = self.chooseRandomCard()
        self.card_selected_to_play = cardSelected
        return(cardSelected)


    def guess_card(self, possible_cards, wholeDeck):
        """
        This function is used to decide what the player's card guess will be, when they
        are playing the Guard card. This is where our player strategies are also defined,
        as the guess logic will differ based on whether they are strategy 1, 2, 3, or 4.

        :param self: Player in the game
        :param possible_cards: a list of card objects that are still in play in the game
        :param wholeDeck: a list of the whole deck of card objects
        :return: a string card name, as the guess
        """

        def getCardValue(card):
            return Card.card_values[card]

        possible_cards_without_guards = []
        for card in possible_cards:
            if card != "Guard":
                possible_cards_without_guards.append(card)
        possible_cards = possible_cards_without_guards

        if self.strategy == "strategy_1":
            return "Princess"

        elif self.strategy == "strategy_2":
            for card in self.players_hand:
                if card in possible_cards:
                    possible_cards.remove(card)
                maxCount = max(possible_cards.count(card) for card in possible_cards)
                cards_withMaxCount = [card for card in possible_cards if possible_cards.count(card) == maxCount]
                guess = random.choice(cards_withMaxCount)
                return guess

        elif self.strategy == "strategy_3":
            for card in self.players_hand:
                if card in possible_cards:
                    possible_cards.remove(card)
                randomPick = random.choice(possible_cards)
                return randomPick

        elif self.strategy == "strategy_4":
            whole_deck_without_guards = []
            for card in wholeDeck:
                if card.__class__.__name__ != "Guard":
                    whole_deck_without_guards.append(card)
            return random.choice(whole_deck_without_guards).__class__.__name__

        elif self.strategy == "strategy_5":
            for card in self.players_hand:
                if card in possible_cards:
                    possible_cards.remove(card)
                maxCount = max(possible_cards.count(card) for card in possible_cards)
                cards_withMaxCount = [card for card in possible_cards if possible_cards.count(card) == maxCount]
                sorted_max = sorted(cards_withMaxCount, key=getCardValue, reverse=True)
                guess = sorted_max[0]
                return guess

    def remove_card(self, card):
        """
        This function removes a card from a player's hand.

        :param card: card object
        :return: the player's hand without that card object
        """
        if card in self.players_hand:
            self.players_hand.remove(card)

