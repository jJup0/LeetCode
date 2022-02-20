class Solution:
    def sortColors(self, nums: [int]) -> None:
        def quicksort(slist, lo, hi):
            if lo < hi:     #else nothing left to sort
                p = partition(slist, lo, hi)
                quicksort(slist, lo, p - 1)
                quicksort(slist, p + 1, hi)

        def partition(slist, lo, hi):
            pivot = slist[hi]
            i = lo
            for j in range(lo, hi):
                if slist[j] < pivot:
                    slist[i], slist[j] = slist[j], slist[i]
                    i += 1
            slist[i], slist[hi] = slist[hi],  slist[i]
            return i
        quicksort(nums, 0, len(nums)-1)
