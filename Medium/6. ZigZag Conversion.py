class firstSolution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2 or len(s) < numRows:
            return s
        retVal = ''
        rowsDict = {}
        i = 0
        while i < len(s):
            # print(i)
            # retVal += s[i]
            rowsDict[i] = s[i]
            i += 2*(numRows-2) + 2
        # print(rowsDict)
        rowsDictActLen = len(rowsDict)
        rowsDict[i] = ''
        newestRow = rowsDict.copy()
        while rowsDictActLen < len(s):
            # print(rowsDict)
            for j in rowsDict:
                if (not (j - 1 in rowsDict)) and j-1 >= 0:
                    if j-1 < len(s):
                        newestRow[j-1] = s[j-1]
                        rowsDictActLen += 1
                    else:
                        newestRow[j-1] = ''
                if (not (j + 1 in rowsDict)) and j+1 < len(s):
                    newestRow[j+1] = s[j+1]
                    rowsDictActLen += 1
            for i, char in newestRow.items():
                retVal += char
                rowsDict[i] = char
            newestRow = {}

        # print("here: " + retVal)
        return retVal


def convert(self, s: str, numRows: int) -> str:
    strLen = len(s)
    if numRows < 2 or strLen < numRows:
        return s
    retVal = ''
    cycleLen = 2*numRows - 2
    i = 0
    for i in range(numRows):
        for j in range(i, strLen, cycleLen):
            retVal += s[j]
            if i != numRows - 1 and i != 0 and j + cycleLen-2*i < strLen:
                retVal += s[j+cycleLen-2*i]
    return retVal


print(convert(0, 'AB', 2))

# P Y
# A P

# P       H       Y
# A     S I     B
# Y   I   R   A
# P L     I B
# A       N
#
# P         R         _
# A       I I       _
# Y     H   N     1
# P   S     G   Y
# A I       B B
# L         A
# 2 > 1
# 3 > 3
# 4 > 5
# 5 > 7
# 6 > 9 ... 2*(x-2) + 1
