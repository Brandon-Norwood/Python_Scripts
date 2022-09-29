#Brandon Norwood
#09/09/2021
#Assign3-8

import sys


time = int(sys.argv[1])
zeroOut = time*1          

if zeroOut>=500 and zeroOut<1200:
        print("Good morning")
elif zeroOut>=1200 and zeroOut<1600:
        print("Good afternoon")
elif zeroOut >=1600 and zeroOut<1900:
        print("Good evening")
elif zeroOut>=0 and zeroOut<500:
        print("Good night")
elif zeroOut>=1900 and zeroOut<=2400:
        print("Good night")