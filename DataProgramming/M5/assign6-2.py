#Brandon Norwood
#11/04/2021
#Assign6-2

import sys

word = sys.argv[1]
letter = sys.argv[2]

counter = 0                         #always need a counter when counting or needing to find an average

for itr in word:                    #itr = iteration from the counter 0. So every letter from 0 to the end of the word/string
    if itr == letter:               #if the iteragtion is an "a"
        counter = counter + 1       #counts the letter

print("There are", counter, "'"+letter+"'s", "in", "'"+word+"'")