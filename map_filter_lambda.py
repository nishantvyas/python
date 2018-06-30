"""
SImple program to try map filter and lambda functions
"""
if __name__ == "__main__":

    my_list = [1,2,3,4,5,6,7,8,9,10]

    ### find the even numbers using lambda and filter

    even_list = list(filter(lambda x: (x%2 == 0), my_list))
    print(even_list)

    ### find square using lambda and map
    square_list = list(map(lambda x: x*x, my_list))
    print(square_list)

