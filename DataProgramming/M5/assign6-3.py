#Brandon Norwood
#11/04/2021
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


"""
length = len(word)    #would have been helpful to assign the length before hand instead of struggling with the for statement

vCount = 0

for letter in word:
    
    char = letter
    if char in ('aeiou'):
        vCount = vCount + 1
        if vCount == 2:
            break
        else:
            continue                    
    print("vowel:"+str(vCount), ",", "consonants:"+str(cCount))
"""