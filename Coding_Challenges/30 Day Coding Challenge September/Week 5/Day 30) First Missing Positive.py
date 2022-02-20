# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         nums = set(nums)
#         for i in range(1, 10**10):
#             if not i in nums:
#                 return i

class Solution:
    def firstMissingPositive(self, nums):
        len_n = len(nums)
        len_n_plus = len_n + 1  # buffer for values smaller than 0 or bigger_equal len_n

        # Replace negative numbers, zeros, and numbers larger than n by len_n_plus.
        # 0 could not be used as buffer instead of len_n_plus, as it is not positive
        # After this convertion nums will contain only positive numbers.
        for i in range(len_n):
            if nums[i] <= 0 or nums[i] > len_n:
                nums[i] = len_n_plus

        # increase len of nums by two, but keeping len_n the same
        # so that the number "len_n" can also be accomodated in the next step
        # and the nums[-1] will always be positive (len_n_plus) after next step
        nums += (len_n_plus, len_n_plus)

        # Use num as index, and sign (+ or -) at that index as a presence indicator.
        # any values that remain positive after this are at the index of a missing number
        for num in nums:
            num = abs(num)  # num could be negative, if its index number was present previously
            if (val_at_idx_num := nums[num]) > 0:
                nums[num] = -val_at_idx_num

        for i, presence in enumerate(nums[1:], start=1):
            if presence > 0:
                return i

        return len_n_plus
