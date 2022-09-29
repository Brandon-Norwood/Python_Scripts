import sys

hours = int(sys.argv[1])
rate = int(sys.argv[2])

total = hours*rate

if (hours<=40):
    print(total)
else: 
    total = (40*rate+((hours-40)*(rate*1.75)))
    print("Your gross pay is $"+str(total))
    