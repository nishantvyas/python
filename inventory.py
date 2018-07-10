"""
Product Inventory Project - Create a simple program to manage an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""

class product():
    """
    blue print for product information
    """
    def __init__(self, id, name, price, unit):
        """
        init default variables for product/item i.e. name, id, price
        """

        self.id = id
        self.name = name
        self.price = price
        self.unit = unit

    def getProductDetail(self, *args):
        """
        get detail of one or more attributes of product
        :return:
        """
        item_json = {}

        if len(args) == 0:
            item_json = {"id": self.id, "name": self.name, "price": self.price, "unit": self.unit}
            return item_json
        else:
            for arg in args:
                if arg == "id":
                    item_json[arg]=self.id
                elif arg=="name":
                    item_json[arg] = self.name
                elif arg == "price":
                    item_json[arg] = self.price
                elif arg=="unit":
                    item_json[arg] = self.unit
                else:
                    item_json = None

            return item_json

class inventory():
    """
    inventory class blueprint
    """
    def __init__(self):
        """
        initialize inventory class
        """
        self.inventory = {}

    def getProductItemId(self, productObject):
        """

        :return:
        """
        return productObject.id

    def setItemObject(self, productObject, quantity):
        """

        :param productObject:
        :param quantity:
        :return:
        """
        return {"productobject":productObject, "quantity":quantity}

    def addInventory(self, productObject, quantity=1):
        """

        :param productObject:
        :return:
        """
        if isinstance(productObject, product):
            item_id = self.getProductItemId(productObject)
            item_object = self.setItemObject(productObject,quantity)
            self.inventory[item_id] = item_object

    def printInventoryDetails(self):
        """

        :return:
        """
        total_cost = 0
        for item_id, details in self.inventory.items():
            print(f"item_id: {item_id}")
            print(f"item_name: {details['productobject'].name}")
            print(f"item_price: {details['productobject'].price}")
            print(f"total_quantity: {details['quantity']}")
            item_cost = details["quantity"] * details["productobject"].price
            total_cost += item_cost
            print()
        print(f"Total Inventory Cost: {total_cost}")

if __name__ == "__main__"   :
    """
    """
    banana = product(1000, "Yellow Banana", 1.99, "pound")
    ##print(banana.getProductDetail("name", "id","unit"))
    ##banana.price=3.99
    print(banana.getProductDetail())
    mango = product(1001, "Indian Mango", 4.99, "pound")
    print(mango.getProductDetail())

    foodmarket = inventory()
    foodmarket.addInventory(banana,20)
    foodmarket.addInventory(mango,10)
    print(foodmarket.inventory)

    print("Inventory Details:")
    foodmarket.printInventoryDetails()