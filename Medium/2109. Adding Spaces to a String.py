"""
You are given a 0-indexed string s and a 0-indexed integer array spaces that
describes the indices in the original string where spaces will be added. Each
space should be inserted before the character at the given index.
- For example, given s ="EnjoyYourCoffee" and spaces = [5, 9], we place spaces
  before'Y' and'C', which are at indices 5 and 9 respectively. Thus, we
  obtain"Enjoy Your Coffee".

Returnthe modified string after the spaces have been added.

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consists only of lowercase and uppercase English letters.
- 1 <= spaces.length <= 3 * 10^5
- 0 <= spaces[i] <= s.length - 1
- All the values of spaces are strictly increasing.
"""


class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        spaces_i = 0
        res: list[str] = []
        for i, c in enumerate(s):
            if spaces_i < len(spaces) and spaces[spaces_i] == i:
                res.append(" ")
                spaces_i += 1
            res.append(c)
        return "".join(res)
