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
    elif money_to_return > 0:

        money_to_return_in_cents = round(money_to_return * 100)

        dollars = int(money_to_return_in_cents / 100)
        money_to_return_in_cents = money_to_return_in_cents % 100


        quarters = int(money_to_return_in_cents / 25)
        money_to_return_in_cents = money_to_return_in_cents % 25


        dimes = int(money_to_return_in_cents / 10)
        money_to_return_in_cents = money_to_return_in_cents % 10


        nickles = int(money_to_return_in_cents / 5)
        money_to_return_in_cents = money_to_return_in_cents % 5

        pennys = float(format_number(money_to_return_in_cents, 2))

        print(f"Here's your change, {dollars} Dollars, {quarters} Quarters, {dimes} Dimes, {nickles} Nickles, {pennys} Pennys")
    else:
        still_to_pay = money_to_return * -1
        print(f"You still owe us, {format_number(still_to_pay,2)}")

    return

if __name__ == "__main__":

    money_to_giveback(30,35)
    money_to_giveback(30.21,35)
    money_to_giveback(35.99,35.001)
