from collections import Counter
from typing import List


class Solution:
    """
    You are given an integer array arr. You can choose a set of integers and remove all the
    occurrences of these integers in the array.
    Return the minimum size of the set so that at least half of the integers of the array are
    removed.
    Constraints:
        2 <= arr.length <= 105
        arr.length is even.
        1 <= arr[i] <= 105
    """

    def minSetSize(self, arr: List[int]) -> int:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        # result variable
        res = 0

        # number of items left to delete
        rem = len(arr) // 2

        # count occurances of each value
        c = Counter(arr)

        # iterate through them in descending count
        for _, count in sorted(c.items(), key=lambda x: -x[1]):
            # remove digits with highest occurances until less or equal to half are left
            rem -= count
            # increment result counter
            res += 1
            # if half are removed, return count
            if rem <= 0:
                return res

        raise Exception("arr has length 0")
