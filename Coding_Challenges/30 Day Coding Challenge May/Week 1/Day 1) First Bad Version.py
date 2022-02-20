class Solution:
    def firstBadVersion(self, n):
        low, high = 1, n
        while high > low:
            mid = low + ((high-low)//2)
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return int(high)


def isBadVersion(val):
    pass
