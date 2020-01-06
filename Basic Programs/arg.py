#!/bin/python
import sys

for arg in sys.argv[1:]:
    print("{}".format(arg.strip(',')))

# NOTE: remove the commas if its present in arguments
