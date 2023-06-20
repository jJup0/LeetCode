class Solution:
    """
    You are given a 0-indexed array nums of n integers, and an integer k.

    The k-radius average for a subarray of nums centered at some index i with
    the radius k is the average of all elements in nums between the indices
    i - k and i + k (inclusive). If there are less than k elements before
    or after the index i, then the k-radius average is -1.

    Build and return an array avgs of length n where avgs[i] is the k-radius
    average for the subarray centered at index i.

    The average of x elements is the sum of the x elements divided by x, using
    integer division. The integer division truncates toward zero, which means
    losing its fractional part.

    For example, the average of four elements 2, 3, 1, and 5 is
    (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

    Constraints:
    - n == nums.length
    - 1 <= n <= 10^5
    - 0 <= nums[i], k <= 10^5
    """

    def getAverages(self, nums: list[int], k: int) -> list[int]:
        """Sliding window sum method.
        O(n) / O(n)     time / space complexity
        """
        n = len(nums)
        res = [-1] * n
        two_k_plus_1 = 2 * k + 1

        if two_k_plus_1 > n:
            return res

        curr_sum = sum(nums[:two_k_plus_1])
        res[k] = curr_sum // two_k_plus_1

        for i in range(k + 1, len(nums) - k):
            # slide sum window one to the right
            curr_sum = curr_sum - nums[i - k - 1] + nums[i + k]
            res[i] = curr_sum // two_k_plus_1
        return res
