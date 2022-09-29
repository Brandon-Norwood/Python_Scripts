#Brandon Norwood
#11/04/2021
#Assign6-1

import sys

word = sys.argv[1]

index = len(word) - 1

while index >= 0:
    letter = word[index]
    print(letter)
    index = index - 1
    