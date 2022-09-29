#Brandon Norwood
#10/14/2021
#Assign5-2

#Write a program the same as assign5-1. In the end, instead of average, print out the max and min 
#value of the numeric inputs. You are not allowed to use predefined python max and min functions.

import sys              #for when inputs are comming from CMD

total = 0
count = 0
itr = 0
maxValue = None         #small input barrier
minValue = None         #large input barrier

while True:
    inp = sys.argv[itr]
    
    if inp == "done":
        break
        
    itr += 1            #same as itr = itr + 1, see below for additional example
    
    try:
        inp = int(inp)
    except:
        continue
    else:
        total += inp
        count += 1
        if maxValue == None or maxValue < inp:
            maxValue = inp
        if minValue == None or minValue > inp:
            minValue = inp
            
print("total:"+str(total)+", count:"+str(count)+", max:"+str(maxValue)+", min:"+str(minValue))
        


