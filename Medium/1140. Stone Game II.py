class Solution:
    """
    Alice and Bob continue their games with piles of stones.  There are a number of
    piles arranged in a row, and each pile has a positive integer number of stones
    piles[i].  The objective of the game is to end with the most stones.

    Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

    On each player's turn, that player can take all the stones in the first X remaining
    piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

    Constraints:
        1 <= piles.length <= 100
        1 <= piles[i] <= 10^4
    """

    def stoneGameII(self, piles: list[int]) -> int:
        def dfs(m: int, idx: int) -> int:
            nonlocal n, end_piles_sum, piles

            if n - idx <= m * 2:
                return end_piles_sum[idx]

            prev_dp = dp[m][idx]
            if prev_dp != -1:
                return prev_dp

            curr_person_res = 0
            curr_takes_sum = 0
            new_m = m
            for takes in range(1, 2 * m + 1):
                new_idx = idx + takes
                if new_idx >= n:
                    break
                new_m = max(new_m, takes)
                curr_takes_sum += piles[new_idx - 1]

                other_person_res = dfs(new_m, new_idx)

                curr_person_res = max(
                    curr_person_res,
                    curr_takes_sum + end_piles_sum[new_idx] - other_person_res,
                )

            dp[m][idx] = curr_person_res
            return curr_person_res

        n = len(piles)
        dp = [[-1] * n for _ in range(n)]

        end_piles_sum: list[int] = piles.copy()
        for i in range(n - 2, -1, -1):
            end_piles_sum[i] += end_piles_sum[i + 1]

        return dfs(1, 0)
