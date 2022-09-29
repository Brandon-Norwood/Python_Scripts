#Brandon Norwood
#08/18/2021
#Assign2-2

import sys

hours = int(sys.argv[1])
rate = float(sys.argv[2])
grossPay = (hours*rate)

print("The gross pay for", hours, "hours with $"+ str(rate), "per hour is $"+ str(round(grossPay,2))+".")