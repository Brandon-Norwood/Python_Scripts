#Brandon Norwood
#09/14/2021
#Assign3-9

import sys

length = float(sys.argv[1])
width = float(sys.argv[2])

if length != width:
    print("Rectangle")
elif length == width:
    print("Square")
    