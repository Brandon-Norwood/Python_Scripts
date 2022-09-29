#Brandon Norwood
#09/30/2021
#Assign4-6

import sys

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
        
    
