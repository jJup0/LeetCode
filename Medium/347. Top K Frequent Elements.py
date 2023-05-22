import collections
import heapq
import itertools
from collections import Counter
from typing import List


class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.

    Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Similar approach to bucket sort.
        O(n) / O(n)     time / space complexity
        """
        # Create a counter of nums in O(n)
        c = Counter(nums)

        # Initialize a buckets array in O(n)
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        # Insert values from the counter into the buckets array in O(n)
        for val, count in c.items():
            buckets[count].append(val)

        # Merge the values from the buckets array to get them in order of frequency in O(n)
        frequency_sorted_nums = list(itertools.chain.from_iterable(buckets))
        # Slice the last k elements in O(k)
        return frequency_sorted_nums[-k:]

    def n_log_k_solution(self, nums: list[int], k: int) -> list[int]:
        counts = list(collections.Counter(nums).items())
        largest = heapq.nlargest(k, counts, key=lambda x: x[1])
        return [value for value, _ in largest]
