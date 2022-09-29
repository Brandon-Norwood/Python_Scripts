#Brandon Norwood
#09/30/2021
#Assign4-8


import random

def calc():
    n1 = random.randint(10,100)
    if n1%6 == 0:
        print(n1, "is divisible by 6")
    else:
        print(n1, "is not divisible by 6")
     
calc()
