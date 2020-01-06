"""A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets."""

this_set = {"apple", "banana", "cherry"}
print(this_set)

"""You cannot access items in a set by referring to an index, since sets are unordered the items has no index."""
"""We can access items using for loop"""

for x in this_set:
    print(x)

"""there are two methods of set add() and update()"""

this_set.add("orange")
print(this_set)

this_set.update(["orange", "mango", "grapes"])
print(this_set)

print(len(this_set))

this_set.remove("banana")
# this_set.remove("papaya")
print(this_set)

"""discard() does not raise error if we try to discard the item which is not present"""
this_set.discard("mango")
this_set.discard("papaya")
print(this_set)

"""Set is unordered so if you use pop() you will not know which item get removed"""
print(this_set.pop())

this_set.clear()

print(this_set)

# NOTE: foreach is not supported in python

# discuss set specific methods with relevant examples

"""(1).union(s) in python -> gives union set of two different sets"""

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
population = people.union(vampires)

"""can use "|" operator to union two sets"""
population1 = people | vampires

"""(2).intersect(s) -> Returns an intersection of two sets (common elements from two sets. 
    The ‘&’ operator comes can also be used in this case"""

victims = people.intersection(vampires)
victims1 = people & vampires

"""(3)difference(s) ->  set containing all the elements of invoking set but not of the second set
    We can use ‘-‘ operator here."""

safe = people.difference(vampires)
safe1 = people - vampires
