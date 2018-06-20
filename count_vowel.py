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

    if string == None:
        print("Enter valid staring")
        return

    for char in string:
        if char in vowel:
            vowel_count += 1

    print(f"Total vowels are: {vowel_count}")

if __name__ == "__main__":
    """
    """
    count_vowel("My name is Nishant")
