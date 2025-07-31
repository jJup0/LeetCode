"""
Given an integer array arr, return the number of distinct bitwise ORs of all
the non-empty subarrays of arr.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray.
The bitwise OR of a subarray of one integer is that integer.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= arr.length <= 5 * 10^4
- 0 <= arr[i] <= 10^9
"""

from functools import cache


class Solution1:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        self.max_bits = max(arr).bit_length()
        bit_to_last_idx = [-1] * self.max_bits
        all_discovered: set[int] = set()
        for i, num in enumerate(arr):
            search_back_until = min(
                (bit_to_last_idx[_i] for _i in self._get_set_bit_idxs(num)), default=0
            )
            unset_idxs = sorted(
                (
                    (bit_to_last_idx[_i], _i)
                    for _i in self._get_unset_bit_idxs(num)
                    if search_back_until < bit_to_last_idx[_i]
                ),
                reverse=True,
            )
            ored_num = num
            prev_idx = unset_idxs[0][0] if unset_idxs else None
            for unset_idx, bit_idx in unset_idxs:
                if unset_idx != prev_idx:
                    all_discovered.add(ored_num)
                    prev_idx = unset_idx
                ored_num |= 1 << bit_idx
            all_discovered.add(ored_num)
            all_discovered.add(num)

            for bitidx in self._get_set_bit_idxs(num):
                bit_to_last_idx[bitidx] = i
        return len(all_discovered)

    @cache
    def _get_set_bit_idxs(self, num: int):
        bitmask = 1
        i = 0
        res: list[int] = []
        while bitmask <= num:
            if bitmask & num:
                res.append(i)
            i += 1
            bitmask *= 2
        return res

    @cache
    def _get_unset_bit_idxs(self, num: int):
        set_bits_iter = iter(self._get_set_bit_idxs(num))
        next_set_bit = next(set_bits_iter, None)
        res: list[int] = []
        for i in range(self.max_bits):
            if i == next_set_bit:
                next_set_bit = next(set_bits_iter, None)
                continue
            res.append(i)
        return res


class SolutionNaive:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """No point being clever, naive is the fastest way.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        res: set[int] = set()
        cumulative: set[int] = set()
        for num in arr:
            cumulative = {prev_or | num for prev_or in cumulative}
            cumulative.add(num)
            res.update(cumulative)
        return len(res)


class Solution(SolutionNaive):
    pass


def test():
    sol = Solution()
    res = sol.subarrayBitwiseORs([1, 1, 2])
    assert res == 3, res
    res = sol.subarrayBitwiseORs([1, 2, 4])
    assert res == 6, res


def test_performance():
    import random

    sol = Solution()
    sol.subarrayBitwiseORs([random.randint(1, 10**9) for _ in range(10**4)])
