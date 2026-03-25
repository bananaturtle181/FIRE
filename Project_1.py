import sys

def main():
    expense = {}

    #Obtaining arguments from user 
    arguments = sys.argv

    #Validating if user provided correct number of arguments
    if len(arguments) != 3: 
        sys.exit("Invalid number of arguments")

    category = arguments[1]

    #Validating if expense is an integer and greater than 0
    try:
        amount = int(arguments[2])
    except ValueError:
        sys.exit("Expense is not an integer")


    if amount <= 0:
        sys.exit("Expense is less than 0")
    else: 
        expense[category] = amount
    return expense

print(main())