#Brandon Norwood
#09/28/2021
#Assign4-2

import sys

def isDivisible(n1, n2):
    if n1%n2 == 0:
        print(n1, "is divisible by", n2)
    else:
        print(n1, "is not divisible by", n2)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

isDivisible(num1,num2)