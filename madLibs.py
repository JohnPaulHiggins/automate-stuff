#! python3
# madLibs.py - Reads in a text file, prompts user for words, then prints and writes the result to a text file.
# Usage: madLibs.py <textfile>

import sys, re

# Read in file
madInput = sys.argv[1]
inputFile = open(madInput, 'r')
preText = inputFile.read()

# Locate special words
madRegex = re.compile(r'NOUN|VERB|ADJECTIVE|ADVERB')
blanks = re.findall(madRegex, preText)

# Prompt user
userIn = []
for blank in blanks:
    if blank.lower()[0] == 'a':
        prep = 'an'
    else:
        prep = 'a'
    print("Enter " + prep + " " + blank.lower() + ":")
    userIn.append(input().strip().lower())

# Replace
userIn = iter(userIn)

def replace_with(m):
    return next(userIn)

postText = re.sub(madRegex, replace_with, preText)

# Write to file
madOutput = madInput[:-4] + 'Filled.txt'

outputFile = open(madOutput, 'w')
outputFile.write(postText)

# Print to screen
print(postText)

inputFile.close()
outputFile.close()