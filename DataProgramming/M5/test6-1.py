import sys

word = sys.argv[1]

index = 0

while index > len(word):
    index = index -1
    letter = word[index]
    print(letter)