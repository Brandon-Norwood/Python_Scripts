#Brandon Norwood
#11/15/2021
#Assign7-1

fHandle = open(r'C:\Users\Norwood\Downloads\mbox-short.txt')

for itr in fHandle:
    print(itr.rstrip().upper())