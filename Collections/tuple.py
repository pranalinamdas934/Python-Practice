"""A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets."""

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(this_tuple)
print(this_tuple[1])
print(this_tuple[2:4])
print(this_tuple[-4:-1])

"""If you want tot change tuple values, you can convert tuple into list."""

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

"""you can loop through the items using for loop"""

x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

for x in this_tuple:
    print(x)

"""unpacking of tuple"""
(first, second, third, *rest) = this_tuple

print(first, second, third, rest)

# why tuple doesn't have append?
"""Python tuple is an immutable object. Hence any operation that tries to modify it (like append) is not allowed. """

# tuple deconstruction example
point = 10, 20, 30
x, y, z = point
print(x, y, z)

b = ("Bob", 19, "CS")
(name, age, studies) = b    # tuple unpacking
name
