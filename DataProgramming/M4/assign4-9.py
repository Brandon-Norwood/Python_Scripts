#Brandon Norwood
#10/05/2021
#Assign4-9

import sys
import math

def calcavg(n1, n2, n3, n4, n5):
    summation = n1+n2+n3+n4+n5
    result = summation/5
    result = round(result,1)
    return result
try:    
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])
    num4 = int(sys.argv[4])
    num5 = int(sys.argv[5])
except:
    print("Error, all grades must be numeric.")
    quit()

result = calcavg(num1, num2, num3, num4, num5)
#print("Average:", result)

def getLetter(avgNum):
    if avgNum >= 90:
        letter = "A"
    elif avgNum >= 80 and avgNum <90:
        letter = "B"
    elif avgNum >= 70 and avgNum < 80:
        letter = "C"
    elif avgNum >= 60 and avgNum < 70:
        letter = "D"
    elif avgNum < 60:
        letter = "F"
    return letter
letter = getLetter(result)
#print("Letter grade:", letter)

def printresults(result, letter):
    
    print("Average:", result)
    print("Letter grade:", letter)

printresults(result, letter)