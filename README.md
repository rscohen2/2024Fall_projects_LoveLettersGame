# 2024Fall_projects

Becca Cohen, Sarah Griebel, Andrew Nam
IS597 - Fall 2024

Rough draft due date: 11.20 Wednesday

Monte Carlo Simulation for the card game Love Letters: To run the game simulation, access game_sim.py and run this file.

Game Overview

Premise: The premise of the game love letters is to be the last remaining player in the game, allowing you to deliver your letter to the princess over other suitors! In the case that the deck runs out before there is one remaining player, the player with the highest value card is the winner.

Simulation Design What we randomized

Shuffling the deck
Drawing the card
Dealing card in the beginning of the game
Choosing target for card effects
Guess when playing the Guard card (strategy 3 & 4)
Strategy Overview Each of these strategies take place when the player draws a guard, and is based on how they decide what card to guess.

Strategy 1: Guard-Princess
The player will always guess Princess.

Strategy 2: Guard-Max
The player will guess the maximum card that is still in play.

Strategy 3: Guard-Random-Remaining
The player will guess a random card from the cards still in play.

Strategy 4: Guard-Random-WholeDeck
The player will guess a random card from the entire deck.

Our Hypotheses

Hypothesis 1: Strategy one performs the worst since there is only one Princess card in the deck, and thus it is likely this guess will be incorrect and thus a bad strategy for guessing, resulting in less wins.
Hypothesis 2: Strategy 2 will beat randomly choosing from all cards in play (Strategy 3). This is because this strategy utilizes the frequency of cards left in the deck, which we expect should lead to more correct guesses and thus wins.
Hypothesis 3: Randomly choosing from all cards in play (Strategy 3) should outperform Strategy 4 which includes the whole deck, and thus cards no longer in play. Therefore, Strategy 4 has the potential to guess a card no longer in play, and is more likely to make an incorrect guess (as compared to Stategy 3 which only considers cards still in play) and have less wins.
Discussion/Results

Convergence? <insert line graphs for the 4 different players>

Strategy 3 (green line, guessing a random card from the cards left in play) seems to be performing the best, which is contrary to our expections. Strategy 2 and 4 perform the worst, which is interesting since we had expected Strategy 2 to outperform the other strategies by guessing the card with the highest frequency remaining in the deck and thus we predicted they would have a higher chance of making a correct guess.) Strategy 1 is coming in second, which is not what we had expected here since we had thought the Princess card only has 1 occurance in the deck, and would often be a false guess.

Future Directions

Testing strategies related to cards other than the guard card
