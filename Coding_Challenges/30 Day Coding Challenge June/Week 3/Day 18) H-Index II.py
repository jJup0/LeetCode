class Solution:
    def hIndex(self, citations: [int]) -> int:
        if not sum(citations):
            return 0
        citations.sort()
        n = len(citations)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if citations[mid] < n-mid:
                lo = mid + 1
            else:
                hi = mid - 1
        while (lo - 1 >= 0 and citations[lo - 1] > n-lo-1):
            lo -= 1
        if n-lo > citations[lo]:
            lo += 1
        return n-lo
