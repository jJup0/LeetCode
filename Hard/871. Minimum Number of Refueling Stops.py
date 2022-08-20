import heapq
from typing import List


class Solution:
    """
    A car travels from a starting position to a destination which is target miles east of the
    starting position.
    There are gas stations along the way. The gas stations are represented as an array stations
    where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles
    east of the starting position and has fueli liters of gas.
    The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.
    It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may
    stop and refuel, transferring all the gas from the station into the car.
    Return the minimum number of refueling stops the car must make in order to reach its destination.
    If it cannot reach the destination, return -1.
    Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If
    the car reaches the destination with 0 fuel left, it is still considered to have arrived.
    Constraints:
        1 <= target, startFuel <= 10^9
        0 <= stations.length <= 500
        0 <= positioni <= positioni+1 < target
        1 <= fueli < 10^9
    """

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Drive as far as possible and refuel at best station in hindsight.
        O(n) / O(n)     time / space complexity
        """
        # a max heap to track the stations already passed with the car
        fuel_max_heap = []

        # current position / farthest reachable position with car
        position = startFuel

        # index for iterating over stations/keeping track which stations have already been passed
        fuel_idx = 0

        # result variable
        res = 0

        # while not at target
        while position < target:

            # add all passed fuel stations fuels to the max heap
            while fuel_idx < len(stations) and stations[fuel_idx][0] <= position:
                heapq.heappush(fuel_max_heap, -stations[fuel_idx][1])
                fuel_idx += 1

            # if there are no more fuel stations to refuel from, target can not be reached
            if not fuel_max_heap:
                return -1

            # refuel (in hindsight) at the fuel station with the largest (ununsed) amount of fuel
            position -= heapq.heappop(fuel_max_heap)
            res += 1

        return res
