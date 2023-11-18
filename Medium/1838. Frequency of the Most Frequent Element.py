"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can
choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k
operations.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^5
"""


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """Sliding window approach.
        O(n*log(n)) / O(1)  time / space complexity
        """
        nums.sort()
        max_frequency = 0  # result
        sliding_sum = 0  # current sum of sliding window
        sliding_len = 0  # current length of sliding window
        left = 0  # left index of sliding window
        for curr_num in nums:
            sliding_sum += curr_num
            sliding_len += 1

            # all numbers can be incremented to the current number if current_sum + k >= curr_num + curr_len
            while sliding_sum + k < curr_num * sliding_len:
                # remove leftmost from sliding window
                sliding_sum -= nums[left]
                left += 1
                sliding_len -= 1

            # update result if new maximum
            max_frequency = max(max_frequency, sliding_len)

        return max_frequency
