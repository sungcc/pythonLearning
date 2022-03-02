import random

def game():
    user_choice = input("'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer_choice = random.choice(['r', 'p', 's'])
    user_win = 0
    computer_win = 0 
    print(f'your choice is {user_choice}, computer choice is {computer_choice}')
    if user_choice == computer_choice:
        return "It's a tie"

    if is_win(user_choice, computer_choice):
        return "You Won"
        user_win += 1

    return "You lost"
    computer_win += 1
    print(computer_win)
    print(user_win)
    


def is_win(user_choice, computer_choice):
    if (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' or computer_choice == 'p'):
        return True

print(game())