#Brandon Norwood
#10/14/2021
#Assign5-4

#Write a program that generates two random integer numbers between 1 and 100. 
#Then, print out the numbers between the two randomly generated ones using a while loop. 
#The output is shown below. 

import random

num1 = random.randint(1,100)
num2 = random.randint(1,100)

if num1 > num2:                 #if first number is larger than second number
    temp = num1
    num1 = num2
    num2 = temp
    
print("start:"+str(num1)+", end:"+str(num2))
while num1 <= num2:
    print(num1)
    num1 = num1 + 1