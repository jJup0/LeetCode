from typing import List


class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    Constraints:
        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    """

    def firstVersionLongestConsecutive(self, nums: List[int]) -> int:
        # mapping from endpoints to current intervals
        endpoints = {}

        # iterate over set to ignore duplicates
        for num in set(nums):

            # check if exiting interval with end_value == num-1
            dec = num - 1
            if dec in endpoints:
                # fetch interval where num-1 is the end value
                interval = endpoints[dec]
                # delete the mapping for the previous endpoint, if it is not also the start
                if interval[0] != interval[1]:
                    del endpoints[dec]
                # update the new interval bounds, and update mapping of num
                interval[1] = num
                endpoints[num] = interval

            # check if exiting interval with start_value == num-1
            inc = num + 1
            if inc in endpoints:
                # analogous to above
                interval = endpoints[inc]
                if interval[0] != interval[1]:
                    del endpoints[inc]
                interval[0] = num

                # if num-1 was an interval boundary, merge the intervals
                if num in endpoints:
                    dec_interval = endpoints[num]
                    interval[0] = dec_interval[0]

                    del endpoints[num]
                    endpoints[interval[0]] = interval
                else:
                    # else update mapping of none
                    endpoints[num] = interval

            elif not num in endpoints:
                # if neither num-1 nor num+1 were boundaries, create new interval
                endpoints[num] = [num, num]

        # calculate size of maximum interval, 0 if nums was empty
        return max(j - i for i, j in endpoints.values()) + 1 if endpoints else 0
    
    def longestConsecutive(self, nums: List[int]) -> int:
        # result variable
        longest_streak = 0
        
        # create set of nums in O(n)
        num_set = set(nums)

        for num in num_set:
            # if num has a predecessor, skip
            if num - 1 not in num_set:
                # else num is the smallest number in a consecutive sequence
                sequence_end = num + 1
                
                # find length of sequence starting with num, by checking if successors in set
                while sequence_end in num_set:
                    sequence_end += 1

                # update result if longer
                streak = sequence_end - num
                if streak > longest_streak:
                    longest_streak = streak

        return longest_streak
