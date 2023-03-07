class Solution:
    """
    You are given an array time where time[i] denotes the time taken by the ith bus to complete
    one trip.

    Each bus can make multiple trips successively; that is, the next trip can start immediately
    after completing the current trip. Also, each bus operates independently; that is, the trips
    of one bus do not influence the trips of any other bus.

    You are also given an integer totalTrips, which denotes the number of trips all buses should
    make in total. Return the minimum time required for all buses to complete at least totalTrips
    trips.

    Constraints:
        1 <= time.length <= 105
        1 <= time[i], totalTrips <= 107
    """

    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        """Binary search for the total amount of time needed
        O(n * log(k))   time / space complexity
        """
        low = 0
        # maximum time possibily needed is time that fastest bus takes to do the job alone
        high = min(time) * totalTrips
        while low < high:
            mid = (low + high) >> 1
            # calculate number of trips made by busses in "mid" time
            trips_made = sum(mid // bus for bus in time)

            # if greater equal set high to mid (not mid - 1, as mid may be the solution)
            if trips_made >= totalTrips:
                high = mid
            else:
                # if strictly less, then at least mid + 1 trips must be made
                low = mid + 1

        return low
