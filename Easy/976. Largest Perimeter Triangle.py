import heapq
from typing import List


class Solution:
    """
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
    formed from three of these lengths. If it is impossible to form any triangle of a non-zero
    area, return 0.

    Constraints:
        3 <= nums.length <= 10^4
        1 <= nums[i] <= 10^6
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Given the fact that at each iteration the biggest side length must decrease at least by a
        factor of two, for an instance of nums where no triangle is possible, it can at most have a
        length of at most log(max_val). 
        Example, the longest possible length of nums with 128 being the largest value:
        [128, 64, 32, 16, 8, 4, 2, 1]
        The approach of 128, 64, 63... does not work:
        [128, 64, 63, 1]
        Using a heap means that for "sorting" happens in O(n), and only log(max_val) items will be 
        popped from the heap.

        O(n + log(n) * log(max_val)) / O(1)     time / space complexity
        """

        # create a max heap of nums by negating all values and calling heapify
        for i, num in enumerate(nums):
            nums[i] = -num
        heapq.heapify(nums)

        # triangle lengths, a = largest, b = second largest
        a = -heapq.heappop(nums)
        b = -heapq.heappop(nums)
        while nums:
            # get third largest not checked length from heap
            c = -heapq.heappop(nums)

            # if the two shorter length are bigger than the biggest length a triable can be formed
            if b + c > a:
                return a + b + c

            # else replace biggest length with second biggest, and second biggest with third
            a = b
            b = c

        # no triangle found, return 0
        return 0

    def largestPerimeter_simple(self, nums: List[int]) -> int:
        """
        Greedily check largest unchecked value and the two following values, a valid triangle can
        be constructed if the two following lengths are larger than the current length. If so
        return sum of these lengths.

        O(n * log(n)) / O(1)    time / space complexity
        """

        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return sum(nums[i:i+3])

        return 0


"""
So first thought was like every other solution, sort the array, and iterate through it until three sides are found where the sum of the two smaller ones is larger than the third.
Due to the sorting this runs in O(n * log(n)) time, however I think one can do better.
Time is wasted sorting the entire array when the three largest sides are already the solution.

The entire list must only be searched through in the case where no triangle is possible. If no triangle is possible, at each iteration the biggest side length must decrease at least by a factor of two, therfore nums can at most have a length of at log(max_val).
Even if a triangle is to be found, this must happen after a maximum of log(max_val) iterations for the same reason.

Example, the longest possible length of nums without a triangle, with 128 being the largest value: [128, 64, 32, 16, 8, 4, 2, 1]
Further example: the approach of 128, 64, 63... does not work: [128, 64, 63, 1]

Since creating a heap only takes O(n) time, and at most log(max_val) calls to heappop will occur, it should be faster:

def largestPerimeter(self, nums: List[int]) -> int:
        # create a max heap of nums by negating all values and calling heapify
        for i, num in enumerate(nums):
            nums[i] = -num
        heapq.heapify(nums)
        
        # triangle lengths, a = largest, b = second largest
        a = -heapq.heappop(nums)
        b = -heapq.heappop(nums)
        while nums:
            # get third largest not checked length from heap
            c = -heapq.heappop(nums)
            
            # if the two shorter length are bigger than the biggest length a triable can be formed
            if b + c > a:
                return a + b + c
            
            # else replace biggest length with second biggest, and second biggest with third
            a = b
            b = c
        
		# no triangle found, return 0
        return 0
Therefore this algorithm has O(n + log(n) * log(max_val)) time complexity and O(1) space complexity.
Due to the test instances being so small, and built in sort being rather fast, this sadly does not perform better when measured.

If there is anything I missed in my thinking or any mistake I made concerning the time complexity please let me know!
"""
