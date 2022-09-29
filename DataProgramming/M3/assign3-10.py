#Brandon Norwood
#09/14/2021
#Assign3-10

import sys

try:
    purchaseNumber = float(sys.argv[1])
except:
    print("Please enter a numeric input.")
else:
    if purchaseNumber <= 8:
        print("No discount. Your total cost is $"+str(purchaseNumber*100))
    elif purchaseNumber > 8:
       print("You get a discount of $"+str(round(purchaseNumber*100*(1/10)))+",", "and your total cost is $"+str((purchaseNumber*100) - (purchaseNumber*100*(1/10))))