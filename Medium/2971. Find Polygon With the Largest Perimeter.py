"""
You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side
of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a_1, a_2, a_3, ...,
a_k where a_1 <= a_2 <= a_3 <= ... <= a_kanda_1 + a_2 + a_3 + ... + a_k-1 >
a_k, then there always exists a polygon with k sides whose lengths are a_1,
a_2, a_3, ..., a_k.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed
fromnums, or-1if it is not possible to create a polygon.

Constraints:
- 3 <= n <= 10^5
- 1 <= nums[i] <= 10^9
"""


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        Simply follow the rules given to form a polygon. Sort nums in descending order,
        and greedily return as soon as a long enough longest side is found.
        O(n * log(n)) / O(n)    time / space complexity
        """
        nums.sort(reverse=True)
        # total length of all sides
        total_length = sum(nums)
        # need at least 3 numbers for a polygon, so iterate until len(nums)-2
        for i in range(len(nums) - 2):
            longest_side = nums[i]
            total_length -= longest_side
            if total_length > longest_side:
                return total_length + longest_side
        # no set of edges exist
        return -1
