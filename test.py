#!/usr/bin/env python3

#Line 1 is the 'shebang' which tells bash to look for python 3 in /usr/bin/env python3

#this is a module in python providing access to variables from the python interpreter 
# We need to import in order to use it to print the current version of python running with sys.version

import sys

print("this is the current python version:\n")
print(sys.version)

