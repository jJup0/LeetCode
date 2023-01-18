class Solution:
    """
    Given a circular integer array nums of length n, return the maximum possible sum of a non-empty
    subarray of nums.

    A circular array means the end of the array connects to the beginning of the array. Formally,
    the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is
    nums[(i - 1 + n) % n].

    A subarray may only include each element of the fixed buffer nums at most once. Formally, for
    a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with
    k1 % n == k2 % n.

    Constraints:
        n == nums.length
        1 <= n <= 3 * 10^4
        -3 * 10^4 <= nums[i] <= 3 * 10^4
    """

    def maxSubarraySumCircular(self, A: list[int]) -> int:
        """
        If maximum subarray uses circular property, just subtract smallest subarray from entire sum.
        Else just use normal maximum subarray.
        O(n) / O(1)     time / space complexity
        """

        # sum of minimum and maximum sub array so far (ignoring circular)
        min_so_far = 10**10
        max_so_far = -10**10

        # minimum and maximum subarray if ending at current index in A (in for loop)
        min_curr = max_curr = 0
        for num in A:
            # if max_curr is negative 'discard' previous subarray, i.e. set max_curr to current
            # value, otherwise add current value
            if max_curr < 0:
                max_curr = num
            else:
                max_curr += num

            # if max_curr is positive 'discard' previous subarray, i.e. set min_curr to current
            # value, otherwise add current value
            if min_curr > 0:
                min_curr = num
            else:
                min_curr += num

            # update global maximum subarray sums
            max_so_far = max(max_so_far, max_curr)
            min_so_far = min(min_so_far, min_curr)

        # calculate total sum
        total_sum = sum(A)
        # if entire array is negative, then total_sum == min_so_far, and so the greatest subbarray
        # would technically be empty, but the question requires the array be non empty, so return
        # max_so_far
        if total_sum == min_so_far:
            return max_so_far

        # else return the maximum between the max-sum subarray so far (makes no use of circular
        # property), and the total array minus the minimum subarray (makese use of circular
        # property, virtually slicing out the smallest (will be negative) subbarray from
        # somewhere within the array)
        return max(max_so_far, total_sum-min_so_far)
