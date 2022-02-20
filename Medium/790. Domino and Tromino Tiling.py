class Solution:
    def numTilings(self, n: int) -> int:
        if (n <= 2):
            return n
        
        given_mod = 1000000007  # from specification
        
        # ringlist might have been more efficient
        prev2 = 1
        prev1 = 2
        prev = 5
        
        for i in range(n-3):
            next_val = (prev * 2 + prev2) % given_mod
            prev2 = prev1
            prev1 = prev
            prev = next_val 
        return prev
