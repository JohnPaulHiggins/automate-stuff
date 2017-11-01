#! python3

# regexSearch.py - Opens all .txt files in a folder and searches for user-supplied regular expression. Prints results to screen.
# Usage: regexSearch.py <path to directory>

import sys, re, os

# Prompt user for, and compile, search regex (we want a match for the whole line)
print("Please enter a regular expression:")
sRegex = re.compile(r'.*%s.*' % input())

# Set path to directory (if none provided, use CWD)
if len(sys.argv) == 2:
    direct = os.path.abspath(sys.argv[1])
    os.chdir(direct)
else:
    direct = os.getcwd()

# Open txt files, search and print
print() # For a more aesthetic format.
for f in os.listdir(direct):
    if f[-3:] == 'txt':
        workingFile = open(f)
        text = workingFile.read()
        for match in re.findall(sRegex, text):
            print(match, end='\n\n')
        workingFile.close()
print("End of results.")
os.system("pause")