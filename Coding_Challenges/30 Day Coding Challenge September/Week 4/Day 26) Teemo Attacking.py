class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        curPoisonEnd = 0
        res = 0
        for timeStamp in timeSeries:
            newEnd = timeStamp + duration
            res += min(duration, newEnd-curPoisonEnd)
            curPoisonEnd = newEnd
        return res
