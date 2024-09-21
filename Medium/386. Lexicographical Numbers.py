"""
Given an integer n, return all the numbers in the range [1, n] sorted in
lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.

Constraints:
- 1 <= n <= 5 * 10^4
"""

import heapq


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        """
        O(n) / O(1)     time / space complexity
        """
        res: list[int] = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                # adding extra 0 gives next lexicographical number
                curr *= 10
            else:
                # if number ends in 9, or previous number was n, divide by 10 to get next lexicographical
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1
        return res

    def lexicalOrder_heap(self, n: int) -> list[int]:
        """
        Technically against the "rules", but I count log(n) as constant, in this case it is 4.
        O(n * log(n)) / O(log(n))     time / space complexity
        """
        # create heap of numbers to add
        heap: list[str] = []
        i = 1
        while i <= n:
            heap.append(str(i))
            i *= 10

        # stop adding to heap once digit limit has been reached
        limits = (9, 99, 999, 9999)

        res: list[int] = []
        while heap:
            num_str = heapq.heappop(heap)
            num_int = int(num_str)
            res.append(num_int)
            if num_int < n and num_int not in limits:
                heapq.heappush(heap, str(num_int + 1))
        return res

    def _lexical_order_trivial(self, n: int) -> list[int]:
        strs = sorted(str(i) for i in range(1, n + 1))
        return [int(s) for s in strs]
