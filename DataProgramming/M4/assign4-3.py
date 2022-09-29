#Brandon Norwood
#09/28/2021
#Assign4-3

import random
import math

def powRand():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    
    calc = math.pow(n1, n2)
    
    print(n1, "power", n2, "is", int(calc))

powRand()
