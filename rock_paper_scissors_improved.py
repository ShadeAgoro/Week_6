
import random, Shade_Ex14

# created a welcome and exit game function

def user_choose_weapon():
    user_decision = ""
    # input function for user to select R, P or S
    users_input = input(
        "Welcome to Rock, Paper, Scissors! Please enter either R for Rock, P for Paper or S for Scissors: ").upper()
    # if conditions to define R,P or S variables and else statement in the event of the user trying to input a value not
    # recognised by the game
    if users_input == 'R':
        users_decision = 'Rock'
    elif users_input == 'P':
        users_decision = 'Paper'
    elif users_input == 'S':
        users_decision = 'Scissors'
    else:
        print('Sorry, that is not an option. Try again, pick either R, P, or S')
        users_decision = 'Not available'
    return user_decision

# highlight code, right click, select "refactor", then "extract method"
user_weapon = user_choose_weapon()


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


# assigning numbers to rock, paper or scissors variables for computer to randomly select in the game
computer_weapon = computer_choose_weapon()

# Set of if statements to compare the user's decision with the computer's decision and give a result
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

if __name__ == '__main__':
    decide_winner(user_weapon, computer_weapon)

