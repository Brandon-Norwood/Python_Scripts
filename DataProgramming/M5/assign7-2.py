#Brandon Norwood
#11/15/2021
#Assign7-2

fHandle = open(r'C:\Users\Norwood\Downloads\mbox.txt')

count = 0
total = 0
for itr in fHandle:
    if itr.startswith('X-DSPAM-Confidence:'):
        count += 1
        index = itr.find(':')
        num = float(itr[index+1:])
        total += num
        
average = total/count

print("Average spam confidence:", round(average,12))