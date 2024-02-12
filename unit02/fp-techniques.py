from pprint import pprint

# Functional Programming Techniques
# Lambda functions
# filter, map

# ---------------------------------------------------------------------------------------------------------
# LAMBDA FUNCTIONS
# they are anonymus functions
# typically used for one line functions and when a function needs to be passed into a higher order function
# syntax:
# lambda <var1>, <var2>: <var1>%<var2>
# ^ this function returns the modulus of the 2 variables
some_func = lambda x, y, z: (x + y) ** z
print(some_func(1, 2, 3))
# just like those funcs in js
# something = (x) => {return x}
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# map
# takes in an iterable and visits each member of the iterable and apply the given function to it.
my_fav_nums = [1, 2, 3, 4, 5, 6, 7]


def square(num: int) -> int:
    return num * num


mfn_squared = list(map(square, my_fav_nums))  # map returns an iterator
pprint(f"my fav nums squared: {mfn_squared}")

# now instead of defining a function square() separately, we can use lambda functions to this inline
mfn_cubed = list(map(lambda num: num**3, my_fav_nums))
pprint(f"my fav nums cubed: {mfn_cubed}")
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# filter
# same as map, but the output contains only the values that satisfy the condition given in the input function
some_nums = [10, 213, 12, 1, 2, 3, 99, 100]


def is_odd(num):
    return num % 2


only_odd = list(filter(is_odd, some_nums))
print(only_odd)

# Lambda implementation
only_even = list(filter(lambda x: not x % 2, some_nums))
print(only_even)
