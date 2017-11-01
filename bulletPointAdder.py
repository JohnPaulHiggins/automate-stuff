#! python3
# bulletPointAdder.py - Adds bullet points to the start of each line from the clipboard.

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = "* " + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)