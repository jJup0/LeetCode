class Solution:
    @cache
    def numDecodings(self, s: str) -> int:

        return self.numDecodingsStolen(s)

        if not s:
            return 1
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        ret = self.numDecodings(s[1:])
        if (s[0] <= '1') or (s[0] == '2' and s[1] <= '6'):
            ret += self.numDecodings(s[2:])
        return ret

    def numDecodingsStolen(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(len(s) - 1):
            nextC = s[i+1]
            temp = s[i] + nextC

            if nextC >= '1':        # != '0'
                dp[i+2] += dp[i+1]
            if temp >= "10" and temp <= "26":
                dp[i+2] += dp[i]

        return dp[-1]
