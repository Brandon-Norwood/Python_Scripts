#Brandon Norwood
#11/18/2021
#Assign7-6

import sys

def findnumericgrade(lg):    #lg is the "letter grade"
    if lg == "A":
        return '4.0'
    elif lg == "B":
        return '3.0'
    else:
        return '2.0'
        
fName = sys.argv[1]
lName = sys.argv[2]

name = fName+" "+lName

fHandle = open(r'C:\Users\Norwood\Downloads\studentdata.csv') #obviously file handle

itCount = 0
itTotal = 0

csCount = 0
csTotal = 0

for line in fHandle:
    
    if name in line and not ',W,' in line: # professor did this differently than i did, output is the same though.
        
        index = line.find(',')    #finds "," then rinse and repeat for everything.
        sec_num = line[:index]
        line = line[index+1:]
            
        index = line.find(',')
        prof = line[:index]
        line = line[index+1:]
            
        index = line.find(',')
        stud_id = line[:index]
        line = line[index+1:]
        
        index = line.find(',')
        grade = line[:index]
        
        numGrade = findnumericgrade(grade)
        numGrade = float(numGrade)          #was returning string??? Quick fix but weird.Further explained, it was because I had the function still returning string when converting letter grade to numeric. Could just remove the '' around the numeric values.
        
        if 'IT' in line:
            itCount += 1
            itTotal += numGrade
            
        elif 'CS' in line:
            csCount += 1
            csTotal += numGrade 
            
if itCount == 0:
    itAvg = 0
    
else:
    itAvg = itTotal/itCount
    
if csCount == 0:
    csAvg = 0
    
else:
    csAvg = csTotal/csCount
    
print(fName+"'s IT courses average:", round(itAvg,2), ", and CS courses average:", round(csAvg,2))
        
        
