#Brandon Norwood
#11/13/2021
#Assign6-8

import sys

string = sys.argv[1]

sumEven = 0
countEven = 0

sumOdd = 0
countOdd = 0

index = string.find(',')

while index != -1:
    
    num = int(string[:index])
    
    if num%2 == 0:
        sumEven += num
        countEven += 1
    else:
        sumOdd += num
        countOdd += 1
        
    string = string[index+1:]
    index = string.find(',')

num = int(string)

if num%2 == 0:
    sumEven += num
    countEven += 1
else:
    sumOdd += num
    countOdd += 1

print("Odd numbers total:"+str(sumOdd)+',',"even numbers total:"+str(sumEven))