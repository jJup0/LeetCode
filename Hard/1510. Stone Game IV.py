from math import isqrt
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # wins[i] stores if game can definitely be won by alice if i rocks at the start of the game
        wins = [False] * (n + 1)
        
        # helper function for recursion, memosation list is non local
        def helper(cur_n: int):
            
            # if no more rocks left, then lost (return false)
            if cur_n == 0:
                return False
            # if this game is provably winnable return true
            if wins[cur_n]:
                return True
            
            # current player can win if next player can not win
            can_win = not all(helper(cur_n - i * i) for i in range(isqrt(cur_n), 0, -1))

            # memoize result
            wins[cur_n] = can_win
            
            return can_win
        
        helper(n)
        return wins[n]
    
        # # boils down to:
        # dp = [False] * (n + 1)
        # for i in range(1, n + 1):
        #     dp[i] = not all(dp[i - k * k] for k in range(isqrt(i), 0, -1))
        # return dp[-1]