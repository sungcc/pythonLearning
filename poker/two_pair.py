# this practice determine if our hands are 2 pairs or not
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suit = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    def __repr__(self):
        
        return self.value + ' of ' + self.suit

Sung = Card('6', 'Diamonds')
print(Sung.suit)