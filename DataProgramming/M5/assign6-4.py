#Brandon Norwood
#11/04/2021
#Assign6-4

import sys

string = sys.argv[1]

colon = string.find(':')

remainder = string[colon + 1:]
print(remainder)
