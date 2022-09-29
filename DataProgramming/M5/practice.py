
#Take 10 integers from keyboard using loop and print their average 
#value on the screen.

import sys

num = len(sys.argv)

for n in range(num):
    numbers = float(num)
    total += numbers
avg = total/num
print(avg)

