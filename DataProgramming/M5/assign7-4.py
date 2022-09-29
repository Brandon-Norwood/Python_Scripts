#Brandon Norwood
#11/15/2021
#Assign7-4

fHandle = open(r'C:\Users\Norwood\Downloads\studentdata.csv')

def findnumericgrade(lg):    #lg is the "letter grade"
    if lg == "A":
        return '4.0'
    elif lg == "B":
        return '3.0'
    else:
        return '2.0'

def loaddata(fHandle):
    
    errorHandle = open(r'C:\Users\Norwood\Downloads\error.txt', 'w')
    outHandle = open(r'C:\Users\Norwood\Downloads\output.txt', 'w')
    
    count = 0
    
    for itr in fHandle:      #itr is the iteration of each line
        
        if itr.startswith('Section_Number'):
            continue
        
        elif ',W,' in itr:
            errorHandle.write(itr)
            
        else:
            index = itr.find(',')    #finds "," then rinse and repeat for everything.
            sec_num = itr[:index]
            itr = itr[index+1:]
            
            index = itr.find(',')
            prof = itr[:index]
            itr = itr[index+1:]
            
            index = itr.find(',')
            stud_id = itr[:index]
            itr = itr[index+1:]
            
            index = itr.find(',')
            courseG = itr[:index]
            itr = itr[index+1:]
            
            index = itr.find(',')
            name = itr[:index]
            courseID = itr[index+1:]
            length = len(courseID)           #Get the lens of the course ID
            courseID = courseID[:length-1]   #Make the lens of the course ID minus 1 in order to ignor the invisible \n
            
            numericG = findnumericgrade(courseG)    #calls numeric grade function above to convert into numeric value
            
            outputL = name+": "+courseID+" "+sec_num+" "+prof+" "+courseG+" "+numericG+"\n"  #add the "\n" so the output is correct
            
            outHandle.write(outputL)
            count += 1
            
    errorHandle.close()    #dont forget to close them files after the loop boi
    outHandle.close()      #dont forget to close them files after the loop boi 
    
    return count
    
c = loaddata(fHandle)

print("The output.txt file contains", c, "lines")
            
  