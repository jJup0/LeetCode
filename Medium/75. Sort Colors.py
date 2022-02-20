class Solution:
    def sortColors(self, nums: [int]) -> None:
        #         def quicksort(slist, lo, hi):
        #             if lo < hi:     #else nothing left to sort
        #                 p = partition(slist, lo, hi)
        #                 quicksort(slist, lo, p - 1)
        #                 quicksort(slist, p + 1, hi)

        #         def partition(slist, lo, hi):
        #             pivot = slist[hi]
        #             i = lo
        #             for j in range(lo, hi):
        #                 if slist[j] < pivot:
        #                     slist[i], slist[j] = slist[j], slist[i]
        #                     i += 1
        #             slist[i], slist[hi] = slist[hi],  slist[i]
        #             return i
        #         quicksort(nums, 0, len(nums)-1)

        # one-pass algorithm using only constant extra space?
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
