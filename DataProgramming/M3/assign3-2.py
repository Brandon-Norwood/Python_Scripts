#Brandon Norwood
#09/06/2021
#Assign3-2

import sys

try:
    hours = int(sys.argv[1])
    rate = int(sys.argv[2])
except:
    print("Error, please enter numeric input.")
    quit()

if hours<=40:
    grossPay = hours*rate
    print("Your gross pay is $"+str(grossPay))
else: 
    extraHour = hours-40
    overPay = extraHour * rate * 1.75
    
    grossPay = 40 * rate + overPay
    print("Your gross pay is $"+str(grossPay))