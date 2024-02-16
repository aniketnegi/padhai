def list_sq(l):
    for i in l:
        yield (i**2)


l = [1, 2, 3, 4, 5]
new = list_sq(l)
print(next(new))
print(next(new))
print(next(new))
print(next(new))
print(next(new))
