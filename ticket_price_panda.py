import pandas


# functions
def make_statement(statement, decoration):
    """"emphasises headings by adding decoration on the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """checks that users enter the full word
    or the 'n' letter/s of the word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if response is the entire word
            if response == item:
                return item

            # check if it's the "n" letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def not_blank(question):
    """checks that user response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again\n")


def int_check(question):
    """checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # return response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# main routine

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# loop for testing
while True:
    name = input("Name: ")

    # if name is exit code, break the loop
    if name == "xxx":
        break

    # ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error and success message
    if age < 12:
        print(f"{name} is too young.")
        continue

    # child ticket price ($7.50)
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    # adult ticket ($10.50)
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # senior citizen ticket ($6.50)
    elif 65 <= age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old.")
        continue

    # ask user for payment method (cash or credit, ca or cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
         surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost and surcharge
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate total payable and profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# work out total paid and total profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

print(mini_movie_frame)
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")