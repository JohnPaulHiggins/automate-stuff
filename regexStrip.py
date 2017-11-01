#! python3
# regexStrip.py - performs same task as strip string method, using regexStrip

import re
def regexStrip(s, side=None): # s is string to be processed; side is left/right side of string
    whitespaceRegex = re.compile(r'(\s*)(\S+.*\S+)(\s*)')
    mo = whitespaceRegex.match(s)
    if mo == None:
        return ''
    if side not in ["left", "right"]:
        return mo.group(2)
    elif side == "left":
        return mo.group(2) + mo.group(3)
    else:
        return mo.group(1) + mo.group(2)