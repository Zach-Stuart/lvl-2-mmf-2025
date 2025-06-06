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


def instructions():
    make_statement("Instructions", "🔍")

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

make_statement("Mini-Movie Fundraiser Program", "🎬")

print()
want_instructions = string_check("Would you like to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    name = input("Name: ")

    # if name is exit code, break the loop
    if name == "xxx":
        break

    # ask user for their name and check it's not blank
    name = not_blank("Name: ")

    # ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error and success message
    if age < 12:
        print(f"{name} is too young.")
        continue
    elif age > 120:
        print(f"{name} is too old.")
        continue
    else:
        pass

    # ask user for payment method (cash or credit, ca or cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})!")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets)!")
else:
    print(f"You have sold {tickets_sold} tickets out of {MAX_TICKETS} tickets.")
