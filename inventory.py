"""
Product Inventory Project - Create a simple program to manage an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""

class product():
    """
    blue print for product information
    """
    def __init__(self, id,name, price, unit):
        """
        init default variables for product/item i.e. name, id, price
        """
        self.id = id
        self.name = name
        self.price = price
        self.unit = unit
        self.item_json = {"id":self.id, "name":self.name, "price":self.price, "unit": self.unit}

    def getProductDetail(self, **kwargs):
        """
        get detail of one or more attributes of product
        :return:
        """
        if len(kwargs) == 0:
            print(self.item_json)
            


if __name__ == "__main__":
    """
    """
    banana = product(1000, "banana", 1.99, "pound")
    banana.getProductDetail()
