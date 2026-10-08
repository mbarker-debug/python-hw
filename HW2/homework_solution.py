def calculate_ticket_price(age, is_weekend, is_member):
    """
    Calculate a movie ticket price.

    Inputs:
        age: Customer's age.
        is_weekend: True if it is a weekend.
        is_member: True if the customer is a theater member.

    Output:
        The final ticket price.
    """
    if age < 0 or age > 120:
        return False

    if age < 13:
        price = 8
    elif age <= 64:
        price = 12
    else:
        price = 9
    
    if is_weekend:
        price = price + 3

    if is_member:
        price = price - 2

    return price

def calculate_total(ticket_price, wants_popcorn):
    """
    Calculate the total theater cost.

    Inputs:
        ticket_price: Price of the movie ticket.
        wants_popcorn: True if the customer wants popcorn.

    Output:
        The final cost.
    """
    if wants_popcorn:
        total = ticket_price + 6
    else:
        total = ticket_price

    return total


age = float(input("Enter your age: "))

weekend_answer = input("Is it a weekend? Enter yes or no: ")

member_answer = input("Are you a theater member? Enter yes or no: ")

popcorn_answer = input("Would you like popcorn? Enter yes or no: ")

if weekend_answer == "yes" or weekend_answer == "Yes":
    is_weekend = True
else:
    is_weekend = False

if member_answer == "yes" or member_answer == "Yes":
    is_member = True
else:
    is_member = False

if popcorn_answer == "yes" or popcorn_answer == "Yes":
    wants_popcorn = True
else:
    wants_popcorn = False

ticket_price = calculate_ticket_price(
    age,
    is_weekend,
    is_member
)

if ticket_price == False:
    print("That age is not valid.")
else:
    total_cost = calculate_total(ticket_price, wants_popcorn)

    print(f"Ticket price: ${ticket_price:.2f}")
    print(f"Final cost: ${total_cost:.2f}")