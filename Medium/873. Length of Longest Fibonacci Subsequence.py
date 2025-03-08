"""
A sequence x_1, x_2,..., x_n is Fibonacci-like if:
- n >= 3
- x_i + x_i+1 == x_i+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence,
return the length of the longest Fibonacci-like subsequence of arr. If one does
not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of
elements (including none) from arr, without changing the order of the remaining
elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

Constraints:
- 3 <= arr.length <= 1000
- 1 <= arr[i] < arr[i + 1] <= 10^9
"""

from collections import defaultdict


class Solution1:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """
        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        # previous_fib_tails[pair_sum][last_num] = longest fibonacci sequence
        # which needs `pair_sum` as the next value and ends with `num`
        previous_fib_tails: dict[int, dict[int, int]] = defaultdict(
            lambda: defaultdict(int)
        )
        for i, num in enumerate(arr):
            # iterate through previous fibonacci sequences,
            # which need `num` as the next value
            for last_value, length in previous_fib_tails[num].items():
                # update length of fibonacci sequence which would need `num + last_value`,
                # with `num` as the last value
                previous_fib_tails[num + last_value][num] = max(
                    previous_fib_tails[num + last_value].get(num, 0), length + 1
                )

            # add fibonacci sequence of length 2 for all previous numbers
            for j in range(i):
                previous_fib_tails[num + arr[j]].setdefault(num, 2)

        res = max(
            max(fib_tails.values(), default=0)
            for fib_tails in previous_fib_tails.values()
        )
        if res < 3:
            return 0
        return res


class Solution2:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """
        Use of lists and early exits make this much faster in practice.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        # dp[i][j] = longest fibonacci sequence ending with arr[i], arr[j]
        dp = [[0] * len(arr) for _ in range(len(arr))]
        # Frozen mapping from value in arr to its index. Usually this would
        # have to be filled during iteration, but since arr is strictly
        # increasing, we can optimize by initializing it with all values,
        # since only smaller values are looked up.
        value_to_index = {value: index for index, value in enumerate(arr)}
        result = 0
        # iterate through all numbers in arr as candidates for the last number of a fibonacci sequence
        for last_idx, last_num in enumerate(arr):
            # iterate through all previous numbers as a candidate for the second last number in a fibonacci sequence
            for second_last_idx in range(last_idx - 1, 0, -1):
                second_last_num = arr[second_last_idx]
                if second_last_num * 2 <= last_num:
                    # break early, second number is too small to form fibonacci tail with last number
                    break

                # check if matching third-last number exists
                third_last_idx = value_to_index.get(last_num - second_last_num, None)
                if third_last_idx is not None:
                    dp[second_last_idx][last_idx] = max(
                        dp[third_last_idx][second_last_idx] + 1, 3
                    )
                    result = max(result, dp[second_last_idx][last_idx])
        return result


class Solution(Solution2):
    pass


def test():
    s = Solution()
    res = s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8])
    assert res == 5, res


def performance_test():
    s = Solution()

    import random
    import time

    for arr_size_magnitude in range(1, 5):
        for num_magnitude in range(arr_size_magnitude, 9):
            arr = sorted(
                set(
                    random.randint(1, 10**num_magnitude)
                    for _ in range(10**arr_size_magnitude)
                )
            )
            # print(arr)
            start = time.perf_counter_ns()
            s.lenLongestFibSubseq(arr)
            print(
                f"{arr_size_magnitude=} {num_magnitude=} {(time.perf_counter_ns()-start)/1_000_000:.3f}ms"
            )
