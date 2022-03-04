from card import Card

class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)

def populate(self):
    suits = ["hearts", "clubs", "diamonds", "spades"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    cards = []
    for suit in suits:
        for number in numbers:
            cards.append( Card(suit, number))
    
    self._cards = cards
    

mydeck = Deck()
print(mydeck)