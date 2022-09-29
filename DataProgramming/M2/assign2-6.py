#Brandon Norwood
#08/26/2021
#Assign2-6

import sys

gallon = int(sys.argv[1])

liter = (gallon*3.785)

print(gallon,"gallon(US) is equal to", round(liter, 3), "liter")