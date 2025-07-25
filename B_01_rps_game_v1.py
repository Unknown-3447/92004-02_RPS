import random


# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user input matches any item in valid_ans
            if user_response in valid_ans:
                return user_response

            # Check if the user input matches the first letter of any item in valid_ans
            elif user_response == item[0]:
                return item

        # If user input doesn't match any valid option, print error message
        print(error)
        print()


# Displays instructions
def instruction():
    print('''

    **** Instructions ****

Welcome to the Paper Scissors Rock game! Here's how to play:

1. The game will ask if you want to read the instructions. Enter 'yes' or 'no' (or just 'y' or 'n').

2. Choose your move by typing 'paper', 'scissors', or 'rock' when prompted. You can also use the first letter of each 
word (p, s, or r).

3. The computer will randomly choose its move.

4. The winner of each round is determined as follows:
   - Paper beats Rock
   - Scissors beats Paper
   - Rock beats Scissors
   - If both players choose the same, it's a tie

5. The game will display the result of each round.

6. You can play multiple rounds. After each round, you'll be asked if you want to play again.

7. When you're done playing, the game will show your final score.

Remember:
- Your input is not case-sensitive, so 'ROCK', 'rock', and 'RoCk' are all valid.
- If you make a typo, the game will ask you to enter a valid option.

Good luck and have fun!

    ''')


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:

        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# compares user / computer choice and returns result (win / lose / tie)
def rps_compare(user, comp):
    # If the user and the computer choice is the same, it's a tie
    if user == comp:
        result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        result = "lose"

    return result  # Added missing return statement


# Main routine Starts here

# Initialise game variable
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("Rock / Paper / Scissors Game")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history / Statistics area
