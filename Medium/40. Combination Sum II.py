"""
Given a collection of candidate numbers ( candidates ) and a target number (
target ), find all unique combinations in candidates where the candidate
numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        O(2^n) / O(2^n)     time / space complexity
        """

        def helper(curr_i: int, curr_cand_list: list[int], curr_sum: int):
            """Appends to nonlocal `res` all collections of candidates summing to target.

            Args:
                curr_i (int): Current index in candidates.
                curr_cand_list (list[int]): Current candidates for sum.
                curr_sum (int): sum(curr_cand_list)
            """
            nonlocal res, target
            if curr_sum == target:
                res.append(curr_cand_list[:])
                return

            # value of previous candidate, pseudo init with -1
            prev_candidate_val = -1
            for i in range(curr_i, len(candidates)):
                candidate_val = candidates[i]
                if candidate_val == prev_candidate_val:
                    # avoid duplicate candidate lists
                    continue

                new_sum = curr_sum + candidate_val
                if new_sum > target:
                    break
                curr_cand_list.append(candidate_val)
                helper(i + 1, curr_cand_list, new_sum)
                curr_cand_list.pop()
                prev_candidate_val = candidate_val

        # sort to return early
        candidates.sort()
        res: list[list[int]] = []
        helper(0, [], 0)
        return res
