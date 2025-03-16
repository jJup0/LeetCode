"""
You are given an integer array ranks representing the ranks of some mechanics.
ranks_i is the rank of the ith mechanic. A mechanic with a rank r can repair n
cars in r * n^2 minutes.

You are also given an integer cars representing the total number of cars
waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

Constraints:
- 1 <= ranks.length <= 10^5
- 1 <= ranks[i] <= 100
- 1 <= cars <= 10^6
"""

import heapq
from collections import Counter


class Solution1:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """Binary search approach.

        Complexity:
            Time: O(n * log((c/n) ^ 2))
            Space: O(n)
        """
        l = 1
        r = sum(ranks) * ((cars // len(ranks)) + 1) ** 2
        while l < r:
            minutes = (l + r) // 2
            if self._can_repair_in(ranks, cars, minutes):
                print(f"can repair in {minutes=}")
                r = minutes
            else:
                print(f"can not repair in {minutes=}")
                l = minutes + 1
        return l

    def _can_repair_in(self, ranks: list[int], cars: int, minutes: int):
        for rank in ranks:
            if rank * cars * cars <= minutes:
                return True
            i = 1
            for i in range(1, cars + 1):
                if rank * i * i > minutes:
                    break
            cars -= i - 1
            if cars <= 0:
                return True
        return False


class Solution2:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """Make use of the fact that 1 <= ranks[1] <= 100.

        k := unique values in ranks
        Complexity:
            Time: O()
            Space: O(100)
        """
        # min_heap for current repairs where
        # min_heap[i] = (total_time, rank, previous_cars_repairs, mechanic_count)
        min_heap = [(rank, rank, 1, count) for rank, count in Counter(ranks).items()]
        heapq.heapify(min_heap)

        time = 1
        while cars > 0:
            # pop the mechanics with the smallest current repair time
            time, rank, n, count = heapq.heappop(min_heap)

            # each mechanic repairs one car
            cars -= count
            n += 1

            # push the updated repair time back into the heap
            heapq.heappush(min_heap, (rank * n * n, rank, n, count))
        return time


class Solution(Solution2):
    pass
