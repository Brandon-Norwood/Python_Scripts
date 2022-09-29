#Brandon Norwood
#11/18/2021
#Assign6-3

import sys

word = sys.argv[1]

vCount = 0
cCount = 0


for itr in range(0,len(word)):
    if word[itr] in ('a','e','i','o','u'):
        vCount = vCount + 1
    elif word[itr] >= 'a' and word[itr] <= 'z':
        cCount = cCount + 1
print("vowel:"+str(vCount), ",", "consonants:"+str(cCount))