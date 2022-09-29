#Brandon Norwood
#10/21/2021
#Assign5-9

#Write three functions called loopeven(), loopsum(), and loopthree() respectively that produce the output below.
#loopeven(): takes the first system argument as a parameter (6 in the example below) and prints the even numbers in the range
#loopsum(): takes the second system argument as a parameter (7 in the example below) and prints the sum of the numbers in the range
#loopthree(): takes the third system argument as a parameter (9 in the example below) and prints treble of numbers in the range, 
#but only if the input is divisible by 3. If it is not divisible by 3, print the message shown below.

import sys

def loopeven(num1):
    print("Function loopeven():")     #print statement before the FOR loop to print correctly
    for itr in range(1,num1+1):
        if itr%2 == 0:                                 
            print(itr)

def loopsum(num2):
    summation = 0
    print("Function loopsum():")
    for num in range(1,num2+1):  
        summation = summation+num 
    print(summation)

def loopthree(num3):
    print("Function loopthree():")
    if num3%3 == 0:
        for itr in range(1,num3+1,3): #to make it print in three columns 
            print(itr, itr+1, itr+2)  #to make it print in three columns
    else:
        print("This one wont work.")

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

    
loopeven(num1)

loopsum(num2)

loopthree(num3)