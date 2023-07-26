import math


class Solution:
    """
    You are given a floating-point number hour, representing the amount of time you have
    to reach the office. To commute to the office, you must take n trains in sequential
    order. You are also given an integer array dist of length n, where dist[i] describes
    the distance (in kilometers) of the ith train ride.

    Each train can only depart at an integer hour, so you may need to wait in between
    each train ride.
    - For example, if the 1st train ride takes 1.5 hours, you must wait for an additional
    0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.

    Return the minimum positive integer speed (in kilometers per hour) that all the
    trains must travel at for you to reach the office on time, or -1 if it is impossible
    to be on time.

    Tests are generated such that the answer will not exceed 10^7 and hour will have at
    most two digits after the decimal point.

    Constraints:
    - n == dist.length
    - 1 <= n <= 10^5
    - 1 <= dist[i] <= 10^5
    - 1 <= hour <= 10^9
    - There will be at most two digits after the decimal point in hour.
    """

    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        """
        Binary seach for speed needed.
        O(n * log(n)) / O(1)    time / space complexity
        """
        # need at least one hour per station, except for last station
        if len(dist) > math.ceil(hour):
            return -1

        # train needs to travel at least 1 kph, but also at least the total distance divided by the time allowed
        lo = max(1, sum(dist) // math.ceil(hour))
        # worst case scenario, every station has distance 1 except the last station
        # dist[-1] in worst case scenario == (sum(dist) - (len(dist) - 1)
        # time left for dist[-1] in worst case scenario == (hour - (len(dist) - 1))
        hi = math.ceil((sum(dist) - (len(dist) - 1)) / (hour - (len(dist) - 1)))

        # binary search
        while lo < hi:
            mid = (lo + hi) >> 1
            # time taken is sum of time taken for each station rounded up,
            # except for the last station
            time_taken = (
                sum(math.ceil(dist[i] / mid) for i in range(len(dist) - 1))
                + dist[-1] / mid
            )
            if time_taken > hour:
                lo = mid + 1
            else:
                hi = mid
        return lo
