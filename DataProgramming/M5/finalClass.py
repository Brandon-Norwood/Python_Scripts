"""Final Inclass

find the average 
Neda Asl 100 70 60 50 50"""

import sys

fname = sys.argv[1]
lname = sys.argv[2]

#for random input u can do numInput = len(sys.argv)

total = 0

for itr in range(3,8):        #3,4,5,6,7
    num = int(sys.argv[itr])
    total = total+num
    
average = total/5
print(fname," 's gpa is", average)

#while loop

total = 0
itr = 3

while itr<=7:
    num = int(sys.argv[itr])
    total = total + num
    itr = itr + 1
    
average = total/5                   #for len input, change to total/(numInput-3) ^^^see comment above^^^
print(fname," 's gpa is", average)