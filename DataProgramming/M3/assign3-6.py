#Brandon Norwood
#09/09/2021
#Assign3-6

import sys

night1 = float(sys.argv[1])
night2 = float(sys.argv[2])
night3 = float(sys.argv[3])
night4 = float(sys.argv[4])
night5 = float(sys.argv[5])
age = int(sys.argv[6])

average = (night1+night2+night3+night4+night5)/5

if age<18:
    print("You must be an adult to participate.")
else:
    if age>=18 and age<=25: 
        print("Average:", average)
    elif age>=26 and age<=64:
        print("Average:", average)
    elif age>=64:
        print("Average:", average)
        
if age>=18 and age<=25 and average>=7 and average<=9:
    print("Sleep type: normal")
elif age>=18 and age<=25 and average<7:
    print("Sleep type: too little")
elif age>=18 and age<=25 and average>9:
    print("Sleep type: too much")
else:
    if age>=26 and age<=64 and average>=7 and average<=9:
        print("Sleep type: normal")
    elif age>=26 and age<=64 and average<7:
        print("Sleep type: too little")
    elif age>=26 and age<=64 and average>9:
        print("Sleep type: too much")
    elif age>=65 and average>=7 and average<=8:
        print("Sleep type: normal")
    elif age>=65 and average<7:
        print("Sleep type: too little")
    elif age>=65 and average>8:
        print("Sleep type: too much")
