#Brandon Norwood
#11/18/2021
#Assign7-7

import sys

def findnumericgrade(lg):    #lg is the "letter grade"
    if lg == "A":
        return '4.0'
    elif lg == "B":
        return '3.0'
    else:
        return '2.0'
        
sectionNum = int(sys.argv[1])

fHandle = open(r'C:\Users\Norwood\Downloads\studentdata.csv')

count = 0
total = 0

for line in fHandle:
    
    index = line.find(',')
    line = line[index+1:]
    
    index = line.find(',')
    line = line[index+1:]
    
    index = line.find(',')
    line = line[index+1:]
    
    index = line.find(',')
    grade = line[:index]
    
    numericG = findnumericgrade(grade)
    numericG = float(numericG)
    
    count += 1
    total += numericG
    
average = total/count
print("The", sectionNum, "average is:", round(average,2))
    
