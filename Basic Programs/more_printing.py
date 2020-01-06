#!/bin/python
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# if we use comma at the end of 'end6', then it will not go to new line.
print(end1 + end2 + end3 + end4 + end5 + end6, end='$', sep='-')
print(end7 + end8 + end9 + end10 + end11 + end12)
print("\n \n")

# Look for python inbuilt new line character.
""" \n  is used for new line in python"""
