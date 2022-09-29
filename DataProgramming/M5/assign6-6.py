#Brandon Norwood
#11/13/2021
#Assign6-6



def calcbmi(height, weight):
   bmi = (weight*703) / (height**2)
   bmi = round(bmi,2)
   return(bmi)

def getcategory(bmi):
   if bmi < 18.5:
       return "Underweight"
   elif bmi >= 18.5 and bmi <= 24.9:
       return "normal"
   elif bmi >= 25 and bmi < 30:
       return "Overweight"
   else:
       return "Obese"


import sys

for itr in range(1,len(sys.argv)):
    
    person = sys.argv[itr]
    
    index = person.find(',')
    name = person[0:index]
    
    person = person[index+1:]
    
    index = person.find(',')
    age = person[0:index]
    person = person[index+1:]
    
    index = person.find(',')
    cat = person[:index]
    person = person[index+1:]
    
    index = person.find(',')
    height = int(person[0:index])
    weight = int(person[index+1:])
    
    BMI = calcbmi(height, weight)
    category = getcategory(BMI)
    
    print(name+':', BMI, ",", category)