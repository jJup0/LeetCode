class Solution:
    def __init__(self, w: List[int]):
        total = 0
        self.totals = [(total := total+cur) for cur in w]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.totals[-1])
        lo, hi = 0, len(self.totals)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.totals[mid] < rand:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
