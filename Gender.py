"""
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

"""

class person():
    """
    Base class
    """
    gender = "Unknown"

    def getGender(self):
        return self.gender

class male(person):
    """
    Male subclass of person
    """
    gender = "Male"

    def getGender(self):
        return self.gender

class female(person):
    """
    Female subclass
    """
    gender = "Female"

    def getGender(self):
        return self.gender

if __name__ == "__main__":
    """
    """
    wonderboy = male()
    wonderwoman = female()

    print(wonderboy.getGender())
    print(wonderwoman.getGender())