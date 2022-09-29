#Brandon Norwood
#09/09/2021
#Assign3-7

import sys

try:
    firstQt = int(sys.argv[1])
    secondQt = int(sys.argv[2])
    thirdQt = int(sys.argv[3])
    fourthQt = int(sys.argv[4])
except:
    print("All sales should be numeric.")
    quit()

totalSales = (firstQt+secondQt+thirdQt+fourthQt)

if totalSales<50000:
    print("Quarterly sales:", "$"+str(firstQt)+",", "$"+str(secondQt)+",", "$"+str(thirdQt)+",", "$"+str(fourthQt))
    print("Total sales:", "$"+str(totalSales))
    print("Sales: low")

else:
    if totalSales>=50000 and totalSales<150000:
        print("Quarterly sales:", "$"+str(firstQt)+",", "$"+str(secondQt)+",", "$"+str(thirdQt)+",", "$"+str(fourthQt))
        print("Total sales:", "$"+str(totalSales))
        print("Sales: med")
    elif totalSales>=150000:
        print("Quarterly sales:", "$"+str(firstQt)+",", "$"+str(secondQt)+",", "$"+str(thirdQt)+",", "$"+str(fourthQt))
        print("Total sales:", "$"+str(totalSales))
        print("Sales: high")       

if totalSales<20000:
    print("Warning: Need to improve sales")