"""
You have planned some train traveling one year in advance. The days of the year
in which you will travel are given as an integer array days. Each day is an
integer from 1 to 365.

Train tickets are sold in three different ways:
- a 1-day pass is sold for costs[0] dollars,
- a 7-day pass is sold for costs[1] dollars, and
- a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.
- For example, if we get a 7-day pass on day 2, then we can travel for 7 days:
  2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given
list of days.

Constraints:
- 1 <= days.length <= 365
- 1 <= days[i] <= 365
- days is in strictly increasing order.
- costs.length == 3
- 1 <= costs[i] <= 1000
"""


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Dynamic programming approach.
        O(n) / O(n)     time / space complexity
        """

        # dp array for memoizing the cheapest
        cheapest_for_day_i = [0] * (len(days) + 1)

        pass_duration_cost = ((1, costs[0]), (7, costs[1]), (30, costs[2]))

        def get_first_travel_day_idx(last_travel_day_idx: int, pass_duration: int):
            """
            Calculates the index of the ealiest possible starting/buy date
            of a pass with the given last travel day index and pass duration.
            O(pass_duration) / O(1)     time / space complexity
            """
            last_travel_day = days[last_travel_day_idx]
            for tday_idx in range(last_travel_day_idx - 1, -1, -1):
                if last_travel_day - days[tday_idx] >= pass_duration:
                    return tday_idx + 1
            return 0

        # iterate over days and use passes in hindsight, cheapest pass is used
        for day_idx in range(len(days)):
            cheapest_for_day_i[day_idx + 1] = min(
                # get dp cost for buying pass that expires on
                # current day and add pass cost
                cheapest_for_day_i[get_first_travel_day_idx(day_idx, pass_duration)]
                + pass_cost
                for pass_duration, pass_cost in pass_duration_cost
            )

        return cheapest_for_day_i[-1]
