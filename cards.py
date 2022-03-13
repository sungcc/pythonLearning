import random

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        valueName = ''
        suitName = ''
        if self.value == 0:
            valueName = 'Two'
        elif self.value == 1:
            valueName = 'Three'
        elif self.value == 2:
            valueName = 'Four'
        elif self.value == 3:
            valueName = 'Five'
        elif self.value == 4:
            valueName = 'Six'
        elif self.value == 5:
            valueName = 'Seven'
        elif self.value == 6:
            valueName ='Eight'
        elif self.value == 7:
            valueName ='Nine'
        elif self.value == 8:
            valueName = 'Ten'
        elif self.value == 9:
            valueName = 'Jack'
        elif self.value == 10:
            valueName = 'Queen'
        elif self.value == 11:
            valueName = 'King'
        elif self.value == 12:
            valueName = 'Ace'
        if self.suit == 0:
            suitName = "Spades"
        elif self.suit == 1:
            suitName = "Hearts"
        elif self.suit == 2:
            suitName = "Clubs"
        elif self.suit == 3:
            suitName = "Diamonds"
        return valueName + ' of ' + suitName

        
class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(value, suit)) for suit in suits] for value in values]

    def shuffle(self):
        random.shuffle(self)
        print('deck shuffled')

    def deal(self):
        print(self.pop(0))


deck = StandardDeck()
    