# Check that users have entered a valid option based on a list
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
