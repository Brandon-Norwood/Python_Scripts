# input is neda,asl,age:30,gpa:3
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import sys

lenInput = len(sys.argv)

itr = 1
while itr < lenInput:
    
    string = sys.argv[itr]      
    index = string.find(",")               #finds the ",", stores in variable called "index"    
    name = string[:index]
    print("name:", name)
    
    string = string[index+1:]              #update the string each time to find next output
    index = string.find(',')
    lname = string[:index]
    print("lname:", lname)
    
    string = string[index+1:]
    indexColon = string.find(":")
    indexComma = string.find(",")
    age = string[indexColon+1:indexComma]  #add the +1 to remove the colon from the output
    print("age:", age)
    
    string = string[indexComma+1:]
    index = string.find(":")
    gpa = string[index+1:]
    print("gpa:", gpa)
    
    itr = itr +1                           #update that itr boi!