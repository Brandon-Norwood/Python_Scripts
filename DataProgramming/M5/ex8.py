"""write a program to take a word and letter and count the number of occurance of the letter in the word using
the following functions and operators:
substring (in)
replace
find
or any other function that you are allowed to use.
word = "hello"
dir(word) shows set of different functions you can use in cmd
input: same as assign6-2
output: same as assign6-2"""

import sys

word = sys.argv[1]
letter = sys.argv[2]

counter = 0                         #always need a counter when counting or needing to find an average

for itr in word:                    #itr = iteration from the counter 0. So every letter from 0 to the end of the word/string
    if itr == letter:               #if the iteragtion is an "a"
        counter = counter + 1       #counts the letter

print("There are", counter, "'"+letter+"'s", "in", "'"+word+"'")