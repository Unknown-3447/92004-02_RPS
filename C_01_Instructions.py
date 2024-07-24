# Function to check user input against a list of valid options
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


# Displays instructions to user
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


# Main routine
print()
print("Rock / Paper / Scissors Game")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()
