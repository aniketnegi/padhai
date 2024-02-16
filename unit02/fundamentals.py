# A class is a blueprint of data that describes various info relating to Class
# use `class` keyword to define a class in python


class Item:
    # parameters
    name = ""
    price = 0.0
    qty = 0

    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.qty = q

    # methods
    # self is used to access the properties of the object
    def calc_total_price(self):
        return self.price * self.qty

    def print_name(self, x):
        print(x)


# An object is an instance of a class
item1 = Item(
    "phone", 100.00, 10
)  # item1 is an object that is an instance of class Item

# now properties relating to this class can be assigned to var `item1`
# item1.name = "Phone"
# item1.price = 100.00
# item1.qty = 10

# calling a method of an object
total_price = item1.calc_total_price()  # should give 100.00 * 10 = 1000.00
print(total_price)
item1.print_name("Sanvi")


class Parent:
    name = "Aniket"

    def print_name(self):
        print(self.name)


class Child(Parent):
    def output(self):
        self.print_name()


obj = Child()
obj.output()
