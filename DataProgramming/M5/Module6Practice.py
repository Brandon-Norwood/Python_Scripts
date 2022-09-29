#MODULE 6 practice

import sys

lenInput = len(sys.argv)

print("I have", lenInput, "inputs")

for itr in range(1,lenInput):
    print(sys.argv[itr])