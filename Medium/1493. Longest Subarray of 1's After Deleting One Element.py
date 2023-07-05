class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        return self._longestSubarray_o_1_space(nums)

    def _longestSubarray_o_1_space(self, nums: list[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        # - None if never had
        # - the length of the previous one's-streak after a single 0
        # - else 0
        previous_one_streak = None

        # length of current one's-streak
        curr_one_streak = 0
        # length of longest streak of one's interrupted by at most one 0
        result = 0
        for n in nums:
            if n == 1:
                curr_one_streak += 1
            else:
                # n == 0
                if previous_one_streak == None:
                    # if no previous one's-streak exists, set it to 0
                    # temporarily to add to curr_one_streak
                    previous_one_streak = 0

                result = max(result, previous_one_streak + curr_one_streak)

                # update previous streak
                previous_one_streak = curr_one_streak
                # set current streak to 0
                curr_one_streak = 0

        if previous_one_streak is None:
            # if entire array is 1's, remove one of them
            return len(nums) - 1

        # possible that there is a current streak, so return maximum of result
        # and current + previous streak
        return max(result, previous_one_streak + curr_one_streak)

    def _longestSubarray_o_n_space(self, nums: list[int]) -> int:
        """Gather streaks of ones, and then connect two streaks if possible.

        O(n) / O(n)  time / space complexity
        """
        prev = 0
        # ones[i] = (start, stop) = ith streak of ones in nums starting
        # at `start` (inclusive) and ending at `stop` (exclusive)
        ones: list[tuple[int, int]] = []
        ones_start = 0
        for i, num in enumerate(nums):
            if num == 0:
                if prev == 1:
                    ones.append((ones_start, i))
            else:
                # num == 1
                if prev == 0:
                    ones_start = i
            prev = num
        if prev == 1:
            ones.append((ones_start, len(nums)))

        res = 0
        prev_start = prev_end = -2  # set to impossible index
        for start, end in ones:
            if start == prev_end + 1:
                res = max(res, end - prev_start - 1)
            else:
                res = max(res, end - start)
            prev_start, prev_end = start, end

        # if entire array is 1s, need to remove at least one,
        # therefore min(res, len(nums) - 1) instead of simply res
        return min(res, len(nums) - 1)
