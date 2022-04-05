class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        # store the highest digit present starting from least significant
        highest_digit = 0
        for i in range(len(nums) - 1, -1, -1):
            # iterate through digits while they are non-decreasing
            if nums[i] >= highest_digit:
                highest_digit = nums[i]
            else:
                # found a digit lower than previous ones, this one will be switched out with
                # the closest next highest digit of all less significant digits
                # local store for efficiency
                firstnum = nums[i]
                # since digits are non-decreasing from least significant to nums[i], find
                # first one that is bigger, it will be the closest one
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > firstnum:
                        # switch the digits
                        nums[i] = nums[j]
                        nums[j] = firstnum
                        break
                # sort the rest of the digits to get the "first" permutation of them
                nums[i+1:] = sorted(nums[i+1:])
                break
        else:
            # nums is in reverse sorted order, which is the last permutation,
            # so sort in normal order for first permutation
            nums.sort()
