"""
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1).
A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 2 * 10^4
- 0 <= k < nums.length
"""


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        return self.maximumScore_iterative(nums, k)

    def maximumScore_recursive(self, nums: list[int], k: int) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        # result variable
        res = 0
        # visited subarray spans
        visited: set[tuple[int, int]] = set()

        def helper(i: int, j: int, curr_min: int) -> None:
            """
            Recursively finds longest good subarray for a given minimum value.

            Args:
                i (int): Starting index of subarray, inclusive.
                j (int): Ending index of subarray, inclusive.
                curr_min (int): Minimum value of nums[i:j+1]
            """
            nonlocal nums, res, visited

            # calculate score of current subarray, and update res
            res = max(res, (j - i + 1) * curr_min)
            # if ends of array reached, return
            if i == 0 and j == len(nums) - 1:
                return
            # mark subarray span as visited
            visited.add((i, j))

            # unless i == j == k, or i == 0, or j == len(nums) - 1 then
            # nums[i-1] and nums[j+1] will be smaller than curr_min
            # get these new minimum values
            next_left_min = next_right_min = curr_min
            if i > 0:
                next_left_min = min(curr_min, nums[i - 1])
            if j < len(nums) - 1:
                next_right_min = min(curr_min, nums[j + 1])

            # iterate over two new minimum values
            for new_min in (next_left_min, next_right_min):
                new_i = i
                new_j = j
                # expand the subarray as much as possible while maintaining minimum value
                while new_i > 0 and nums[new_i - 1] >= new_min:
                    new_i -= 1
                while new_j < len(nums) - 1 and nums[new_j + 1] >= new_min:
                    new_j += 1
                if (new_i, new_j) in visited:
                    # if "new" subarray has previously been checked, skip
                    continue

                # recurse with new good subarray
                helper(new_i, new_j, new_min)

        helper(k, k, nums[k])
        return res

    def maximumScore_iterative(self, nums: list[int], k: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        n = len(nums)
        res = min_val = nums[k]
        # l and r are exclusive bounds for
        l = r = k
        while l >= 0 or r < n:
            # expand subarray until l and r are out of bounds or they point
            # to numbers smaller than the current minimum value
            while l >= 0 and nums[l] >= min_val:
                l -= 1
            while r < n and nums[r] >= min_val:
                r += 1

            # subtract 2 from length of subarray as l and k are exlusive
            res = max(res, (r - l + 1 - 2) * min_val)

            # next minimum value is the maximum of the values that l and r point at
            min_val = max(nums[l] if l >= 0 else 0, nums[r] if r < n else 0)

        return res
