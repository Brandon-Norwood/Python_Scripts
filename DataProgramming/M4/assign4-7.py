#Brandon Norwood
#09/30/2021
#Assign4-7

import sys
import math

def isOdd(number):
    if number%2 == 0:
        print(number, "is not an odd number")
    else:
        print(number, "is an odd number")
        

number = int(sys.argv[1])

isOdd(number)