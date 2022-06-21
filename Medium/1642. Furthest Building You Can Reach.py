import heapq
from typing import List


class Solution:
    """
    You are given an integer array heights representing the heights of buildings, some bricks, and
    some ladders.
    You start your journey from building 0 and move to the next building by possibly using bricks
    or ladders.
    While moving from building i to building i+1 (0-indexed),
        If the current building's height is greater than or equal to the next building's height,
        you do not need a ladder or bricks.
        If the current building's height is less than the next building's height, you can either
        use one ladder or (h[i+1] - h[i]) bricks.
    Return the furthest building index (0-indexed) you can reach if you use the given ladders and
    bricks optimally.
    Constraints:
        1 <= heights.length <= 10^5
        1 <= heights[i] <= 10^6
        0 <= bricks <= 10^9
        0 <= ladders <= heights.length
    """

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Greedily use bricks for all ascends, and replace largest previous ascend "in hindsight"
        with a ladder when bricks run out. Worst case: bricks=0, ladders=n, each building higher
        than the next: results in heappush and pop at every iteration.
        # O(n * log(n)) time, O(n) space
        """
        # maintain a max heap of all previous ascends
        ascends = []

        # height of previous building
        prev_height = heights[0]

        for i, height in enumerate(heights):
            # if current building is higher than previous, need to use bricks
            if height > prev_height:
                # calculate bricks needed
                diff = height - prev_height

                # greedily always use bricks when there are some remaining
                bricks -= diff

                # push the amount of bricks used to the max heap
                # (python3.10 only offers minheap built in, so push (and pop) -diff)
                heapq.heappush(ascends, -diff)

                # if more bricks were uses than availible
                if bricks < 0:
                    # if ladders are remaining, "replace" previous biggest brick usage by one ladder
                    if ladders:
                        # add bricks used back to brick count
                        bricks -= heapq.heappop(ascends)
                        # "use" up one ladder
                        ladders -= 1
                    else:
                        # if there are no ladders remaining, furthest index reachable is prev
                        return i - 1

            prev_height = height

        # if not returned in for loop, then last building can be reached
        return len(heights) - 1
