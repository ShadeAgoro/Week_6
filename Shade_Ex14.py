# EXERCISE 14
# import random
# imported random module for computer to select values at random during the game

# play = ['rock', 'paper', 'scissors']
# created list of values for play variable

# users_input = input("Enter a value of (R, P, or S): ")
# created a variable to assign user's input to values in play list

# if users_input == 'R':S
#   users_decision = 'rock'
# elif users_input == 'P':
#     users_decision = 'paper'
# elif users_input == 'S':
#     users_decision = 'scissors'
#else:
#    print('Sorry, this is not an option. Try again, pick either R, P, or S.')
# used an if conditional statement to create outputs for user's input
# prints a message if any values other than R, P or S is inputted e.g. Q

# comp_number = play[random.randint(0,2)]
# randint method for comp game variable to selects random integers assigned to the value of rock, paper, scissors

# if comp_number == 0:
#   comp_decision = 'rock'
# if comp_number == 1:
#   comp_decision = 'paper'
# else:
#    comp_decision = 'scissors'

# print(f"Computer chose {comp_decision}.")
# print the random object that the computer generates

# if users_decision == comp_decision:
#    print('It is a tie!')

# elif users_decision == 'rock':
#    if comp_decision == 'scissors':
#        print('Rock smashes scissors!')
#    else:
#        print('Better luck next time!')

# elif users_decision == 'paper':
#    if comp_decision == 'scissors':
#        print("You win! Scissors cuts paper")
#   else:
#        print("You lose - paper is cut by scissors!")

# elif users_decision == 'paper':
#if comp_decision == 'rock':
#print("You win! Paper wraps rock")
#else:
#      print("Oh no - you lost!")

# victoria's feedback
# create functions by selecting code, clicking on "refactor", then "extract method"
# for user choice and computer choice and user vs computer
# this automatically brings up 'def' as well as the method that was created from selecting code
# i.e. user_choose_weapon, computer_choose_weapon and decide winner
# then type "return" to return code at the end of if statements
# in first if statement, we created line 67 with empty parentheses, typed "return at the end
# we also created a variable on the left hand side - "user_weapon = user_choose_weapon"
# in second if statement, we returned code and created variable "computer_weapon = computer_choose_weapon"
# we also printed messaged "computer decided, computer_decision" to tidy up the terminal
# it was feeding back user decision in terminal but not computer decision
# in third if statement, we put variables 'users_decision' and 'computer_decision' in empty brackets that
# came with creating the function "decide_winner(user_weapon, computer_weapon)" (line 134)

import random

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

