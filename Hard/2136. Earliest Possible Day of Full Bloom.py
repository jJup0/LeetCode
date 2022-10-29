from typing import List


class Solution:
    """
    You have n flower seeds. Every seed must be planted first before it can begin to grow, then
    bloom. Planting a seed takes time and so does the growth of a seed. You are given two 0-indexed
    integer arrays plantTime and growTime, of length n each:

      plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can
        work on planting exactly one seed. You do not have to work on planting the same seed on
        consecutive days, but the planting of a seed is not complete until you have worked
        plantTime[i] days on planting it in total.
      growTime[i] is the number of full days it takes the ith seed to grow after being completely
        planted. After the last day of its growth, the flower blooms and stays bloomed forever.
        From the beginning of day 0, you can plant the seeds in any order.

    Return the earliest possible day where all seeds are blooming.

    Constraints:
        n == plantTime.length == growTime.length
        1 <= n <= 10^5
        1 <= plantTime[i], growTime[i] <= 10^4
    """

    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        Example https://assets.leetcode.com/uploads/2021/12/21/2.png showed some interleavings of
        plant times, however this cannot improve solution, and at most delays the final blooming 
        day.
        Zip plant and grow time a sort by growTime decscending. Earliest full bloom time is 
        min(sum(plantTime) + growTime[-1], sum(plantTime[:-1]) + growTime[-2] ...)
        Greedily plant in descending grow time, and calculate maximum remaining time at each step.
        Add final remaining grow time to total plant time.
        
        O(n * log(n)) / O(n)    time / space complexity
        """

        pg = [(g, p) for g, p in zip(growTime, plantTime)]
        pg.sort(reverse=True)
        grow_rem = 0
        for grow, plant in pg:
            grow_rem = max(grow_rem - plant, grow)

        return sum(plantTime) + grow_rem
