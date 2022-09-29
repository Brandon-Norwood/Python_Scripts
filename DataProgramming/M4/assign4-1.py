#Brandon Norwood
#09/28/2021
#Assign4-1

import sys

def computepay(hour, rate):
    if hour<=40:
        grossPay = hour * rate
    
    else:
        extraHour = hour - 40
        overPaid = extraHour * rate * 1.75
        
        grossPay = 40 * rate + overPaid
        
    return grossPay

try:
    hour = int(sys.argv[1])
    rate = int(sys.argv[2])
except:
    print("Error, please enter numeric input.")

output = computepay(hour, rate)
print("You gross pay is $"+str(output))

