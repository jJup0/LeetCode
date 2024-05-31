"""
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:
- a = arr[i]^ arr[i + 1]^...^ arr[j - 1]
- b = arr[j]^ arr[j + 1]^...^ arr[k]

Note that^ denotes the bitwise-xor operation.

Return the number of triplets ( i, j and k ) Where a == b.

Constraints:
- 1 <= arr.length <= 300
- 1 <= arr[i] <= 10^8
"""

from collections import Counter, defaultdict


class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        return self.countTriplets_linear(arr)

    def countTriplets_quadratic(self, arr: list[int]) -> int:
        """
        O(n^2) / O(n^2)     time / space complexity
        """
        n = len(arr)
        # xors[i][j] = xor of arr[i:j+1]
        xors = [[0] * n for _ in range(n)]
        for start in range(n):
            xor = 0
            for end in range(start, n):
                xor ^= arr[end]
                xors[start][end] = xor

        # iterate over each j and and match xor pairings
        res = 0
        for j in range(1, n):
            # mapping from xor value to amount of subarrays ending with j-1 with that value
            xor_to_i = Counter(xors[i][j - 1] for i in range(j))
            # find matching k's
            for k in range(j, n):
                res += xor_to_i[xors[j][k]]
        return res

    def countTriplets_linear(self, arr: list[int]) -> int:
        """
        Black magic, I do not understand it.
        O(n) / O(n)     time / space complexity
        """
        res = 0
        curr_xor = 0

        # xor_counts[x] = amount of indexes i encountered so far where XOR(arr[:i+1]) == x
        xor_counts: defaultdict[int, int] = defaultdict(int)
        xor_counts[0] = 1
        # xor_idx_cumulative[x] = cumulative sum of 1-indexed indices where XOR(arr[:i+1]) == x
        xor_idx_cumulative: defaultdict[int, int] = defaultdict(int)

        for i, num in enumerate(arr):
            curr_xor ^= num

            # This is where the black magic happens, I still have not figured it out yet
            # If the current xor value has never been encountered before then both xor
            # mappings at curr_xor will be 0, so our result does not increase.
            # If we have encountered the xor_value before then xor_counts[curr_xor] >= 1.
            # Each previous occurance of curr_xor can form valid triplets with i.
            # Why we multiply by i? I do not know. Why we subtract the cumulative sums of indices. I do not know.
            res += xor_counts[curr_xor] * i - xor_idx_cumulative[curr_xor]

            # update xor dicts as decribed above
            xor_idx_cumulative[curr_xor] += i + 1
            xor_counts[curr_xor] += 1

        return res

    def countTriplets_linear2(self, arr: list[int]) -> int:
        """
        Black magic but a little different.
        O(n) / O(n)     time / space complexity
        """
        res = 0
        size = len(arr)
        # mapping of xor value to triplet (cumulative sum of of subarray count so far, number of times xor was seen, last index xor was seen)
        xor_dp: dict[int, tuple[int, int, int]] = {0: (0, 1, 0)}

        curr_xor = 0
        for i in range(1, size + 1):
            curr_xor ^= arr[i - 1]
            if curr_xor in xor_dp:
                cumu_sum_subarrs, previous_encounters, last_idx = xor_dp[curr_xor]
                res += cumu_sum_subarrs + previous_encounters * (i - last_idx - 1)
                xor_dp[curr_xor] = (
                    cumu_sum_subarrs + previous_encounters * (i - last_idx),
                    previous_encounters + 1,
                    i,
                )
            else:
                xor_dp[curr_xor] = (0, 1, i)

        return res
