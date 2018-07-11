"""
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

"""
class transactions():
    """

    """
    def __init__(self):
        """

        """
        self.total = 0

    def parseInput(self, user_input):
        """

        :param user_input:
        :return:
        """
        values = user_input.split(" ")
        return values[0], int(values[1])

    def transact(self, user_input):
        """

        :param operation:
        :param amount:
        :return:
        """
        operation, amount = self.parseInput(user_input)

        if operation == "D":
            self.total += amount
        elif operation == "W":
            self.total -= amount
        else:
            print("Invalid transaction")
            return

if __name__ == "__main__":
    """
    """
    my_account = transactions()

    print("Enter the transaction details:")

    while True:
        user_input = input();
        if not user_input:
            break
        my_account.transact(user_input)


    print(f"Current account total is {my_account.total}")