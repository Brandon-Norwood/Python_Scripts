#Brandon Norwood
#10/19/2021
#Assign5-6

#Write a program the takes an input number and calculates the summation 
#of the numbers between 1 and the entered number using a for loop.

import sys

num = int(sys.argv[1])

summation = 0

for itr in range(1,num+1):  #+1 adds the entered number into the range as well
    summation += itr        #summation of all numbers from 1 to the entered number
    
print(summation)
