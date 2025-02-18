"""
Given an array nums of distinct positive integers, return the number of tuples
(a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums,
and a!= b!= c!= d.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
- All elements in nums are distinct.
"""

from collections import Counter, defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        return self.tupleSameProduct_fast(nums)

    def tupleSameProduct_fast(self, nums: list[int]) -> int:
        """
        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        counter = Counter(
            num1 * num2 for i, num1 in enumerate(nums) for num2 in nums[i + 1 :]
        )
        return sum(count * (count - 1) * 4 for count in counter.values())

    def tupleSameProduct_slow(self, nums: list[int]) -> int:
        """Fails to use the constraint that nums is distinct list of integers.
        Complexity:
            Time: O(n^3)
            Space: O(n^2)
        """
        product_to_idx_pair: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1 :]):
                product_to_idx_pair[num1 * num2].append((num1, num2))

        res = 0
        for tuples in product_to_idx_pair.values():
            for i, (num1, num2) in enumerate(tuples):
                for j in range(i + 1, len(tuples)):
                    num3, num4 = tuples[j]
                    if num1 == num3 or num1 == num4:
                        continue
                    if num2 == num3 or num2 == num4:
                        continue
                    res += 8
        return res
