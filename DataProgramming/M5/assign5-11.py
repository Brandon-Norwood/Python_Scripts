#Brandon Norwood
#10/21/2021
#Assign5-11

import sys

def calcbmi(height, weight):
    average = (weight/(height*height))*703
    result = round(average,2)
    
    return result

numInput = len(sys.argv)
if numInput%2==0:
    print("The wrong number of arguments provided")
else:
    for itr in range(1,numInput,2):
        try:    
            height = float(sys.argv[itr])
            weight = float(sys.argv[itr+1])

        except:
            print("This program only takes numeric input. Program terminated.")
            quit()
        else:
            result = calcbmi(height, weight)
            BMI = calcbmi(height, weight)
            category = getcategory(result)
            

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

print("BMI:", str(BMI)+",", "and the category is", category)