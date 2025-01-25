"""
You are given a 0-indexed array of positive integers nums and a positive
integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and
nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing
the operation any number of times.

An array a is lexicographically smaller than an array b if in the first
position where a and b differ, array a has an element that is less than the
corresponding element in b. For example, the array [2,10,3] is
lexicographically smaller than the array [10,2,3] because they differ at index
0 and 2 < 10.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= limit <= 10^9
"""

from collections import Counter, deque


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        return self.lexicographicallySmallestArray_v2(nums, limit)

    def lexicographicallySmallestArray_v2(
        self, nums: list[int], limit: int
    ) -> list[int]:
        """
        Iterate through sorted numbers putting them into groups, where
        a number is in its previous numbers group if they are at most
        `limit` apart, otherwise put them in a new group.
        Keep track of which group a number belongs to, then sort the array
        by popping the smallest unused number in a group of the current
        number.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        nums_sorted = sorted(nums)
        # previous value, initialize with dummy value out of reach for smallest number
        prev_num = nums_sorted[0] - (limit + 1)
        # group partitions for numbers within `limit` of each other
        groups: list[deque[int]] = []
        # mapping from num to which group they are in
        num_to_group_idx: dict[int, int] = {}
        for num in nums_sorted:
            if prev_num + limit < num:
                # num is not in range of previous number, make new group
                groups.append(deque())
            groups[-1].append(num)
            num_to_group_idx[num] = len(groups) - 1
            prev_num = num

        # sort array by popping smallest unused number from group of current number
        return [groups[num_to_group_idx[num]].popleft() for num in nums]

    def lexicographicallySmallestArray_first_submitted_version(
        self, nums: list[int], limit: int
    ) -> list[int]:
        """
        First submitted version. Same aysmptotic complexities, but unecessarily complex code.
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        nums_sorted = sorted(set(nums))
        # groups: dict[int, list[int]] = {}
        groups: list[list[int]] = []
        num_to_group_id: dict[int, int] = {}
        i = 0
        for j, num in enumerate(nums_sorted):
            while nums_sorted[i] + limit < num:
                i += 1

            if i != j:
                # num is part of previous gang
                # groups[num] = groups[nums_sorted[i]]
                groups[-1].append(num)
                num_to_group_id[num] = len(groups) - 1
            else:
                # num cannot reach any smaller number
                # groups[num] = [num]
                groups.append([num])

            num_to_group_id[num] = len(groups) - 1

        counter = Counter(nums)
        groups_full_nums: list[list[int]] = [[] for _ in range(len(groups))]
        for group_id, group in enumerate(groups):
            for num in group:
                groups_full_nums[group_id].extend([num] * counter[num])

        groups_full_nums_iter = [iter(full_nums) for full_nums in groups_full_nums]

        res: list[int] = []
        for num in nums:
            group_id = num_to_group_id[num]
            next_val = next(groups_full_nums_iter[group_id])
            res.append(next_val)
        return res
