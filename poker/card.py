class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self.number = number

    def __repr__(self):
        return self.number + ' of ' + self.suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ['hearts', 'clubs', 'diamonds', 'spades']:
            self._suit = suit
        else: 
            print("This is not a suit")

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if number in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
            self._number = number
        else: print('not a valid card number')

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