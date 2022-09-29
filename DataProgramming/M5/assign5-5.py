#Brandon Norwood
#10/19/2021
#Assign5-5

#Write a program to generate a random number between 2 and 100. 
#The program should use a while loop to determine if the number is prime or not. 
#You can not use a predefined set of prime numbers.

import random 

num = random.randint(2,100) #generate a random number between 2 and 100

itr = 2 #important to have an iteration variable for a WHILE loop

isPrime = True

while itr < num:
    if num%itr == 0: #0 means no remainder
        isPrime = False
        break
    itr += 1 #increase itr by 1...

if isPrime:
    
    print(num, "is a prime number")
   

else:
    print(num, "is NOT a prime number")