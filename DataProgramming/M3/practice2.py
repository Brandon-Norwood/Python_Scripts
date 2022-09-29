
#If/else Statements, dont need to practice really

import sys

number1 = float(sys.argv[1])
number2 = float(sys.argv[2])
number3 = float(sys.argv[3])

if number1 >= number2 and number1 >= number3:
    print("Max:", number1)
elif number2 >= number1 and number2 >= number3:
    print("Max:", number2)
elif number3 >= number1 and number3 >= number2:
    print("Max:", number3)

if number1 <= number2 and number1 <= number3:
    print("Min:", number1)
elif number2 <= number1 and number2 <= number3:
    print("Min:", number2)
elif number3 <= number1 and number3 <= number2:
    print("Min:", number3)

#Basic try and except ################################

import sys

try:
    firstQt = int(sys.argv[1])
    secondQt = int(sys.argv[2])
    thirdQt = int(sys.argv[3])
    fourthQt = int(sys.argv[4])
except:
    print("All sales should be numeric.")
    quit()

totalSales = (firstQt+secondQt+thirdQt+fourthQt)

if totalSales<50000:
    print("Quarterly sales:", "$"+str(firstQt)+",", "$"+str(secondQt)+",", "$"+str(thirdQt)+",", "$"+str(fourthQt))
    print("Total sales:", "$"+str(totalSales))
    print("Sales: low")

else:
    if totalSales>=50000 and totalSales<150000:
        print("Quarterly sales:", "$"+str(firstQt)+",", "$"+str(secondQt)+",", "$"+str(thirdQt)+",", "$"+str(fourthQt))
        print("Total sales:", "$"+str(totalSales))
        print("Sales: med")
    elif totalSales>=150000:
        print("Quarterly sales:", "$"+str(firstQt)+",", "$"+str(secondQt)+",", "$"+str(thirdQt)+",", "$"+str(fourthQt))
        print("Total sales:", "$"+str(totalSales))
        print("Sales: high")       

if totalSales<20000:
    print("Warning: Need to improve sales")

#Basic try and except for string, integer, and decimal. Will show "Invalid Information" if not entered correctly ################################


import sys

try:
    string = sys.argv[1]
    number = int(sys.argv[2])
    decimal = float(sys.argv[3])
except:
    print("Invalid information")
    quit()
    
print (string, number, decimal)


# Loops and functions ################################

def shapes(shapeName, number):
    if shapeName == "circle":
        areaCircle(number)
    else:
        areaSquare(number)
        
def areaCircle(radius):
    area = 3.14159265359 * radius ** 2
    area = round(area,2)
    print("The circle area is", area)
    
def areaSquare(edge):
    area = edge * edge
    print("The square area is", round(area,2))
       
name = sys.argv[1]
num = int(sys.argv[2])

shapes(name, num)

# Loops and functions continued ################################

import random
import math

def powRand():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    
    calc = math.pow(n1, n2)
    
    print(n1, "power", n2, "is", int(calc))

powRand()

# Loops and functions continued ################################

import sys

def isDivisible(n1, n2):
    if n1%n2 == 0:
        print(n1, "is divisible by", n2)
    else:
        print(n1, "is not divisible by", n2)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

isDivisible(num1,num2)

# Loops and functions continued ################################

import sys
import math

def calc(n1, n2, n3):
    ex1= n1 
    ex2= n2 * n2
    ex3= n3 * n3 * n3
    
    summation = ex1 + ex2 + ex3
    result = summation ** (1/2) # math.sqrt(summation)
    
    result = round(result, 2)
    return result

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

result = calc(num1, num2, num3)
print(result)

# Loops and functions continued ################################

import sys
import math

def isOdd(number):
    if number%2 == 0:
        print(number, "is not an odd number")
    else:
        print(number, "is an odd number")
        

number = int(sys.argv[1])

isOdd(number)

# Loops and functions continued ################################

import sys
import math

def calcavg(n1, n2, n3, n4, n5):
    summation = n1+n2+n3+n4+n5
    result = summation/5
    result = round(result,1)
    return result
try:    
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])
    num4 = int(sys.argv[4])
    num5 = int(sys.argv[5])
except:
    print("Error, all grades must be numeric.")
    quit()

result = calcavg(num1, num2, num3, num4, num5)
#print("Average:", result)

def getLetter(avgNum):
    if avgNum >= 90:
        letter = "A"
    elif avgNum >= 80 and avgNum <90:
        letter = "B"
    elif avgNum >= 70 and avgNum < 80:
        letter = "C"
    elif avgNum >= 60 and avgNum < 70:
        letter = "D"
    elif avgNum < 60:
        letter = "F"
    return letter
letter = getLetter(result)
#print("Letter grade:", letter)

def printresults(result, letter):
    
    print("Average:", result)
    print("Letter grade:", letter)

printresults(result, letter)

# Loops and functions continued ################################

import sys

def calcbmi(height, weight):
    average = (weight/(height*height))*703
    result = round(average,2)
    
    return result
try:    
    height = float(sys.argv[1])
    weight = float(sys.argv[2])

except:
    print("This program only takes numeric input. Program terminated.")
    quit()

result = calcbmi(height, weight)

