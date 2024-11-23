"""
You are given an integer array nums of length n and a 2D array queries where
queries[i] = [l_i, r_i].

Each queries[i] represents the following action on nums:
- Decrement the value at each index in the range [l_i, r_i] in nums by at most1.
- The amount by which the value is decremented can be chosen independently for
  each index.

A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such
that nums can still be converted to a zero array using the remaining queries.
If it is not possible to convert nums to a zero array, return -1.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 0 <= l_i <= r_i < nums.length
"""

import heapq


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Greedily use queries that have the highest upper end that still include the lowest index which has not been decreased to 0.
        """
        # sort queries by lower bound
        queries.sort()
        queries_i = 0

        # max heap of upper boundaries of unused queries
        unused_queries_heap: list[int] = []
        # min heap of upper boundaries of currently "active" queries
        active_queries_heap: list[int] = []
        used_queries_count = 0

        for i, num in enumerate(nums):
            # remove all queries where the upper bound is lower than the current index
            while active_queries_heap and active_queries_heap[0] < i:
                heapq.heappop(active_queries_heap)

            # skip all queries which end before the current index
            while queries_i < len(queries) and queries[queries_i][1] < i:
                queries_i += 1

            # add the upper bounds of all queries which include the current index in the max heap
            while queries_i < len(queries) and queries[queries_i][0] <= i:
                heapq.heappush(unused_queries_heap, (-queries[queries_i][1]))
                queries_i += 1

            # all quries in `active_queries_heap` can be used to decrement current index
            num -= len(active_queries_heap)
            if num <= 0:
                continue

            # `num` queries still need to be used
            used_queries_count += num
            for _ in range(num):
                if not unused_queries_heap:
                    # no unused queries which include the current index  remaining
                    return -1

                upper_boundary = -heapq.heappop(unused_queries_heap)
                if upper_boundary < i:
                    # largest unused upper boundary is lower than current index,
                    # can not decrement current index to 0
                    return -1

                # move query to active queries
                heapq.heappush(active_queries_heap, upper_boundary)

        return len(queries) - used_queries_count
