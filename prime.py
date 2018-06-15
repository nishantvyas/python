"""
Program to find prime number.
Using 3 different approaches and timing it for efficiency.

"""

import timeit

def is_prime_with_factors_1(givennumber):
    """
    default way of checking if given number is prime and printing all the factors
    :param givennumber:
    :return:
    """
    total_factors = 0
    factors = []

    if givennumber <= 1:
        print("Enter any number larger than 1")
        return
    else:
        for i in range(2,givennumber+1):
            if givennumber % i == 0:
                total_factors += 1
                factors.append(i)

    if total_factors > 1:
        print(f"Number {givennumber} is NOT prime.")
        print(f"Factors are {factors}")
    else:
        print(f"Number {givennumber} is PRIME")


    return

def is_prime_1(givennumber):
    """
    checking if given number is prime and short circuiting when found factors.
    :param givennumber:
    :return:
    """
    total_factors = 0

    if givennumber <= 1:
        print("Enter any number larger than 1")
        return
    else:
        for i in range(2,givennumber+1):
            if givennumber % i == 0:
                total_factors += 1

            if total_factors > 1:
                print(f"Number {givennumber} is NOT prime.")
                return

    print(f"Number {givennumber} is PRIME")

    return

def is_prime_sqrt(givennumber):
    """
    onjecture: Every composite number has a proper factor less than or equal to its square root.

    Proof: We use proof by contradiction.  Suppose n is composite. Then, we can write n = ab, where a and b are both between 1 and n.
    If both a > sqrt{n} and b> sqrt{n}, then (a)(b) > (sqrt{n})(sqrt{n}) which means that ab > n. This contradicts our assumption that ab = n.
    Hence, at least one of a, b is less than or equal to \sqrt{n}. That is, if n is composite,  , then n has a prime factor p <= sqrt{n}.

    :param givennumber:
    :return:
    """
    total_factors = 0

    if givennumber <= 1:
        print("Enter any number larger than 1")
        return
    else:
        for i in range(2,int(givennumber ** 0.5) +1):
            if givennumber % i == 0:
                total_factors += 1

            if total_factors >= 1:
                print(f"Number {givennumber} is NOT prime.")
                return

    print(f"Number {givennumber} is PRIME")

    return


if __name__ == "__main__":
    """
    """
    print("***** Prime numbers with Factors *****")
    is_prime_with_factors_1(3)
    is_prime_with_factors_1(5)
    is_prime_with_factors_1(13)
    is_prime_with_factors_1(21)
    is_prime_with_factors_1(35)
    is_prime_with_factors_1(500)

    print("***** Prime numbers check with loop/break method *****")
    is_prime_1(3)
    is_prime_1(5)
    is_prime_1(13)
    is_prime_1(21)
    is_prime_1(35)
    is_prime_1(500)

    print("***** Prime numbers check with sqrt method *****")
    is_prime_sqrt(3)
    is_prime_sqrt(5)
    is_prime_sqrt(13)
    is_prime_sqrt(35)
    is_prime_sqrt(21)
    is_prime_sqrt(500)

    ###print(timeit.timeit('is_prime_with_factors_1(500)', globals=globals(), number=100))