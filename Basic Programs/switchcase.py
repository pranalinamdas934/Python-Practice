def numbers_to_months(month_num):
    switcher = {
        1: "January",
        -2: "February",
        -3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    return switcher.get(month_num, "not a valid month number")


if __name__ == "__main__":
    print(numbers_to_months(41))

# why switch case is not there in python?
""" Most programming languages have switch/case because they don't have proper mapping constructs. 
    You cannot map a value to a function, that's why they have it. 
    But in Python, you can easily have a mapping table(dict) where a certain value maps to a certain function. 
    Python functions are first class values, you can use the functions as the values of 
    the dictionary get(key[, default]) method """


def east(): return "East"


def west(): return "West"


def north(): return "North"


def south(): return "South"


# map the inputs to the function blocks
switch_case = {
    1: east,
    2: west,
    3: north,
    4: south
}
print(switch_case[2]())
