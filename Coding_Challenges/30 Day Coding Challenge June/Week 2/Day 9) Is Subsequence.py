class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        curSindex = 0
        for tc in t:
            if tc == s[curSindex]:
                curSindex += 1
                if curSindex == len(s):
                    return True
        return False
