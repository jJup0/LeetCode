"""
We have n jobs, where every job is scheduled to be done from startTime[i] to
endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum
profit you can take such that there are no two jobs in the subset with
overlapping time range.

If you choose a job that ends at time X you will be able to start another job
that starts at time X.

Example 2:
"""


import bisect
from functools import cache


class Solution:
    def jobScheduling(
        self, start_times: list[int], end_times: list[int], profits: list[int]
    ):
        return self.jobScheduling2(start_times, end_times, profits)

    def jobScheduling1(
        self, start_times: list[int], end_times: list[int], profits: list[int]
    ) -> int:
        """
        O(n * log(n)) / O(n)   time / space complexity
        """

        @cache
        def max_profit(job_idx: int) -> int:
            """
            O(log(n)) / O(1) time complexity
            """
            nonlocal jobs
            _end, start, profit = jobs[job_idx]
            if job_idx == 0:
                return profit

            ignore_job_profit = max_profit(job_idx - 1)

            prev_compatible_job_idx = bisect.bisect_right(
                jobs, (start, float("inf"), float("inf")), hi=job_idx - 1
            )
            if jobs[prev_compatible_job_idx][0] > start:
                prev_compatible_job_idx -= 1
            if (
                prev_compatible_job_idx <= 0
                and jobs[prev_compatible_job_idx][0] > start
            ):
                return max(ignore_job_profit, profit)
            take_job_profit = profit + max_profit(prev_compatible_job_idx)
            return max(take_job_profit, ignore_job_profit)

        jobs = sorted(zip(start_times, end_times, profits), key=lambda x: x[1])
        return max_profit(len(jobs) - 1)

    def jobScheduling2(
        self, start_times: list[int], end_times: list[int], profits: list[int]
    ) -> int:
        """
        Same time/space complexity but more elegant
        """
        jobs = sorted(zip(start_times, end_times, profits), key=lambda x: x[1])
        sorted_end_times = [end_time for _s, end_time, _p in jobs]

        # max_profits[i] = maximum profits that can be achieved for jobs[:i]
        max_profits = [0]

        for start, _end, profit in jobs:
            # ignore job, take max profit of previous job
            ignore_job_profit = max_profits[-1]

            # schedule current job
            # prev_idx = "index of the latest ending job compatible with the current job" + 1
            # this means that max_profits[i] contains the profits for the previously compatible job
            # if no previous compatible job exists, then prev_job_profit = 0 since max_profits[0] = 0
            prev_idx = bisect.bisect_right(sorted_end_times, start)
            prev_job_profit = max_profits[prev_idx]
            take_job_total_profit = prev_job_profit + profit

            # use the maximum profit between taking and ignoring the job
            max_profits.append(max(ignore_job_profit, take_job_total_profit))

        return max_profits[-1]
