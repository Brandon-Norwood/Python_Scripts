#Brandon Norwood
#10/19/2021
#Assign5-8

#Write a program that takes two integers from the inputs. 
#The code should find the value of one number raised 
#to the power of the other one using a while loop. 
#You are not allowed to use the build-in power function and ** operator. 

import sys

num1 = int(sys.argv[1]) #3
num2 = int(sys.argv[2]) #5

power = 1                   #variable to store 3*3*3*3*3

itr = 1                     #while loop always has an iteration value

while itr<=num2:
    power = power * num1
    itr +=1                 #update itr, so when itr is no longer <= num2, it stops to prevent an infinite loop

print(num1,"power",str(num2)+":",power)