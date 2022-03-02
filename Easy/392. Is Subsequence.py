class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        cur_s_idx = 0
        for tc in t:
            if tc == s[cur_s_idx]:
                cur_s_idx += 1
                if cur_s_idx == len(s):
                    return True
        return False