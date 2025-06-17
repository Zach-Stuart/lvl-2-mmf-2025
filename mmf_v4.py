import pandas
import random


# functions
def make_statement(statement, decoration):
    """"emphasises headings by adding decoration on the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


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


# currency formatting
def currency(x):
    return "${:.2f}".format(x)


def instructions():
    print(make_statement("Instructions", "🔍"))

    print('''
    
    For each ticket holder, enter:
    - Their name
    - Their age
    - Their payment method (cash / credit)
    
    The program will record the ticket sale and calculate the cost (and the profit).
    
    Once you have either sold all the tickets or entered the exit code ('xxx'), the program will display the sales information and write the data to a text file.
    
    It will also choose one lucky ticket holder who wins the draw (their ticket is free).
    
    ''')


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

# initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

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

# main heading
print(make_statement("Mini-Movie Fundraiser Program", "🎬"))

# ask user if they want to see instructions
# display instructions if necessary
print()
want_instructions = string_check("Would you like to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# loop to get name, age and payment details
while tickets_sold < MAX_TICKETS:
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
    print()

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost and surcharge
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# end of ticket loop

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate total payable and profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# work out total paid and total profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# choose random winner
winner = random.choice(all_names)

# find index of winner (ie: position in list)
winner_index = all_names.index(winner)

# find total won
total_won = mini_movie_frame.at[winner_index, 'Total']

# retrieve winner ticket price and profit
# so that we can adjust profit numbers and exclude winning ticket
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# currency formatting (use currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# print mini movie frame
mini_movie_string = mini_movie_frame.to_string(index=False)

print()
total_paid_string = f"Total Paid: ${total_paid:.2f}"
total_profit_string = f"Total Profit: ${total_profit:.2f}"

# winner announcement
lucky_winner_string = f"The lucky winner is {winner}! Their ticket worth ${total_won:.2f} is free!"
final_total_paid_string = make_statement(f"Total Paid is now ${total_paid - ticket_won:.2f}!")
final_profit_string = make_statement(f"Total Profit is now ${total_profit - profit_won:.2f}!")

if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement(f"You have sold all the tickets" 
                                     f"(ie: {MAX_TICKETS} tickets)", "-")
else:
    num_sold_string = make_statement(f"You have sold {tickets_sold} tickets out of {MAX_TICKETS} tickets.")

# additional strings / headings
heading_string = make_statement("Mini Movie Fundraiser", "*")
ticket_details_heading = make_statement("Ticket Details", "*")
raffle_heading = make_statement("Raffle Winner", "*")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit", "*")

adjusted_explanation = (f"We have given away a ticket worth ${ticket_won:.2f}, "
                        f"meaning sales have decreased by ${ticket_won:.2f} and our profit "
                        f"decreased by ${ticket_won:.2f}")

# list of strings to be outputted / written to file
to_write = [heading_string, "\n", ticket_details_heading,
            mini_movie_string, "\n", total_paid_string,
            total_profit_string, "\n", raffle_heading,
            lucky_winner_string, "\n", adjusted_sales_heading,
            adjusted_explanation, "\n", final_total_paid_string,
            final_profit_string, "\n", num_sold_string]

# print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = "MMF_ticket_details"
write_to = "{},txt".format(file_name)

text_file = open(write_to, "w+")

# write item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")