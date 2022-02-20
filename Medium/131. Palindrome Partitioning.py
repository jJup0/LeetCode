from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for i in range(n)]    #dp[i,j] = str[i,j] is palindrome 
        res = [[] for i in range(n)]            #perms up until each char
        for i in range(n):
            for j in range(i+1):
                # if two chars are equal, and they are next to each other or text between them is a palindrom or 
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True     #s[i:j] is palindrome
                    substr = s[j:i+1]   #make copy of current palimdrome substring
                    prevs = res[j-1] if j > 0 else [[]]   #store "previous" combinations in temp variable 
                    res[i].extend(l + [substr] for l in prevs)      #create all new possibles for i
        return res[-1]   