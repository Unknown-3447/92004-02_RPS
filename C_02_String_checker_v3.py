# Function to check user input against a list of valid options
def string_checker(question, valid_ans=['yes', 'no']):
    error = f"Please enter a valid option from the following list {valid_ans}"

    while True:
        user_response = input(question).lower()

        # Check if the user input matches any item in valid_ans
        if user_response in valid_ans:
            return user_response

        # Check if the user input matches the first letter of any item in valid_ans
        for item in valid_ans:
            if user_response == item[0].lower():
                return item

        # If user input doesn't match any valid option, print error message
        print(error)
        print()


# Main routine

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instructions? ")

print("You chose:", want_instructions)

user_choice = string_checker("Choose: ", rps_list)
print("You chose ", user_choice)
