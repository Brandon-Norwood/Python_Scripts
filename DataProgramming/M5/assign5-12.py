#Brandon Norwood
#10/21/2021
#Assign5-12

import sys

def calstats(numInput):
    
    itr = 1
    summation = 0
    small = None
    big = None
    
    while itr < numInput:
        num = int(sys.argv[itr])
        summation += num
        if small == None or small > num:
            small == num
        if big == None or big < num:
            big = num
        itr = itr+1
        
    difference = big - small
    average = summation/(numInput-1)
        
        
    
    
 
    print("Min:", small)   
    print("Max:", big)
    print("Range:", difference)    
    print("Average:", round(average,2))
    

numInput = len(sys.argv)

try:
    for i in range(1,numInput):
        num = int(sys.argv[itr])
except:
    print("All inputs should be numeric.")
else:
    calstats(numInput)