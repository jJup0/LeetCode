class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        prev = [0]*(len(text2)+1)
        for i in range(len(text1)):
            cur = [0]*(len(text2)+1)
            for j in range(len(text2)):
                cur[j+1] = prev[j]+1 if text1[i] == text2[j] else max(prev[j+1], cur[j])
            prev = cur
                    
        return cur[-1]