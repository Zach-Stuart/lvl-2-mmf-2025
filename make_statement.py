# functions
def make_statement(statement, decoration):
    """"emphasises headings by adding decoration on the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# main routine
make_statement(statement="Instructions", decoration="*")