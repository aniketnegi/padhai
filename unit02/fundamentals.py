# A class is a blueprint of data that describes various info relating to Class
# use `class` keyword to define a class in python


class Item:
    # parameters
    name: str
    price: float
    qty: int

    # methods
    # self is used to access the properties of the object
    def calc_total_price(self):
        return self.price * self.qty

    def print_name(self, x):
        print(x)


# An object is an instance of a class
item1: Item = Item()  # item1 is an object that is an instance of class Item

# now properties relating to this class can be assigned to var `item1`
item1.name = "Phone"
item1.price = 100.00
item1.qty = 10

# calling a method of an object
total_price = item1.calc_total_price()  # should give 100.00 * 10 = 1000.00
print(total_price)
item1.print_name(item1.name)
