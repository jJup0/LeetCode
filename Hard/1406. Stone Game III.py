from collections import deque


class Solution:
    """
    Alice and Bob continue their games with piles of stones. There are several stones
    arranged in a row, and each stone has an associated value which is an integer given
    in the array stoneValue.

    Alice and Bob take turns, with Alice starting first. On each player's turn, that
    player can take 1, 2, or 3 stones from the first remaining stones in the row.

    The score of each player is the sum of the values of the stones taken. The score
    of each player is 0 initially.

    The objective of the game is to end with the highest score, and the winner is the
    player with the highest score and there could be a tie. The game continues until
    all the stones have been taken.

    Assume Alice and Bob play optimally.

    Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will
    end the game with the same score.

    Constraints:
        1 <= stoneValue.length <= 5 * 10^4
        -1000 <= stoneValue[i] <= 1000
    """

    def stoneGameIII(self, piles: list[int]) -> str:
        def dfs(idx: int) -> int:
            nonlocal n, end_piles_sum, piles
            if idx >= n:
                return 0

            prev_dp = dp[idx]
            if prev_dp != -1:
                return prev_dp

            curr_person_res = -1_000_000_000
            curr_takes_sum = 0
            for takes in range(1, 4):
                new_idx = idx + takes
                if new_idx > n:
                    break
                curr_takes_sum += piles[new_idx - 1]

                other_person_res = dfs(new_idx)

                curr_person_res = max(
                    curr_person_res, end_piles_sum[idx] - other_person_res
                )
            dp[idx] = curr_person_res
            return curr_person_res

        n = len(piles)
        dp = [-1] * n

        end_piles_sum: list[int] = piles.copy()
        for i in range(n - 2, -1, -1):
            end_piles_sum[i] += end_piles_sum[i + 1]

        alice_res = dfs(0)
        bob_res = end_piles_sum[0] - alice_res
        if alice_res > bob_res:
            return "Alice"
        if alice_res < bob_res:
            return "Bob"
        return "Tie"

    def stoneGameIII_O_1_space(self, stone_values: list[int]) -> str:
        n = len(stone_values)

        # dp max value if starting at stone, except only storing the
        # last three indices, as only at most 3 stones can be taken
        dp = deque([0] * 3)

        total_stone_sum = 0
        for i in range(n - 1, -1, -1):
            total_stone_sum += stone_values[i]

            # alice will maximize, by minimizing bob
            new_dp_value = total_stone_sum - min(dp)

            dp.pop()
            dp.appendleft(new_dp_value)

        alice_points = dp[0]
        # bob's maximum points is the difference between
        # the sum of all stones and alice's points
        bob_points = total_stone_sum - alice_points

        if alice_points > bob_points:
            return "Alice"
        elif alice_points < bob_points:
            return "Bob"
        else:
            return "Tie"
