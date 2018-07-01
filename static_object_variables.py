"""
Class to test static vs object variables in class.
Question: Should variable be define under class or under __init__
"""

class MyClass:
    """

    """
    ## STatic method defined under class
    static_elem = 123

    def __init__(self):
        ##object method defined under __init__
        self.object_elem = 456


if __name__ == "__main__":
    """
    """
    c1 = MyClass()
    c2 = MyClass()

    # Initial values of both elements, Nothing new so far...
    print(f"c1 static element {c1.static_elem} and c1 object element {c1.object_elem}")
    print(f"c2 static element {c2.static_elem} and c2 object element {c2.object_elem}")

    # Let's try changing the static element
    MyClass.static_elem = 999
    print("Changing Class static element,")

    print(f"c1 static element {c1.static_elem} and c1 object element {c1.object_elem}")
    print(f"c2 static element {c2.static_elem} and c2 object element {c2.object_elem}")

    # Now, let's try changing the object element
    c1.object_elem = 888
    print("Changing Object element,")

    print(f"c1 static element {c1.static_elem} and c1 object element {c1.object_elem}")
    print(f"c2 static element {c2.static_elem} and c2 object element {c2.object_elem}")

    #When changed the class element, it changed for both objects. But, when changed the object element, the other object remained unchanged.
