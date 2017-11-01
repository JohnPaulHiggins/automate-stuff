#! python3
# printTable.py - Given list of lists of strings, formats them in table of right-justified columns

def printTable(tableData):
    widths = []

    for i in range(len(tableData)):
        widths.append(1 + max([len(w) for w in tableData[i]]))

    rows = len(tableData[0])
    cols = len(tableData)

    for i in range(rows):
        s = ""
        for j in range(cols):
            s += tableData[j][i].rjust(widths[j])
        print(s)