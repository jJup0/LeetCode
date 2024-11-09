"""
You are given two integers n and x. You have to construct an array of positive
integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater
than nums[i], and the result of the bitwise AND operation between all elements
of nums is x.

Return the minimum possible value of nums[n - 1].

Constraints:
- 1 <= n, x <= 10^8
"""


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """Set unset bits in x to n-1 to get smallest nums[n-1].

        Since all bits in x have to remain set, we can treat unset
        bits as ones we can "increment" to get nums[i].

        Complexity:
            Time: O(log(n) + log(x))
            Space: O(1)
        """
        # only need to add n-1 numbers after x
        nums_to_add = n - 1
        # bitmask for iterating through
        mask_x = 1
        mask_n = 1
        while mask_n <= nums_to_add:
            # find next unset bit in x
            while mask_x & x:
                mask_x <<= 1

            if mask_n & nums_to_add:
                # we need to add n-1 numbers after x, so check
                # if its bit is set, then also set it in x
                x |= mask_x

            # move to next highest bit
            mask_x <<= 1
            mask_n <<= 1
        return x
