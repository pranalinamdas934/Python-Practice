"""List is a collection which is ordered and changeable. Allows duplicate members."""

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(this_list)
print(this_list[1])
print(this_list[-1])
print(this_list[2:5])
print(this_list[2:5])
print(this_list[:4])
print(this_list[2:])


"""We can loop through the items using for loop"""

for x in this_list:
    print(x)

"""append() to add item at last in the list"""
this_list.append("orange")
"""insert sets at the front of the list"""
this_list.insert(0, "grapes")
print(this_list)

"""insert() to add item at the specified position"""
this_list.insert(1, "orange")
this_list.insert(-1, "muskmelon")

print(this_list)

"""remove() is to remove item from the list"""
this_list.remove("banana")
print(this_list)


"""The pop() method removes the specified index, or the last item if index is not specified"""
this_list.pop()
print(this_list)

"""The del keyword removes the specified index"""
del this_list[0]
print(this_list)

"""The del keyword can also delete the list completely"""
del this_list
