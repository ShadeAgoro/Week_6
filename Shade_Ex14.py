import random

def welcome():
    user_name = input('Please enter your name: ')
    print(f'Welcome to the game {user_name}!')
# created a welcome function in addition to pre-existing user, computer and decide winner functions from last week

def user_choose_weapon():
    user_decision = ""
    # input function for user to select R, P or S
    users_input = input(
        "Please enter either R for Rock, P for Paper or S for Scissors: ").upper()
    # if conditions to define R,P or S variables and else statement in the event of the user trying to input a value not
    # recognised by the game
    if users_input == 'R':
        user_decision = 'Rock'
    elif users_input == 'P':
        user_decision = 'Paper'
    elif users_input == 'S':
        user_decision = 'Scissors'
    else:
        print('Sorry, that is not an option. Try again, pick either R, P, or S')
        user_decision = 'Not available'
    return user_decision


def computer_choose_weapon():
    options = [0, 1, 2]
    computer_number = random.choice(options)
    if computer_number == 0:
        computer_decision = 'Rock'
    elif computer_number == 1:
        computer_decision = 'Paper'
    else:
        computer_decision = 'Scissors'
    print("Computer decided", computer_decision)
    return computer_decision


def decide_winner(users_decision, computer_decision):
    if users_decision == 'Not available':
        print('Please try again!')
    elif users_decision == computer_decision:
        print('It is a tie!')
    elif users_decision == 'Rock':
        if computer_decision == 'Scissors':
            print('Congratulations, you won! - Play again!')
        else:
            print('Sorry, you lost! - Play again!')
    elif users_decision == 'Paper':
        if computer_decision == 'Rock':
            print('Congratulations, you won! - Play again!')
        else:
            print('Sorry, you lost! - Play again!')
    else:
        if computer_decision == 'Paper':
            print('Congratulations, you won! - Play again!')
        else:
            print('Sorry, you lost! - Play again!')


# included a main trick with welcome function and play again function from while loop
if __name__ == '__main__':
    welcome()
    play_again = "Y"
    while play_again == "Y":
        user_weapon = user_choose_weapon()
        computer_weapon = computer_choose_weapon()
        decide_winner(user_weapon, computer_weapon)
        play_again = input("Do you want to play again? (Y/N)").upper()
