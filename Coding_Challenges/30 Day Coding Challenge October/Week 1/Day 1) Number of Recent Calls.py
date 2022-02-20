import bisect
class RecentCounter:
    def __init__(self):
        self.calls = []        

    def ping(self, t: int) -> int:
        self.calls.append(t)
        return len(self.calls) - bisect.bisect(self.calls, t-3001)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)