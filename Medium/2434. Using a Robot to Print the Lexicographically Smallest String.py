"""
You are given a string s and a robot that currently holds an empty string t.
Apply one of the following operations until s and t are both empty:
- Remove the first character of a string s and give it to the robot. The robot
  will append this character to the string t.
- Remove the last character of a string t and give it to the robot. The robot
  will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only English lowercase letters.
"""


class Solution:
    def robotWithString(self, s: str) -> str:
        """
        Create an array `smallest_to_end` where smallest_to_end[i] = min(s[i:]).
        Keep a char array `t` as described in the problem.
        Iterate through i, 0 <= i < len(s). While `t` is not empty and
        t[-1] < smallest_to_end[i] the pop from t and append to result. If
        s[i] == smallest_to_end[i] then append to result. This way at each step
        we append the smallest possible character that is still available to us.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        smallest_to_end = self._calc_smallest_to_end(s)
        return self._construct_smallest_string(s, smallest_to_end)

    def _construct_smallest_string(self, s: str, smallest_to_end: list[str]):
        t: list[str] = []
        res: list[str] = []

        for c, smallest in zip(s, smallest_to_end):
            while t and t[-1] <= smallest:
                res.append(t.pop())
            if c == smallest:
                res.append(smallest)
            else:
                t.append(c)
        res.extend(reversed(t))
        return "".join(res)

    def _calc_smallest_to_end(self, s: str):
        smallest_to_end: list[str] = []
        smallest_char = "\u9999"
        for c in reversed(s):
            if c < smallest_char:
                smallest_char = c
            smallest_to_end.append(smallest_char)
        smallest_to_end.reverse()
        return smallest_to_end


def test():
    sol = Solution()
    res = sol.robotWithString("zza")
    assert res == "azz"


test()
