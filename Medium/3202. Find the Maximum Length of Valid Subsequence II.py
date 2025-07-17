"""
You are given an integer array nums and a positive integer k.

A subsequence sub of nums with length x is called valid if it satisfies:
- (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k ==... == (sub[x - 2] + sub[x - 1]) % k.

Return the length of the longest valid subsequence of nums.

Constraints:
- 2 <= nums.length <= 10^3
- 1 <= nums[i] <= 10^7
- 1 <= k <= 10^3
"""

from collections import defaultdict


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        Try pairwise interleavings of each modulo k group.

        Worst case k >= len(nums) and nums has the structure similar to [1, 2, 3, ..., k, k, ... 3, 2, 1].

        Complexity:
            Time: O(n + k*k)
            Space: O(n)
        """
        modulo_to_indexes: dict[int, list[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            modulo_to_indexes[num % k].append(i)
        # start off setting result to the length of the biggest modulo group
        res = max(len(idxs) for idxs in modulo_to_indexes.values())

        # sort modulo group to break early during iteration
        sorted_mods = sorted(
            modulo_to_indexes.items(),
            key=lambda remainder_count: -len(remainder_count[1]),
        )
        # try pairing each modulo group with each other modulo group and
        # find the longest interleaving of the group groups
        for i in range(len(sorted_mods)):
            count1 = len(sorted_mods[i][1])
            for j in range(i + 1, len(sorted_mods)):
                count2 = len(sorted_mods[j][1])
                if count1 + count2 <= res:
                    # break early if the two groups cannot form
                    # longest interleaving so far
                    break

                # calculate longest interleaving and update res accordingly
                res = max(
                    res,
                    self._find_longest_interleaving(
                        sorted_mods[i][1], sorted_mods[j][1]
                    ),
                )
        return res

    def _find_longest_interleaving(self, l1: list[int], l2: list[int]):
        lists = [l1, l2]
        list_indexes = [0, 0]
        idx_of_last_number = -1
        if l1[0] < l2[0]:
            next_list_idx = 0
        else:
            next_list_idx = 1

        res = 0
        while True:
            # find next index of number for interleaving
            while (
                list_indexes[next_list_idx] < len(lists[next_list_idx])
                and idx_of_last_number
                > lists[next_list_idx][list_indexes[next_list_idx]]
            ):
                list_indexes[next_list_idx] += 1

            if list_indexes[next_list_idx] == len(lists[next_list_idx]):
                # reached end of next modulo group for interleaving
                break

            # update last idx to current idx
            idx_of_last_number = lists[next_list_idx][list_indexes[next_list_idx]]
            res += 1
            # at next iteration we need a number from the other list
            next_list_idx = 1 - next_list_idx
        return res


def test():
    sol = Solution()
    res = sol.maximumLength([1, 4, 2, 3, 1, 4], 3)
    assert res == 4, res


test()
