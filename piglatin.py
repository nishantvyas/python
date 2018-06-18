"""
Pig Latin - Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed
to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
Read Wikipedia for more information on rules.
"""

def to_piglatin(string=None):

    string_to_convert = string.split()
    pig_latin = []


    for sub_string in string_to_convert:
        pig_prefix = sub_string[1:]
        pig_suffix = sub_string[0] + "ay"
        pig_latin.append(pig_prefix + pig_suffix)

    return ' '.join(pig_latin)

if __name__ == "__main__":

    print(to_piglatin("test"))
    print(to_piglatin("soup was good"))