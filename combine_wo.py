"""
Write a program to generate all sentences where subject is in
["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

"""

if __name__ == "__main__":
    """
    """

    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]


    for subject in subjects:
        for verb in verbs:
            for object in objects:
                print(f"{subject} {verb} {object}.")