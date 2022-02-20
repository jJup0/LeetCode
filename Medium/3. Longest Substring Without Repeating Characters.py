class firstSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1
        curStart = curEnd = 0
        while curEnd < len(s) - 1:
            if s[curStart: curEnd + 1].rfind(s[curEnd + 1]) == -1:
                curEnd += 1
            else:
                if curEnd - curStart + 1 > longest:
                    longest = curEnd - curStart + 1
                if s[curEnd] == s[curEnd + 1]:
                    curStart = curEnd = curEnd + 1
                else:
                    curStart += 1
        if curEnd - curStart + 1 > longest:
            longest = curEnd - curStart + 1
        return longest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastOccurance = {}

        max_length = start = 0

        for i, char in enumerate(s):

            # next letter in question has already occured and current streak started before last occurance -> current occurence ruins streak
            if char in lastOccurance and start <= lastOccurance[char]:
                start = lastOccurance[char] + 1  # start new streak
            else:
                # check if new max streak
                max_length = max(max_length, i - start + 1)

            # set last occurance of character to current i (place in string)
            lastOccurance[char] = i
        return max_length
