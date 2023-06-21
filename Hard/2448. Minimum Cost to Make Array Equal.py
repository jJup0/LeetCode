class Solution:
    """
    You are given two 0-indexed arrays nums and cost consisting
    each of n positive integers.

    You can do the following operation any number of times:

    Increase or decrease any element of the array nums by 1.
    The cost of doing one operation on the ith element is cost[i].

    Return the minimum total cost such that all the elements
    of the array nums become equal.

    Constraints:
    - n == nums.length == cost.length
    - 1 <= n <= 10^5
    - 1 <= nums[i], cost[i] <= 10^6
    """

    def minCost(self, nums: list[int], costs: list[int]) -> int:
        """
        For each number in nums, calculate cost to bring each other number
        down to at least this number, and up to at least this number.
        Do so by sorting nums first, and accumulating cost so far when iterating through.
        O(n * log(n)) / O(n)    time / space complexity
        """
        nc = sorted(zip(nums, costs))

        # construct bring_all_up_to_val
        accu_cost_per = 0
        prev_num = nc[0][0]
        bring_all_up_to_val = {prev_num: 0}
        for num, cost in nc:
            diff = num - prev_num
            # cost to bring all values up to at least num, is cost to
            # previous, plus difference between num and previous times,
            # the accumulated cost per number
            bring_all_up_to_val[num] = (
                bring_all_up_to_val[prev_num] + accu_cost_per * diff
            )
            accu_cost_per += cost
            prev_num = num

        # everything works analogously for bring_all_down_to_val
        accu_cost_per = 0
        prev_num = nc[-1][0]
        bring_all_down_to_val = {prev_num: 0}
        for num, cost in reversed(nc):
            diff = prev_num - num
            bring_all_down_to_val[num] = (
                bring_all_down_to_val[prev_num] + accu_cost_per * diff
            )
            accu_cost_per += cost
            prev_num = num

        # zip together bring_all_down_to_val and bring_all_up_to_val, and find minimum sum
        return min(
            up_cost + bring_all_down_to_val[val]
            for val, up_cost in bring_all_up_to_val.items()
        )
