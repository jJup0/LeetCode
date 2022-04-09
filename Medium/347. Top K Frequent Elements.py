import itertools
from collections import Counter
from typing import List


class Solution:
    # O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a counter of nums in O(n)
        c = Counter(nums)

        # Initialize a buckets array in O(n)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Insert values from the counter into the buckets array in O(n)
        for val, count in c.items():
            buckets[count].append(val)

        # Merge the values from the buckets array to get them in order of frequency in O(n)
        sorted_nums = list(itertools.chain.from_iterable(buckets))
        # Slice the first k elements in O(k)
        return sorted_nums[-k:]
