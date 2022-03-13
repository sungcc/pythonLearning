from cards import deck
from player import player1

deck.shuffle()
deck.deal(player1)
print(player1.cards)