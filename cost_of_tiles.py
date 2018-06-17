"""
Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of
width and height, using a cost entered by the user.
"""

def house_sqft(width=None, height=None):
    return int(width * height)

def cost_of_project(sqft=None, dollar=None):
    return int(sqft * dollar)

if __name__ == "__main__":

    width = int(input("Enter the width:"))
    height = int(input("Enter the height:"))
    dollar = int(input("Enter the cost of tile per sqft:"))

    print(f"Total cost of project will be {cost_of_project(sqft=house_sqft(width=width, height=height),dollar=dollar)}")