#Brandon Norwood
#11/13/2021
#Assign6-5

import sys

patientNum = len(sys.argv)

index = 1
high = 0
desirable = 0
borderline = 0

while index < patientNum:
    info = sys.argv[index]
    
    if 'high' in info:
        high = high + 1
    
    elif 'desirable' in info:
        desirable = desirable + 1
        
    elif 'borderline' in info:
        borderline = borderline + 1
        
    index = index + 1
  
print("Desirable Count:"+str(desirable))
print("Borderline Count:"+str(borderline))
print("High Count:"+str(high))
"""
lenInp = len(sys.argv)
dCount = 0
bCount = 0
hCount = 0

for itr in range(1,patientNum)
    
    patient = sys.argv[itr]
    
    index = patient.find(',')
    patient = patient[index+1:]
    
    index = patient.find(',')
    patient = patient[index+1:]
    
    index = patient.find(',')
    category = patient[:index]
    
    if category == 'high':
        hCount += 1
    elif category == 'borderline':
        bCount += 1
    else:
        dCount += 1

print("Desirable Count:", dCount)
print("Borderline Count:", bCount)
print("High Count:", hCount)
"""   
    

        
    

