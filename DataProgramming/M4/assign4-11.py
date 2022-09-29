#Brandon Norwood
#10/05/2021
#Assign4-11

import sys

def calcinterest(p, r, n, t):
    
    totalAmount = principal*(1+rate/numPay)**(numPay*totalYear)
    interestPaid = totalAmount - principal
    result = round(interestPaid,1)
    return result

principal = int(sys.argv[1]) 
rate = float(sys.argv[2])/100
numPay = int(sys.argv[3])
totalYear = int(sys.argv[4])

result = calcinterest(principal, rate, numPay, totalYear)

calcinterest(principal, rate, numPay, totalYear)
print("Interest Paid: $"+ str(result))