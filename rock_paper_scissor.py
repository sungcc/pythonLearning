import random
import math

def game():
    user_choice = input("'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer_choice = random.choice(['r', 'p', 's'])


    print(f'your choice is {user_choice}, computer choice is {computer_choice}')
    if user_choice == computer_choice:
        return (0, user_choice, computer_choice)

    if is_win(user_choice, computer_choice):
        return (1, user_choice, computer_choice)

    return (-1, user_choice, computer_choice)

    


def is_win(user_choice, computer_choice):
    if (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' or computer_choice == 'p'):
        return True

def play_best_of(n):
    user_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)

    while user_wins < wins_necessary and computer_wins < wins_necessary:
        result, user_choice, computer_choice = game()
        if result == 0:
            print(f"It's a tie. You and the computer have both chosen {user_choice}.\n")
        elif result == 1:
            user_wins += 1
            print(f"You won, you chose {user_choice} and computer chose {computer_choice}\n")
        else:
            computer_wins += 0
            print(f"You lost, you chose {user_choice} and computer chose {computer_choice}\n")
    
    if user_wins > computer_wins:
        print(f"You have won the best out of {n}, congrat ")
    else: 
        print("You have lost the best out of {n}, try again")


if __name__ == '__main__':
    play_best_of(3)