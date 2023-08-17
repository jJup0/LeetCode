import heapq


class Solution:
    """
    Given an integer array nums and an integer k, return the kth largest element
    in the array.

    Note that it is the kth largest element in the sorted order, not the kth
    distinct element.

    Can you solve it without sorting?

    Constraints:
        1 <= k <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
    """

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k < (n // 2):
            # O(k) space, good for small k
            return heapq.nlargest(k, nums)[-1]
        else:
            # O(n-k) space, good for large k
            return heapq.nsmallest(n - k + 1, nums)[-1]

    def findKthLargest_alternative(self, nums: list[int], k: int) -> int:
        """
        Create a heap for k largest elements, heap[0] == kth largest.
        O(k + (n-k) * log(k)) / O(k)  time / space complexity
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            num = nums[i]
            # if a value if larger than kth largest, pushpop to heap
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        return heap[0]
