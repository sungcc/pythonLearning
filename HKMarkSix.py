import random
numList = list(range(1, 50))
random.shuffle(numList)
result = numList[0: 7]

def random_draw():
    randomDraw = list(range(1,50))
    random.shuffle(randomDraw)
    randomDraw = randomDraw[0:7]
    match = 0
    for x in randomDraw:
        for y in result:
            if x == y:
                
                print(x)
                
    print(f'you just bought {randomDraw}\nThe result is {result}\n')

random_draw()