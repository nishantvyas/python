"""
Change Return Program - The user enters a cost and then the amount of money given.
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
"""

def format_number(number, precision=2):

    return '{number:.{digits}f}'.format(number=number, digits=precision)

def money_to_giveback(cost_of_item, user_paid):

    if cost_of_item < 0 or user_paid < 0:
        print("Cost of item Or the User paid amount has to br greater than 0")
        return

    money_to_return = float(format_number(user_paid,2)) - float(format_number(cost_of_item,2))

    if money_to_return == 0:
        print("Thanks for doing business! Good day!")
        return
    elif money_to_return < 0:
        flag_owe = "We"
    else:
        flag_owe = "You"

    
    print(f"{flag_owe} owe, {format_number(money_to_return,2)}")

if __name__ == "__main__":

    money_to_giveback(30,35)
    money_to_giveback(30.99,35.001)
    money_to_giveback(35.99,35.001)
