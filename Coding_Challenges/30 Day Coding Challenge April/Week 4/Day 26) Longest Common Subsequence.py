"abcdefgxyopyknd"
"gefoxyloon"


class fugDisSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not(text1) or not(text2):
            return 0
        dp = [[0]*len(text1)]*len(text2)
        print(dp)
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                print(i, j)
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp)
        print(len(text1)-1, len(text2)-1)
        return dp[len(text1)-1][len(text2)-1]

# class recursiveSlowSolution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         def helper(t1, t2,chain, biggest):
#             # print(t1, t2,str(len(chain)), str(biggest))
#             if not(t1) or not(t2):
#                 return len(chain)
#             for i, c in enumerate(t2):
#                 cIdx = t1.find(c)
#                 if cIdx != -1:
#                     # print(chain+c, end=': ')
#                     biggest = max(helper(t1[cIdx+1:], t2[i+1:],chain + c ,biggest), biggest)
#             # print('end of helper')
#             return max(biggest, len(chain))
#         return helper(text1, text2,'',  0)
