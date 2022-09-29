#Brandon Norwood
#08/17/2021
#Assign1-3

import sys

name = sys.argv[1]
height = int(sys.argv[2])
weight = int(sys.argv[3])

BMI = (weight/(height*height))*703

print(name+"'s", 'BMI is', BMI)

