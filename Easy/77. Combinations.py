from typing import List


class Solution:
    """
    Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
    You may return the answer in any order.
    Constraints:
        1 <= n <= 20
        1 <= k <= n
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, comb_idx):
            """Generates combinations
            Parameters
                start : int
                    Starting val of numbers left to chooose for combination
                comb_idx : int
                    Current index of combination which should be iterated over
                Returns
                    Nothing, only appends to combinations list
            """
            nonlocal combination
            nonlocal combinations
            # if no number left to append to combination, append a copy to result
            if comb_idx == k:
                combinations.append(combination.copy())
            else:
                # go through all values between start and n - k + comb_idx + 1
                # reason: e.g. there can not be a 5 choose 4 combination that starts with 4 (if values in permutation are in order)
                for i in range(start, n + 1 + comb_idx - k + 1):
                    combination[comb_idx] = i
                    # recursion for next value in combination, start at i + 1
                    backtrack(i + 1, comb_idx + 1)
                # pop dummy value

        # current combination in recursion
        combination = [0] * k

        # result variable
        combinations = []
        backtrack(1, 0)
        return combinations


class SlowSolution:
    # slow for some reason, designed independently
    def combine(self, n: int, k: int) -> List[List[int]]:
        fac = [1] * (n + 1)
        for i in range(2, n + 1):
            fac[i] = fac[i-1] * i

        n_choose_k = fac[n]/(fac[k] * fac[n-k])

        # arr = [None for _ in range(n_choose_k)]
        arr = [None] * k

        ret = []

        stop = n + 1

        def helper(start, idx):
            # nonlocal stop
            range_ = stop - start
            if idx == k-1:
                for val in range(start, stop):
                    arr[idx] = val
                    ret.append(arr.copy())
                return

            for val in range(start, stop):
                arr[idx] = val
                helper(val + 1, idx + 1)

        helper(1, 0)
        return ret
