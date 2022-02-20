import numpy
# stole some optimisations from other solutions making it x1.5 faster


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # nums is already sorted
        n = len(nums)
        l, r = 1, nums[-1]
        while l < r:
            div = (l + r)//2
            # (x+div-1)//div is waaaay faster than math.ceil
            # list comprehension is also faster than summing up and breaking when sum is bigger than threshold
            currSum = sum((x+div-1)//div for x in nums)

            if currSum > threshold:
                l = div + 1
            else:
                r = div
        return l


# numpy solution, another x2 faster


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # nums is already sorted
        nums = numpy.array(nums)  # diving every element in a list is a lot faster in a numpy array
        l, r = 1, nums[-1]

        while l < r:
            div = (l + r)//2
            currSum = numpy.sum(numpy.ceil(nums/div))
            if currSum > threshold:
                l = div + 1
            else:
                r = div
        return l
