"""
Hercy wants to save money for his first car. He puts money in the Leetcode
bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday
to Sunday, he will put in $1 more than the day before. On every subsequent
Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank
at the end of the nth day.

Constraints:
- 1 <= n <= 1000
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        """
        O(1) / O(1)     time / space complexity
        """
        weeks, leftover_days = divmod(n, 7)
        standard_weeks_money = sum(range(1, 8)) * weeks
        full_weeks_bonus_money = 7 * (weeks - 1) * weeks // 2
        last_week_money = sum(range(weeks + 1, weeks + 1 + leftover_days))
        return standard_weeks_money + full_weeks_bonus_money + last_week_money
