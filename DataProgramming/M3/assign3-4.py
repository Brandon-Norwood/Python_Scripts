#Brandon Norwood
#09/06/2021
#Assign3-4

import sys
try:
    grade = float(sys.argv[1])
except:
    print("Error, please enter a numeric value")
else:
    if grade>=0 and grade<=1:
        if grade>=0.9:
            print("The letter grade is A")
        elif grade>=0.8:
            print("The letter grade is B")
        elif grade>=0.7:
            print("The letter grade is C")
        elif grade>=0.6:
            print("The letter grade is D")
        elif grade<0.6:
            print("The letter grade is F")
    
    else:
        print("Error, please enter a numeric value between 0 and 1")