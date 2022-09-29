#Brandon Norwood
#08/17/2021
#Assign1-4

import sys

principal = int(sys.argv[1]) #will read first input from command prompt
rate = float(sys.argv[2])/100
numPay = int(sys.argv[3])
totalYear = int(sys.argv[4])

totalAmount = principal*(1+rate/numPay)**(numPay*totalYear)
interestPaid = round(totalAmount - principal, 1)

print("Interest Paid: $"+ str(interestPaid))


