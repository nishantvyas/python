"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

def createMatrix(rows=1,columns=2):
    """

    :param rows:
    :param columns:
    :return:
    """
    return [[i*j for j in range(columns)] for i in range(rows)]


if __name__ == "__main__":
    """
    """
    user_input = input("Enter number of rows and columns in matrix, e.g. 2,3 ::")
    rows,columns = user_input.split(",")
    my_matrix = createMatrix(rows=int(rows), columns=int(columns))
    print(my_matrix)