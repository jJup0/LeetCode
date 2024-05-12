"""
You are given a sorted integer array arr containing 1 and prime numbers, where
all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction
arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of
integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Constraints:
- 2 <= arr.length <= 1000
- 1 <= arr[i] <= 3 * 10^4
- arr[0] == 1
- arr[i] is a prime number for i > 0.
- All the numbers of arr are unique and sorted in strictly increasing order.
- 1 <= k <= arr.length * (arr.length - 1) / 2
"""

import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        return self.kthSmallestPrimeFraction_good_for_small_k(arr, k)

    def kthSmallestPrimeFraction_good_for_small_k(
        self, arr: list[int], k: int
    ) -> list[int]:
        """
        Note that this is still quadratic as k may be in O(n^2)
        O(k * log(n)) / O(n)    time / space complexity
        """
        # keep a heap of the smallest unchecked fraction for each numerator possible
        min_heap: list[tuple[float, int, int]] = [
            (arr[i] / arr[-1], i, len(arr) - 1) for i in range(len(arr) - 1)
        ]
        heapq.heapify(min_heap)

        for _ in range(k - 1):
            _, numerator_idx, denominator_idx = heapq.heappop(min_heap)

            if numerator_idx == denominator_idx - 1:
                # no more denominators remaining
                continue

            # get next largest fraction with same numerator and add to heap
            heapq.heappush(
                min_heap,
                (
                    arr[numerator_idx] / arr[denominator_idx - 1],
                    numerator_idx,
                    denominator_idx - 1,
                ),
            )

        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]

    def kthSmallestPrimeFraction_naive(self, arr: list[int], k: int) -> list[int]:
        """
        Naive way, good enough for k in Theta(n)
        O(n^2 * log(n)) / O(n^2)    time / space complexity
        """
        all_fractions = sorted(
            (arr[i] / arr[j], i, j)
            for i in range(len(arr))
            for j in range(i + 1, len(arr))
        )
        for _, i, j in all_fractions:
            print(f"{arr[i]}/{arr[j]}, ", end="")
        _, i, j = all_fractions[k - 1]
        return [arr[i], arr[j]]

    def kthSmallestPrimeFraction_fast(self, arr: list[int], k: int) -> list[int]:
        """
        Binary search approach. I did not fully grasp it yet, but it is a lot faster than the other implementations.
        Worst case time complexity seems to be the same however.
        """

        def find_fractions_larger_than(max_value: float) -> tuple[int, int, int]:
            nb_smallest_fraction = 0
            largest_frac_num = arr[0]
            largest_frac_denom = arr[-1]
            largest_frac_value = largest_frac_num / largest_frac_denom

            curr_num_idx = 0
            for curr_denom_idx in range(1, len(arr)):
                curr_frac_value = arr[curr_num_idx] / arr[curr_denom_idx]
                while curr_num_idx < curr_denom_idx and curr_frac_value < max_value:
                    if curr_frac_value > largest_frac_value:
                        largest_frac_num = arr[curr_num_idx]
                        largest_frac_denom = arr[curr_denom_idx]

                    curr_num_idx += 1
                    curr_frac_value = arr[curr_num_idx] / arr[curr_denom_idx]

                nb_smallest_fraction += curr_num_idx

            return nb_smallest_fraction, largest_frac_num, largest_frac_denom

        l = arr[0] / arr[-1]
        r = 1

        while l < r:
            m = (l + r) / 2

            count, numer, denom = find_fractions_larger_than(m)

            if count == k:
                return [numer, denom]

            if count > k:
                r = m
            else:
                l = m

        raise ValueError("`arr` is not a sorted list of primes")
