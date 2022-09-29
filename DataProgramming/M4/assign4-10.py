#Brandon Norwood
#10/05/2021
#Assign4-10

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