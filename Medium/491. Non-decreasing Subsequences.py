class Solution:
    """
    Given an integer array nums, return all the different possible non-decreasing subsequences of
    the given array with at least two elements. You may return the answer in any order.

    Constraints:
        1 <= nums.length <= 15
        -100 <= nums[i] <= 100
    """

    def findSubsequences(self, nums: list[int]) -> set[tuple[int]]:
        """
        Method signature was originally list[list[int]], but implementation works with sets and
        tuples. Can easily be converted to list[list[int]], but unnecessary computation, but 
        leetcode only iterates anyways.

        O(2^n) / O(2^n)     time / space complexity
        """

        # could make some optimizations, but worst case nums is already sorted, in which case the result is exponential

        # intermediary result, use set to avoid duplicates
        non_decreasing = set()
        for num in nums:
            # create a 1 tuple of current num
            num_tuple = (num,)

            # append num to all previous non-decreasing subsequences, for which
            # the last item is smaller equal to current num
            new_non_dec = tuple(prev + num_tuple
                                for prev in non_decreasing
                                if prev[-1] <= num)

            non_decreasing.update(new_non_dec)

            # add just num by itself
            non_decreasing.add(num_tuple)

        # remove subsequences of length 1,
        # not using list comprehension with filter for performance reasons
        for num in nums:
            non_decreasing.discard((num,))
        return non_decreasing
