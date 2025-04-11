"""
A city's skyline is the outer contour of the silhouette formed by all the
buildings in that city when viewed from a distance. Given the locations and
heights of all the buildings, return the skyline formed by these buildings
collectively.

The geometric information of each building is given in the array buildings
where buildings[i] = [left_i, right_i, height_i]:
- left_i is the x coordinate of the left edge of the ith building.
- right_i is the x coordinate of the right edge of the ith building.
- height_i is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely
flat surface at height 0.

The skyline should be represented as a list of"key points" sorted by their
x-coordinate in the form [[x_1,y_1],[x_2,y_2],...]. Each key point is the left
endpoint of some horizontal segment in the skyline except the last point in the
list, which always has a y-coordinate 0 and is used to mark the skyline's
termination where the rightmost building ends. Any ground between the leftmost
and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the
output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not
acceptable; the three lines of height 5 should be merged into one in the final
output as such: [...,[2 3],[4 5],[12 7],...]

Constraints:
- 1 <= buildings.length <= 10^4
- 0 <= left_i < right_i <= 2^31 - 1
- 1 <= height_i <= 2^31 - 1
- buildings is sorted by left_i in non-decreasing order.
"""

import heapq

from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        # result variable
        key_points: list[list[int]] = []
        # sort buildings by start coordinate, the rest does not matter
        buildings.sort(key=lambda b: b[0])
        end_of_last_building = max(building[1] for building in buildings)
        # buildings that are part of current silhouette
        active_buildings_heap = [(end_of_last_building + 1, 0)]
        # sorted list of heights of buildings in current silhouette
        curr_heights = SortedList([0])
        for b_start, b_end, b_height in buildings:
            self._process_past_buildings(
                key_points, active_buildings_heap, curr_heights, b_start
            )
            if b_height > curr_heights[-1]:
                # new highest building in silhouette, add to keypoints
                key_points.append([b_start, b_height])
            # add building to
            curr_heights.add(b_height)
            heapq.heappush(active_buildings_heap, (b_end, b_height))

        self._process_past_buildings(
            key_points, active_buildings_heap, curr_heights, end_of_last_building + 1
        )
        return self._clean_up_key_points(key_points)

    def _process_past_buildings(
        self,
        key_points: list[list[int]],
        heap: list[tuple[int, int]],
        curr_heights: SortedList[int],
        until_x_coordinate: int,
    ) -> None:
        """
        Removes buildings from the heap that have ended before `until_x_coordinate`,
        updating the skyline if the tallest building ends.

        Args:
            key_points (list[list[int]]): Accumulates critical points of the skyline.
            heap (list[tuple[int, int]]): Min-heap of (end_x, height) for active buildings.
            curr_heights (SortedList[int]): Sorted list of current active building heights.
            until_x_coordinate (int): x-coordinate threshold up to which buildings are removed.
        """
        while heap[0][0] < until_x_coordinate:
            prev_end, prev_height = heapq.heappop(heap)
            if prev_height == curr_heights[-1]:
                # tallest building in silhouette ends, add to key points
                curr_heights.pop()
                key_points.append([prev_end, curr_heights[-1]])
            else:
                curr_heights.remove(prev_height)

    def _clean_up_key_points(self, key_points: list[list[int]]):
        """Remove neighboring keypoints with same x or y value."""
        key_points_result: list[list[int]] = []
        for x, y in key_points:
            if key_points_result and key_points_result[-1][0] == x:
                key_points_result[-1][1] = max(key_points_result[-1][1], y)
            elif not key_points_result or key_points_result[-1][1] != y:
                key_points_result.append([x, y])
        return key_points_result


def test():
    s = Solution()
    res = s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    assert res == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]], res

    res = s.getSkyline([[0, 2, 3], [2, 5, 3]])
    assert res == [[0, 3], [5, 0]], res

    res = s.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
    assert res == [[1, 3], [2, 0]], res

    res = s.getSkyline([[1, 5, 3], [1, 5, 3], [1, 5, 3]])
    assert res == [[1, 3], [5, 0]], res

    # fmt: off
    res = s.getSkyline([[1,38,219],[2,19,228],[2,64,106],[3,80,65],[3,84,8],[4,12,8],[4,25,14],[4,46,225],[4,67,187],[5,36,118],[5,48,211],[5,55,97],[6,42,92],[6,56,188],[7,37,42],[7,49,78],[7,84,163],[8,44,212],[9,42,125],[9,85,200],[9,100,74],[10,13,58],[11,30,179],[12,32,215],[12,33,161],[12,61,198],[13,38,48],[13,65,222],[14,22,1],[15,70,222],[16,19,196],[16,24,142],[16,25,176],[16,57,114],[18,45,1],[19,79,149],[20,33,53],[21,29,41],[23,77,43],[24,41,75],[24,94,20],[27,63,2],[31,69,58],[31,88,123],[31,88,146],[33,61,27],[35,62,190],[35,81,116],[37,97,81],[38,78,99],[39,51,125],[39,98,144],[40,95,4],[45,89,229],[47,49,10],[47,99,152],[48,67,69],[48,72,1],[49,73,204],[49,77,117],[50,61,174],[50,76,147],[52,64,4],[52,89,84],[54,70,201],[57,76,47],[58,61,215],[58,98,57],[61,95,190],[66,71,34],[66,99,53],[67,74,9],[68,97,175],[70,88,131],[74,77,155],[74,99,145],[76,88,26],[82,87,40],[83,84,132],[88,99,99]])
    assert res == [[1,219],[2,228],[19,225],[45,229],[89,190],[95,175],[97,152],[99,74],[100,0]], res
    # fmt: on


test()
