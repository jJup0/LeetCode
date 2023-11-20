"""
You are given a 0-indexed array of strings garbage where garbage[i] represents
the assortment of garbage at the ith house. garbage[i] consists only of the
characters 'M', 'P' and 'G' representing one unit of metal, paper and glass
garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the
number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one
type of garbage. Each garbage truck starts at house 0 and must visit each house
in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is
driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.

Constraints:
- 2 <= garbage.length <= 10^5
- garbage[i] consists of only the letters 'M', 'P', and 'G'.
- 1 <= garbage[i].length <= 10
- travel.length == garbage.length - 1
- 1 <= travel[i] <= 100
"""


class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        """
        n := sum(len(g) for g in garbage)
        m := len(travel)
        O(n + m) / O(m)     time / space complexity
        """
        # find last house for each garbage type
        last_idxs: dict[str, int] = {}
        for garbage_type in "MPG":
            for i in range(len(garbage) - 1, -1, -1):
                if garbage_type in garbage[i]:
                    last_idxs[garbage_type] = i
                    break

        # calculate travel prefix sum
        travel_prefix_sum = [0]
        curr_sum = 0
        for t in travel:
            curr_sum += t
            travel_prefix_sum.append(curr_sum)

        # sum up collection and driving time
        collection_time = sum(len(gs) for gs in garbage)
        driving_time = sum(travel_prefix_sum[last] for last in last_idxs.values())
        return collection_time + driving_time
