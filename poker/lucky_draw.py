import random
# this practice draw a random card

card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suit = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

def draw():
    randomList = []
    for i in card:
        for j in suit:
            randomList.append(i + " of " + j)
    random.shuffle(randomList)
    print(randomList[0])
    
    
draw()