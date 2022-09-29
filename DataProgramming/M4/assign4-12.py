#Brandon Norwood
#10/05/2021
#Assign4-12

import sys

def calstats(s1, s2, s3, s4, s5):
    small = min(s1, s2, s3, s4, s5)
    print("Min:", small)
    big = max(s1, s2, s3, s4, s5)
    print("Max:", big)
    difference = big - small
    print("Range:", difference)
    average = (s1+s2+s3+s4+s5)/5
    print("Average:", average)
    
try:
    sale1 = (sys.argv[1])
    sale2 = (sys.argv[2])
    sale3 = (sys.argv[3])
    sale4 = (sys.argv[4])
    sale5 = (sys.argv[5])
except:
    print("The wrong number of sales provided.")
    quit()
else:
    try:
        sale1 = int(sale1)
        sale2 = int(sale2)
        sale3 = int(sale3)
        sale4 = int(sale4)
        sale5 = int(sale5)
    except:
        print("All inputs should be numeric.")
        quit()
    
        
calstats(sale1, sale2, sale3, sale4, sale5)
#print("Min:", small)
#print("Max:", big)
#print("Range:", difference)
#print("Average:", average)