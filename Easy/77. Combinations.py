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
        def backtrack(start, combination):
            """Generates combinations
            Parameters
                start : int
                    Starting val of numbers left to chooose for combination
                combination : int
                    Previously generated combination
                Returns
                    Nothing, only appends to combinations list
            """
            nonlocal combinations
            # if no number left to append to combination, append to result
            if len(combination) == k:
                combinations.append(combination.copy())
            else:
                # else append dummy value, will be reassigned in loop
                combination.append(-1)
                # go through all values between start and n, or less, for example
                # there can not be a 5 choose 4 combination that starts with 4 (if values in permutation are in order)
                for i in range(start, min(n + 1, len(combination) + n - k + 1)):
                    combination[-1] = i
                    # recursion for next value in combination, start at i + 1
                    backtrack(i + 1, combination)
                # pop dummy value
                combination.pop()

        combinations = []
        backtrack(1, [])
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
