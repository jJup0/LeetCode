"""
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:
- Its maximum element if all of its elements are consecutive and sorted in
  ascending order.
- -1 otherwise.

You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the
power of nums[i..(i + k - 1)].

Constraints:
- 1 <= n == nums.length <= 500
- 1 <= nums[i] <= 10^5
- 1 <= k <= n
"""


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        consecutive_start = 0
        prev = nums[0] - 1
        res: list[int] = []
        for i, num in enumerate(nums):
            if num != prev + 1:
                # current number broke consecutive chain, reset start index
                consecutive_start = i
            prev = num

            if i < k - 1:
                # do not append to result for first k-1 elements
                continue
            if i - consecutive_start >= k - 1:
                # nums[i-k+1:i+1] are k consecutive numbers,
                # maximum element is last (current) element
                res.append(num)
            else:
                res.append(-1)
        return res
