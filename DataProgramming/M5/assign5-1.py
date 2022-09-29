#Brandon Norwood
#10/14/2021
#Assign5-1

#Write a program that repeatedly reads inputs using a while loop until it reads "done". 
#The inputs could be numbers and words. The program should detect non-numeric inputs 
#using try/except and skip the words unless it is "done". Once it reads "done", print out 
#the summation of numbers, number of numbers, and the average of the numbers, and the program 
#terminates. Some sample outputs are shown below. Use the round function to have at most 2 
#decimal places in the answer.

#itr is iteration <----
import sys

itr = 1                     #define variable before loop
total = 0
count = 0

while True:                 #infinite loop for unlimited number of inputs    
    inp = sys.argv[itr]
    #print(inp)
    if inp == "done":
        break               #stops loop once done is typed
    itr = itr + 1           #update itr so you dont get an infinite output
    try:
        inp = int(inp)
    except:             
        continue 
    else:
        
        count = count + 1
        total = total + inp 

if count == 0:
    print("total:0, count:0, average:0")
else:
    average = round(total/count,2)
    print("total:"+str(total),", count:"+str(count), ", average:"+str(average)) 
        
    