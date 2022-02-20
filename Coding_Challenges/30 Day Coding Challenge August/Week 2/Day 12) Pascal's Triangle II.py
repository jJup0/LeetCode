import math


class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        factorials = [1] * (rowIndex+1)
        for i in range(1, len(factorials)):
            factorials[i] = factorials[i-1] * i

        retList = [1] * ((rowIndex+2)//2)
        for i in range((rowIndex+2)//2):
            retList[i] = int(factorials[rowIndex]/(factorials[i] * factorials[rowIndex-i]))

        return retList + retList[::-1] if rowIndex % 2 else retList + retList[-2::-1]
