"""A dictionary is a collection which is unordered, changeable and indexed"""

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)

"""We can access the items of a dictionary by referring to its key name"""
x = this_dict["model"]
print(x)

"""there is also a get() that will give the same result"""
y = this_dict.get("model")
print(y)

"""we can change the dictionaries values by referring to their key name"""
this_dict["year"] = 2019
print(this_dict)

"""we can use for loop to get keys from dictionaries"""
for x in this_dict:
    print(x)

for x in this_dict:
    print(this_dict[x])
    """this will return the values from dictionaries"""

""".values() also returns the values from dictionary"""
for x in this_dict.values():
    print(x)

"""to get both key value pair we can  use .items()"""
for x in this_dict.items():
    print(x)

"""to get the number of items in the dictionary"""
print(len(this_dict))

"""we can add new item in the dictionary"""
this_dict["color"] = "red"
print(this_dict)

"""remove item from dictionary with specified key using pop()"""
this_dict.pop("model")
print(this_dict)

"""we can use popitem() to remove last item from dictionary"""
this_dict.popitem()
print(this_dict)

"""The del keyword removes the item with the specified key name"""
x = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del x["model"]
print(x)

"""del can keyword can also delete the complete dictionary"""
del x
