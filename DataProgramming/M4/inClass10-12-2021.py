#WHILE LOOP
#in-class 10/12/2021
#Have users enter a number using the input function until they
#type the word done. Only print number that are not multiple of 3. Add
#a print statesment incase the number is multiples of 3 to notify the user
i=1
while i>0:
    word = input("please enter a number or word done:")
    
    if word == "done":
        print("the user entered done:")
        break 
    num = int(word)
    if num%3==0:
        print(num, "is multiples of 3")
        continue
    
    print(word)   
print("out of loop")
    