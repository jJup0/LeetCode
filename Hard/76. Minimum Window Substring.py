from collections import Counter


class Solution:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring
    of s such that every character in t (including duplicates) is included in the window. If there
    is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.

    Constraints:
        m == s.length
        n == t.length
        1 <= m, n <= 10^5
        s and t consist of uppercase and lowercase English letters.
    """

    def minWindow(self, s: str, t: str) -> str:
        # remaining characters and their count in t to cover by s substring
        remaining_chars = Counter(t)
        
        # total count of remaining characters in t to cover by s substring
        remaining_count = len(t)
        
        n = len(s)
        
        # left and right index of shortest substring
        best_l = -1
        best_r = n
        
        # left and right index of current subtring
        l = r = 0

        while r < n:
            # shift right index of substring until all characters in t are covered, or end of s is reached
            for r in range(r, n):
                if s[r] in remaining_chars:
                    # if s[r] is a relevant character, decrement remaining_count if the remaining
                    # count needed for s[r] is greater than 0
                    remaining_count -= remaining_chars[s[r]] > 0
                    # decrement characters of s[r] needed
                    remaining_chars[s[r]] -= 1
                    
                    if not remaining_count:
                        break
            
            # avoid using for-else
            if remaining_count != 0:
                break
            
            # increment r, so that s[l:r] contains the full substring
            r += 1  

            # shift left index until a character would be missing
            for l in range(l, r):
                if s[l] in remaining_chars:
                    # increase count needed for s[l]
                    remaining_chars[s[l]] += 1
                    # if greater than zero, then cannot remove s[l] for substring,
                    if remaining_chars[s[l]] > 0:
                        # s[l] to be removed from substring so remaining count back up to 1
                        remaining_count = 1
                        # so check if s[l:r+1] is shortest substring so far covering and update accordingly
                        if (r - l) < (best_r - best_l):
                            best_l = l
                            best_r = r
                        break
            l += 1
                
        return "" if best_l == -1 else s[best_l:best_r]
