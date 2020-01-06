import json

# some JSON:
x = '[{ "name":"John", "age":30, "city":{ "name" : "New York", "zip-code":1234556 } },' \
    '{"name":"priya", "age":23, "city":{ "name" : "London", "zip-code":876543 }}]'

"""convert from JSON to PYTHON"""
y = json.loads(x)
# NOTE: to access nested properties.
print(y[1]["city"]['zip-code'])

# python object
x = {
    "name": "john",
    "age": 30,
    "city": "New York"
}

"""Convert from Python to JSON"""
y = json.dumps(x)
print(y)

# difference between double quotes and single quotes in python
""" there is no difference between double quotes and single quotes.
    double quotes are useful inside single quotes and vice versa """