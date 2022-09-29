#Brandon Norwood
#09/09/2021
#Assign3-5

import sys

sysBp = int(sys.argv[1])     #systolic blood pressure
totalC = int(sys.argv[2])    #total cholesterol

if sysBp<120: 
        print("Systolic blood pressure:", str(sysBp)+",", "normal blood pressure")
elif sysBp>=120 and sysBp<=129:
        print("Systolic blood pressure:", str(sysBp)+",", "elevated blood pressure")
elif sysBp>=130 and sysBp<=139:
        print("Systolic blood pressure:", str(sysBp)+",", "stage 1 hypertension")
elif sysBp>=140:
        print("Systolic blood pressure:", str(sysBp)+",", "stage 2 hypertension")

if totalC<200:
    print("Total cholesterol:", str(totalC)+",", "desirable")
elif totalC>=200 and totalC<=239:
    print("Total cholesterol:", str(totalC)+",","borderline high")
elif totalC>=240:
    print("Total cholesterol:", str(totalC)+",","high")
