import heapq
from typing import List


class Solution:
    """
    You are given an array target of n integers. From a starting array arr consisting of n 1's,
    you may perform the following procedure :
    let x be the sum of all elements currently in your array.
    choose index i, such that 0 <= i < n and set the value of arr at index i to x.
    You may repeat this procedure as many times as needed.
    Return true if it is possible to construct the target array from arr, otherwise, return false.
    Constraints:
        n == target.length
        1 <= n <= 5 * 10^4
        1 <= target[i] <= 10^9
    """

    def isPossible(self, target: List[int]) -> bool:
        # special case, causes division by zero if not handled
        if (len(target) == 1):
            return target[0] == 1

        n = len(target)

        # current remaining sum in list
        s = sum(target)

        # maxheap of vals currently in list
        maxheap = [-val for val in target]
        heapq.heapify(maxheap)

        # work backwards, starting from target, while target != [1]*n
        while s > n:
            # get biggest digit from list (info at what index i is not required)
            curr_val = -heapq.heappop(maxheap)

            # sum of all other digits in target
            sum_without_curr = s - curr_val

            # case where len(target) and res == True must be checked (no generalization apparantly)
            if sum_without_curr == 1:
                return True

            # previous value of target[i] before iterations of replacing with sum
            prev_val = curr_val % sum_without_curr

            if prev_val == 0 or prev_val == curr_val:
                return False

            # subtract difference from total sum of target, virtually replacing target[i] with prev_val
            s -= curr_val - prev_val

            # push 'previous' value of target[i] to maxheap
            heapq.heappush(maxheap, -prev_val)

        # if target can be back tracked to [1]*n, return true, else false
        return s == n
