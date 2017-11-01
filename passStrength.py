#! python3
# passStrength.py - checks that password is "strong" (>= 8 chars, upper and lower cases, includes a number)

import re
def passStrength(password):
    upcaseRegex = re.compile(r'[A-Z]')
    lowcaseRegex = re.compile(r'[a-z]')
    numRegex = re.compile(r'\d')
    if len(password) < 8:
        return False
    elif upcaseRegex.search(password) == None:
        return False
    elif numRegex.search(password) == None:
        return False
    else:
        return True