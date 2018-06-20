"""
Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

def count_vowel(string=None):
    """

    :param String:
    :return:
    """
    vowel = ['a','e','i','o','u']
    vowel_count = 0
    vowel_count_dict = {'a':0,'e':0,'i':0,'o':0,'u':0}

    if string == None:
        print("Enter valid staring")
        return

    for char in string:
        if char in vowel:
            vowel_count += 1
            vowel_count_dict[char] += 1

    print(f"Total vowels are: {vowel_count}")
    print(f"Count for each vowel {vowel_count_dict}")

if __name__ == "__main__":
    """
    """
    count_vowel("My name is Nishant")
