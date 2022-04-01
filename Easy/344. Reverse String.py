from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s.reverse() in long form:
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = temp
