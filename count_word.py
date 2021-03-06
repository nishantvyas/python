"""
Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary.
"""

def count_word(string=None):
    world_list = string.split()
    return len(world_list)

if __name__ == "__main__":
    """
    """
    #print("String has " + f"{count_word('test')}" + " words")
    #print("String has " + f"{count_word('My name is Nishant.')}" + " words")
    words = 0
    file = "textfile.txt"
    with open(file) as f:
        for line in f:
            words += count_word(line.strip())

    print(f"Total words in file {file} are {words}")