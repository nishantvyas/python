"""
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to the Nth number.

"""

def fibonacci(total_iterations):

    first_number = 0
    second_number = 1
    fib_series = []

    if total_iterations < 2:
        print("Need atleast 2 iterations")
    else:
        fib_series.append(first_number)
        fib_series.append(second_number)
        for i in range(0,total_iterations-2):
            current = first_number + second_number
            fib_series.append(current)
            first_number = second_number
            second_number = current
        print (fib_series)

if __name__ == "__main__":
    fibonacci(1)
    fibonacci(2)
    fibonacci(5)
    fibonacci(10)
    fibonacci(20)
