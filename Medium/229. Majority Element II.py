from collections import Counter


class Solution:
    """
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

    Constraints:
    - 1 <= nums.length <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9
    """

    def majorityElement(self, nums: list[int]) -> list[int]:
        return self.majorityElement_o_1_space(nums)

    def majorityElement_simple(self, nums: list[int]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        third = len(nums) // 3
        c = Counter(nums)
        return [num for num, count in c.items() if count > third]

    def majorityElement_o_1_space(self, nums: list[int]) -> list[int]:
        """
        Stolen from someone else's solution, based on Boyer-Moore Majority Voting
        Any number with more than n/3 occurances will be stored in candidate
        1 or 2 by the end of the first pass due to the fact that it's count
        can be decremented a maximum of n/3 times, and a number can only be
        kicked out from its candidate place when its counter reaches 0.
        candidates are then checked in two more passes (using .count()) for
        whether they are actual majority numbers

        O(n) / O(1)     time / space complexity
        """
        count1 = count2 = 0
        candidate1, candidate2 = 0, 1
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) / 3]