def getcategory(BMI):
    if BMI < 18.5:
        category = "underweight."
    elif BMI >= 18.5 and BMI <= 24.99:
        category = "normal."
    elif BMI >= 25 and BMI <= 29.99:
        category = "overweight"
    elif BMI >= 30 and BMI <= 34.99:
        category = "Obesity (Class 1)."
    elif BMI >= 35 and BMI <= 39.99:
        category = "Obesity (Class 2)."
    elif BMI >= 40:
        category = "Morbid Obesity."
    
    return category

category = getcategory(result)
BMI = calcbmi(height, weight)


#calcbmi(height,weight)

print("BMI:", str(BMI)+",", "and the category is", category)

# Loops and functions continued ################################

import sys

word = sys.argv[1]

vCount = 0
cCount = 0


for itr in range(0,len(word)):
    if word[itr] in ('a','e','i','o','u'):
        vCount = vCount + 1
    elif word[itr] >= 'a' and word[itr] <= 'z':
        cCount = cCount + 1
print("vowel:"+str(vCount), ",", "consonants:"+str(cCount))


""" How the professor did it in class, my way worked as well though.

length = len(word)    #would have been helpful to assign the length before hand instead of struggling with the for statement

vCount = 0

for letter in word:
    
    char = letter
    if char in ('aeiou'):
        vCount = vCount + 1
        if vCount == 2:
            break
        else:
            continue                    
    print("vowel:"+str(vCount), ",", "consonants:"+str(cCount))
"""

# Loops and functions continued ################################

import sys

def calcinterest(p, r, n, t):
    
    totalAmount = principal*(1+rate/numPay)**(numPay*totalYear)
    interestPaid = totalAmount - principal
    result = round(interestPaid,1)
    return result

principal = int(sys.argv[1]) 
rate = float(sys.argv[2])/100
numPay = int(sys.argv[3])
totalYear = int(sys.argv[4])

result = calcinterest(principal, rate, numPay, totalYear)

calcinterest(principal, rate, numPay, totalYear)
print("Interest Paid: $"+ str(result))

# Loops and functions continued ################################ 

import sys

customer = sys.argv[1]
amount = int(sys.argv[2])
price = float(sys.argv[3])
tax = float(sys.argv[4])/100

def calctotal(amount, price, tax):
    beforeTax = amount * price
    taxTotal = beforeTax * tax
    total = beforeTax + taxTotal
    print("Hello", customer+',', "your total today is", total)

calctotal(amount, price, tax)

# Slicing and indexing ################################ (ALSO FILE HANDLING FOR THIS ONE!)

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
    
    if name in line and not ',W,' in line: # professor did this differently than i did, output is the same though. If "W" in studentdata: print() quit() else: continue...I think?
        
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

# Slicing and indexing continued ################################

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

# Slicing and indexing continued################################(USE AN ARGUMENT!) Update itr index accordingly and you should be good.

import sys

information = sys.argv[1]

def findnumericgrade(numericG):
    if numericG == "A"
        return 4.0
    elif numericG == "B"
        return 3.0
    else:
        return 2.0

def calcavg(information):
    avg = numericG/4
    print(name1,", Average =", avg)

for itr in information:
    
    index = itr.find(",")    #could be a'.' or ',' or ';' or whatever. you tell it to find it, it's gonna find it
    name1 = itr[:index]      
    itr = itr[index+1:]
    
    index = itr.find(",")
    name2 = itr[:index]      #follows the iteration and index as set. 
    itr = itr[index+1:]
    
    index = itr.find(",")
    grade1 = itr[:index]     #follows the iteration and index as set. 
    itr = itr[index+1:]
    
    index = itr.find(",")
    grade2 = itr[:index]     #follows the iteration and index as set. 
    itr = itr[index+1:]      #updates itr with +1 to move through the index
    
    index = itr.find(",")
    grade3 = itr[:index]     #follows the iteration and index as set. 
    itr = itr[index+1:]
    
    index = itr.find(",")
    grade4 =itr[:index]
    
    numericG = findnumericgrade()
    
    
   
calcavg(information)
    
# file handling ################################ (THIS ONE WAS CONFUSING AS FUCK AT FIRST)

fHandle = open(r'C:\Users\Norwood\Downloads\test (1).txt')

longestWord = ""         
longestL = 0             #longest word "length"

for line in fHandle:     #wish i had figured this out lol. Read whole file as one string     allFile = fHandle.read()   makes whole file into one string
    
    index = line.find(' ')
    
    while index != -1:   # -1 means as long as there is something to check it will be checked ie != means does not equal
        
        word = line[:index]
        
        if len(word) > longestL:
            
            longestW = word
            longestL = len(word)
            
        line = line[index+1:]
        index = line.find(' ')
        
    word = line[:-1]
    
    if len(word) > longestL:
        
        longestW = word
        longestL = len(word)
        
print("The longest word is", longestW+", and it has", longestL, "characters.")

# file handling ################################ 

fHandle = open(r'C:\Users\Norwood\Downloads\mbox-short.txt')
testHandle = open(r'C:\Users\Norwood\Downloads\test.txt','w')

for line in fHandle:             #line is the iteration...as in each line
    testHandle.write(line[:-1])  #I smooshed it, professor did it differently below
    
testHandle.close()

"""
for itr in fHandle:
    itr = itr[:-1]
    testHandle.write(itr)
    
testHandle.close()
"""