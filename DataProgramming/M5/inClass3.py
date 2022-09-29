import sys

word = sys.argv[1]

letter = 'a'

counter = 0   #always need a counter when counting or needing to find an average

for itr in word:    #itr = iteration from the counter 0. So every letter from 0 to the end of the word/string
    if itr == letter:  #if the iteragtion is an "a"
        counter = counter + 1  #counts the letter
print("For:", counter)

counter = 0

itr = 0

while itr < len(word):
    if word[itr] == letter:
        counter += 1
    itr += 1
print("While:", counter)