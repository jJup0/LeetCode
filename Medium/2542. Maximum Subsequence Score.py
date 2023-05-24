import heapq


class Solution:
    """
    You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and
    a positive integer k. You must choose a subsequence of indices from nums1 of length k.

    For chosen indices i0, i1, ..., ik - 1, your score is defined as:

        The sum of the selected elements from nums1 multiplied with the minimum of the
          selected elements from nums2.
        It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) *
          min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).

    Return the maximum possible score.

    A subsequence of indices of an array is a set that can be derived from the set
    {0, 1, ..., n-1} by deleting some or no elements.

    Constraints:
        n == nums1.length == nums2.length
        1 <= n <= 10^5
        0 <= nums1[i], nums2[j] <= 10^5
        1 <= k <= n

    """

    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """Sort pairs by nums2 value descending.
        Iterate through pairs always using the current pair in the subsequence.
        Track the largest nums1 values so far, and always use those in the subsequence.
        Since ordered by nums2 descending, these largest nums1 values can never
          "pull down" the value of min(nums2[i_0] ...).
        O(n * log(n)) / O(n)    time / space complexity.
        """
        # match up values from nums1 with values from nums2
        # sort by value in nums2
        zipped: list[tuple[int, int]] = sorted(
            zip(nums1, nums2), key=lambda x: x[1], reverse=True
        )

        # keep heap of largest values in nums1 so far
        largest_n1s: list[int] = [zipped[i][0] for i in range(k)]
        heapq.heapify(largest_n1s)

        # track current sum of values in nums1 heap
        curr_sum = sum(largest_n1s)

        # result variable, initial lower bound result is first k pairs with kth highest nums2 value
        max_score = zipped[k - 1][1] * curr_sum

        # iterate through remaining pairs
        for i in range(k, len(zipped)):
            n1, n2 = zipped[i]
            # push current num1 to heap, then pop (k-th) smallest num1 so far
            subtract = heapq.heappushpop(largest_n1s, n1)
            # update current sum of nums1 values
            curr_sum += n1 - subtract
            # update max score
            max_score = max(max_score, curr_sum * n2)
        return max_score
