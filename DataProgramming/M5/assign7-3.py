#Brandon Norwood
#11/15/2021
#Assign7-3

fHandle = open(r'C:\Users\Norwood\Downloads\studentdata.csv')

def loaddata(fHandle):
    
    outHandle = open(r'C:\Users\Norwood\Downloads\error.txt', 'w')    #Output file that we are going to write to, 'w'
    
    for itr in fHandle:              #Loops through file to read the contents, itr will be a line of the file
        if ',W,' in itr:             #If ",W," is in the line (itr) 
            outHandle.write(itr)     #Writes the line (itr) to the "error.txt" file 
            
    outHandle.close()                #Always close file after the loop
    
loaddata(fHandle)

