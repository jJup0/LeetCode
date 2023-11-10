"""
There is an integer array nums that consists of n unique elements, but you have
forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each
adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent
in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will
exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]].
The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

Constraints:
- nums.length == n
- adjacentPairs.length == n - 1
- adjacentPairs[i].length == 2
- 2 <= n <= 10^5
- -10^5 <= nums[i], ui, vi <= 10^5
- There exists some nums that has adjacentPairs as its pairs.
"""
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        # build adjacency list
        adjacents: dict[int, list[int]] = defaultdict(list)
        for a, b in adjacentPairs:
            adjacents[a].append(b)
            adjacents[b].append(a)

        # there will be two nums with only one adjacent, the start and
        # end number
        # there are always two valid answers: res and res[::-1], so it
        # does not matter which number is used for start and end
        first_num = None
        for first_num, adj in adjacents.items():
            if len(adj) == 1:
                break
        assert first_num is not None

        # restore array
        res: list[int] = [first_num]
        curr_num = prev_num = first_num
        for _ in range(len(adjacents) - 1):
            # iterate through neighbors for curr_num, there are either 1 or 2
            for neighbor in adjacents[curr_num]:
                if neighbor != prev_num:
                    # only append neighbor if it has not been seen before
                    res.append(neighbor)
                    # update curr and prev num
                    prev_num = curr_num
                    curr_num = neighbor
                    break
        return res
