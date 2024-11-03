
import random

# cards = ['Princess', 'Countess', 'King','Prince','Prince','Handmaid','Handmaid','Baron','Baron','Priest','Priest','Guard','Guard','Guard','Guard','Guard']

def new_game():
    cards_drawn = []
    cards = ['Princess', 'Countess', 'King', 'Prince', 'Prince', 'Handmaid', 'Handmaid', 'Baron', 'Baron', 'Priest',
             'Priest', 'Guard', 'Guard', 'Guard', 'Guard', 'Guard']

    return cards_drawn, cards


def current_deck(cards, cards_drawn):
    for card in cards:
        if card in cards_drawn:
            cards.remove(card)
    return cards

def draw_a_card(cards_drawn, cards):
    i = random.randint(0, 15)
    card = cards[i]
    cards_drawn.append(card)
    return card

def play_card():
    """

    :return:
    """

def player_is_out_of_the_round(player_out, players):
    """

    :return:
    """
    players = players.remove(player_out)
    return players


if __name__ == '__main__':
    players = [1,2,3,4]
    cards_drawn, cards = new_game()
    print(len(cards))

    for player in players:
        cards = current_deck(cards, cards_drawn)
        card_drawn = draw_a_card(cards_drawn, cards)
        print(card_drawn)


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


