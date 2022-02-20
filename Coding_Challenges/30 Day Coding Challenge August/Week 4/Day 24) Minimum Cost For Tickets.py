class Solution:
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        n = len(days)
        if costs[0] > costs[1]:
            costs[0] = costs[1]
        dp = [0, costs[0]] + [0]*(n - 1)
        for i in range(1, n):
            dp[i+1] = dp[i]+costs[0]  # buy one-day ticket

            # what about buy 7-day ticket 7 days ago or 30-day ticket 30 days ago
            j = i
            for dpast, cost in ((7, costs[1]), (30, costs[2])):
                while j >= 0 and days[j] > days[i]-dpast:  # find day which was max 7 days ago
                    j -= 1
                dp[i+1] = min(dp[i+1], dp[j+1]+cost)

        return dp[-1]
