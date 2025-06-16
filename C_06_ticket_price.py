# Functions go here

def int_check(question):
    """Checks users enter an integer"""
    error = "Oops - please enter an integer"
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)
        if response.strip() != "":
            return response
        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first letter of a word
    from a list of valid responses"""
    while True:
        response = input(question).lower()
        for item in valid_ans_list:
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here

# Initialise valid options
payment_ans = ('cash', 'credit')
MAX_TICKETS = 5
tickets_sold = 0

# Ticket Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# Keep going until 5 valid tickets are sold
while tickets_sold < MAX_TICKETS:
    print(f"\nTicket {tickets_sold + 1} of {MAX_TICKETS}")

    name = not_blank("Name: ")
    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue

    # Determine ticket price
    if age < 16:
        ticket_price = CHILD_PRICE
    elif age < 65:
        ticket_price = ADULT_PRICE
    else:
        ticket_price = SENIOR_PRICE

    # Ask user for payment method
    pay_method = string_check("Payment method (cash/credit): ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    total_to_pay = ticket_price + surcharge

    print(f"\n{name}'s ticket cost: ${ticket_price:.2f}")
    print(f"Payment method: {pay_method} | Surcharge: ${surcharge:.2f}")
    print(f"Total payable: ${total_to_pay:.2f}\n")

    tickets_sold += 1

# After the loop finishes
print("\n🎉 You sold all the tickets!")
