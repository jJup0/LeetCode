class Solution:
    def maxPower(self, s: str) -> int:
        prevC = ''
        maxStreak = streak = 0
        for c in s:
            if c == prevC:
                streak += 1
            else:
                maxStreak = max(maxStreak, streak)
                prevC = c
                streak = 1
        
        return max(maxStreak, streak)