#Brandon Norwood
#11/18/2021
#Assign7-8

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
            
            
    