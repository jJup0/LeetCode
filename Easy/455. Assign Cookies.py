"""
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie
that the child will be content with; and each cookie j has a size s[j]. If s[j]
>= g[i], we can assign the cookie j to the child i, and the child i will be
content. Your goal is to maximize the number of your content children and
output the maximum number.

Constraints:
- 1 <= g.length <= 3 * 10^4
- 0 <= s.length <= 3 * 10^4
- 1 <= g[i], s[j] <= 2^31 - 1
"""


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """
        O(n * log(n) + m *log(m)) / O(1)    time / space complexity
        """
        g.sort()
        s.sort()
        res = 0
        s_i = 0
        for greed in g:
            while s_i < len(s) and greed > s[s_i]:
                s_i += 1
            if s_i < len(s):
                res += 1
                s_i += 1
            else:
                break
        return res
