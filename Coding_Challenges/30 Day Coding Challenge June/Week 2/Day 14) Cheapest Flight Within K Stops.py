from collections import defaultdict
import heapq


class myslowSolution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        destDict = defaultdict(set)
        for s, d, p in flights:
            destDict[s].add((d, p))

        self.prices = []
        heapq.heapify(self.prices)

        def helper(_src, _dst, curFlights, totalPrice):
            if curFlights > K or totalPrice > self.prices[0]:
                return
            for d, p in destDict[_src]:
                tp = totalPrice + p
                if d == _dst:
                    heapq.heappush(self.prices, tp)
                else:
                    helper(d, _dst, curFlights+1, tp)

        helper(src, dst, 0, 0)
        retVal = self.prices[0] if self.prices else -1
        return retVal


class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        mapp = defaultdict(dict)
        for s, d, p in flights:
            mapp[s][d] = p

        flightsHeap = []
        for d, p in mapp[src].items():
            heapq.heappush(flightsHeap, (p, d, 0))  # sorted by price

        while flightsHeap:
            price, d, k = heapq.heappop(flightsHeap)
            if k > K:
                continue
            if d == dst:
                return price

            for newd, newp in mapp[d].items():
                heapq.heappush(flightsHeap, (price+newp, newd, k+1))

        return -1
