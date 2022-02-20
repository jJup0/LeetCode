class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        prevSums, result, countSum = {0: -1}, 0, 0
        for i, num in enumerate(nums):
            countSum += num and 1 or -1  # if num is 1 add one, if num is 0 subtract 1
            if countSum in prevSums:
                result = max(result, i - prevSums[countSum])
            else:
                prevSums[countSum] = i
        return result


class FailSolution:
    def findMaxLength(self, nums: [int]) -> int:
        count, lowestC, highestC = 0, 1, -1
        totalsDict = dict()  # [first occurance, second occurance, first occurance one or zero]
        for i, x in enumerate(nums):
            count += x and 1 or -1  # if num is 1 add one, if num is 0 subtract 1
            # print(x, count)
            if count in totalsDict:
                totalsDict[count][1] = i
            else:
                totalsDict[count] = [i, i, x]
            if count > highestC:
                highestC = count
            elif count < lowestC:
                lowestC = count

        curTotalVal = lowestC
        retVal = 0
        while curTotalVal < highestC:
            print(curTotalVal, end=': ')
            if totalsDict[curTotalVal][2]:
                if curTotalVal in totalsDict:
                    retVal = max(retVal, totalsDict[curTotalVal-1][1]-totalsDict[curTotalVal][0])
                    print(retVal)
            else:
                retVal = max(retVal, totalsDict[curTotalVal+1][1]-totalsDict[curTotalVal][0])
                print(retVal)

            curTotalVal += 1
        return retVal + 1
