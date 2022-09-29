#Brandon Norwood
#10/14/2021
#Assign5-3

#Write a program that reads the inputs repeatedly using a while loop. 
#The code should skip the even numbers and print only the odd numbers. Inputs are always valid.

import sys

itr = 1

numInput = len(sys.argv)   #for no known number of inputs 

while itr < numInput:
    num = int(sys.argv[itr])
    itr += 1
    if num%2==0:
        continue
    print(num)