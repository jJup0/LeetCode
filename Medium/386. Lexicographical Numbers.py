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
        Keep track of current number. Add trailing zeros if this keeps the
        current number below n. Otherwise add 1 and remove all trailing zeros.

        Removal of trailing zeroes accounts for 10% extra steps.
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        res: list[int] = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                # adding extra 0 gives next lexicographical number
                curr *= 10
            else:
                # if we reached n we have to remove trailing digit
                if curr == n:
                    curr = curr // 10
                # next lexicographical number is next number
                curr += 1
                # but we remove next number's trailing zeros, these will be
                # added back in subsequent numbers
                while curr % 10 == 0:
                    curr //= 10
        return res

    def lexicalOrder_heap(self, n: int) -> list[int]:
        """
        Technically against the "rules", but here log(n) == 4 which imo is constant.
        Complexity:
            Time: O(n * log(n))
            Space: O(log(n))
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

    def lexicalOrder_trivial(self, n: int) -> list[int]:
        """Trivial implementation, used to check faster implementations."""
        strs = sorted(str(i) for i in range(1, n + 1))
        return [int(s) for s in strs]


def test():
    sol = Solution()
    for i in range(1000):
        res = sol.lexicalOrder(i)
        real = sol.lexicalOrder_trivial(i)
        assert res == real


test()
