class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        curLen = len(str(low))
        retList = []
        while curLen <= len(str(high)):
            addedDigits = int("1" * curLen)
            curLen += 1
            curNum = 0
            for i in range(1, curLen):
                curNum = curNum*10 + i
            while curNum <= high and curNum % 10 and curNum < 10**curLen:
                if curNum >= low:
                    retList.append(curNum)
                curNum += addedDigits

        return retList
