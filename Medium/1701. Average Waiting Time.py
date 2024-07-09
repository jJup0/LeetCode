"""
There is a restaurant with a single chef. You are given an array customers,
where customers[i] = [arrival_i, time_i]:
- arrival_i is the arrival time of the ith customer. The arrival times are
  sorted in non-decreasing order.
- time_i is the time needed to prepare the order of the ith customer.

When a customer arrives, he gives the chef his order, and the chef starts
preparing it once he is idle. The customer waits till the chef finishes
preparing his order. The chef does not prepare food for more than one customer
at a time. The chef prepares food for customers in the order they were given in
the input.

Return the average waiting time of all customers. Solutions within 10-5 from
the actual answer are considered accepted.

Constraints:
- 1 <= customers.length <= 10^5
- 1 <= arrival_i, time_i <= 10^4
- arrival_i <= arrival_i+1
"""


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        """
        O(n) / O(1)     time / space complexity
        """
        total_wait_time = 0
        next_ready_timestamp = 0
        for arrival, cook_time in customers:
            cook_ready_timestamp = max(next_ready_timestamp, arrival)
            wait_time = (cook_ready_timestamp - arrival) + cook_time
            total_wait_time += wait_time
            next_ready_timestamp = arrival + wait_time
        return total_wait_time / len(customers)
