# _ -> protected
# __ -> private


class Parent:
    public = "public"
    _protected = "protected"
    __private = "private"

    def print_private(self):
        print(self.__private)


class Child(Parent):
    def print_output(self):
        super().print_private()
        print(self.public, self._protected)


obj = Child()
obj.print_output()
