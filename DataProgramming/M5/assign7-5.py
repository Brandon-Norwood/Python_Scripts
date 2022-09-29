#Brandon Norwood
#11/18/2021
#Assign7-5

fHandle = open(r'C:\Users\Norwood\Downloads\mbox-short.txt')
testHandle = open(r'C:\Users\Norwood\Downloads\test.txt','w')

for line in fHandle:             #line is the iteration...as in each line
    testHandle.write(line[:-1])  #I smooshed it, professor did it differently below
    
testHandle.close()

"""
for itr in fHandle:
    itr = itr[:-1]
    testHandle.write(itr)
    
testHandle.close()
"""