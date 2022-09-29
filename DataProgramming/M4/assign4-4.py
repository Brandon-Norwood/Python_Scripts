#Brandon Norwood
#09/28/2021
#Assign4-4

import sys
import math

def calc(n1, n2, n3):
    ex1= n1 
    ex2= n2 * n2
    ex3= n3 * n3 * n3
    
    summation = ex1 + ex2 + ex3
    result = summation ** (1/2) # math.sqrt(summation)
    
    result = round(result, 2)
    return result

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

result = calc(num1, num2, num3)
print(result)


