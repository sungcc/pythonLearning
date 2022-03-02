import random
from re import L

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number greater than 1 and {x}\n'))
        
        if guess < random_number:
            print('Sorry, too low. Guess again')
        elif guess > random_number:
            print("Sorry, too high. Guess again")

    print("Yay, you guess the correct number")
            
            
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    life = 5
    print('Welcome to my number guessing game, u have 5 lifes to guess to right number')

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low    
        feedback = input(f"Is {guess} too high (H), or too low (L), or correct (C)?").lower()

        if life == 0:
            print('You ran out of life!')
            break

        elif feedback == 'h':
            high = guess - 1
            life = life - 1
            print(f"You have {life} life left")
        elif feedback == 'l':
            low = guess + 1
            life = life -1 
            print(f"You have {life} life left")
        elif feedback == 'c':
            print(f"yay The computer guessed your number, {guess}, correctly.")
        else:
            print("please enter a valid response")
            


        
    

