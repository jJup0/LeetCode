class Solution:
    """
    Given two arrays nums1 and nums2.

    Return the maximum dot product between non-empty subsequences of nums1 and
    nums2 with the same length.

    A subsequence of a array is a new array which is formed from the original
    array by deleting some (can be none) of the characters without disturbing
    the relative positions of the remaining characters. (ie, [2,3,5] is a
    subsequence of [1,2,3,4,5] while [1,5,3] is not).

    Constraints:
    - 1 <= nums1.length, nums2.length <= 500
    - -1000 <= nums1[i], nums2[i] <= 1000
    """

    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        """
        O(n * m) / O(m)     time / space complexity
        """
        NEG_INF = -1_000_000_000

        # maxmimum dot product for previous number from nums2 for subarrays
        # nums1[:i], 0 <= i < len(nums1)
        prev_dp = [NEG_INF] * (len(nums1) + 1)
        for num2 in nums2:
            # same meaning as prev_dp except for current num2
            dp = [NEG_INF] * (len(nums1) + 1)

            for i1, num1 in enumerate(nums1):
                max_prev_num1_curr_num2 = dp[i1]
                max_curr_num1_prev_num2 = prev_dp[i1 + 1]
                # use maximum of prev_dp and 0 and prev_dp may be negative
                include_curr_num1_curr_num2 = max(0, prev_dp[i1]) + num1 * num2
                dp[i1 + 1] = max(
                    max_prev_num1_curr_num2,
                    max_curr_num1_prev_num2,
                    include_curr_num1_curr_num2,
                )

            # update prev_dp for next iteration
            prev_dp = dp

        return prev_dp[-1]
