#Brandon Norwood
#10/21/2021
#Assign5-10

import sys

def calcavg(numInput):                          #"nInput" is the lenInput...the unknown number of inputs
    total = 0                                   # total number of inputs start at zero and stores summation
    count = 0                                   #counts all of the random inputs
    
    """itr = 1
    while itr < numInput:                       #while iteration is less than the number of inputs, it will keep reading them
        num = float(sys.argv[itr])              #store the itr variable in brackets because it will be updated after each iteration
        total = total + num
        count = count + 1
        itr = itr + 1"""                           #update iteration to avoid infinite loop
    
    for itr in range(1,numInput):
        num = float(sys.argv[itr])
        total = total + num
        count = count + 1
    
    average = total/count
    return round(average,2)


lenInput = len(sys.argv)   #return number of inputs

avg = calcavg(lenInput)
print("The average is", avg)