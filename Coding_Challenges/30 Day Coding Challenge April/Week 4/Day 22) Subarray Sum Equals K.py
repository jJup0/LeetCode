import heapq
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        prevSums = {0: 1}
        curs, retVal = 0, 0
        for num in nums:
            curs += num
            retVal += prevSums.get(curs - k, 0)
            prevSums[curs] = prevSums.get(curs, 0) + 1
        return retVal



def arr3000msSubarraySum(self, nums: [int], k: int) -> int:
    retVal, curSum = 0, 0
    sumsSoFar = [0]
    for num in nums:
        curSum += num
        retVal += sumsSoFar.count(-curSum + k)
        sumsSoFar.append(curSum)
    return retVal
        




def heapSlowsubarraySum(self, nums: [int], k: int) -> int:
    retVal, curSum = 0, 0
    sumsSoFar = [0]
    heapq.heapify(sumsSoFar)
    for num in nums:
        curSum += num
        for x in heapq.nsmallest(len(sumsSoFar), sumsSoFar):
            if curSum - x < k:
                break
            if curSum - x == k:
                retVal += 1
        heapq.heappush(sumsSoFar, curSum)
    print(heapq.nlargest(len(sumsSoFar), sumsSoFar))
    return retVal
