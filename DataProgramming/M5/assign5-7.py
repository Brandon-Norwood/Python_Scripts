#Brandon Norwood
#10/19/2021
#Assign5-7

#Write a program that reads the input repeatedly using a for loop, 
#and then prints the sum of the even and odd integers separately.

import sys

lenInput = len(sys.argv)        #returns the number of inputs (for multiple inputs)
sumEven = 0                     #define these variables before the loop
sumOdd = 0                      #define these variable before the loop
for itr in range(1,lenInput):   #make a range to cover all numbers
    num = int(sys.argv[itr])    #updates each iteration, has to be an integer
    if num%2==0:                #it is even
        sumEven += num
        
    else:                       #it is odd
        sumOdd += num
    
print("sum of even:", sumEven, ",sum of odd:", sumOdd)
