class Parent:
    a = 0

    def __iter__(self):
        self.a = 0
        return self

    upper = 10

    def __next__(self):
        if self.a < self.upper:
            print(self.a)
        else:
            raise StopIteration

        self.a += 1


a = Parent()

(next(a))
(next(a))
(next(a))
(next(a))
(next(a))
(next(a))
(next(a))
(next(a))
(next(a))
(next(a))
(next(a))
