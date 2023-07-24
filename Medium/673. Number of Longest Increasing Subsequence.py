class Solution:
    """
    Given an integer array nums, return the number of longest increasing subsequences.

    Notice that the sequence has to be strictly increasing.

    Constraints:
    - 1 <= nums.length <= 2000
    - -10^6 <= nums[i] <= 10^6
    """

    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        # lengths[i] = max length for nums[:i+1]
        lengths = [1] * n
        # counts[i] = amount of longest increasing subsequences for nums[:i+1]
        counts = [1] * n

        for i in range(1, n):
            for j in range(i):
                # if current number is smaller equal to previous number, cannot
                # "build on" previous subsequence ending with nums[j]
                if nums[i] <= nums[j]:
                    continue

                # if maximum subsequence length for nums[:j+1] is longer than
                # current longest subsequence for nums[:i+1] including nums[j]
                # then increase length
                if lengths[j] + 1 > lengths[i]:
                    # there is a new longest subsequence for nums[:i+1] by
                    # using the longest subsequences of nums[:j+1]
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    # appending nums[i] to the end of the longest subsequences of
                    # nums[:j+1] creates an equally long subsequence as was
                    # previously discovered for nums[:i+1]
                    counts[i] += counts[j]
                # else if shorter, then no point in adding nums[j] to subsequences
                # that nums[i] is part of, it will not be longest

        max_length = max(lengths)
        return sum(
            count for length, count in zip(lengths, counts) if length == max_length
        )
