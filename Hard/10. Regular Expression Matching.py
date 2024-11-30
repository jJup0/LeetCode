"""
Given an input string s and a pattern p, implement regular expression matching
with support for'.' and'*' where:
-'.' Matches any single character.
-'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters,'.', and'*'.
- It is guaranteed for each appearance of the character'*', there will be a
  previous valid character to match.
"""

from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.is_match_iterative(s, p)

    def is_match_iterative(self, s: str, p: str) -> bool:
        """
        Complexity:
            Time: O(n * m)
            Space: O(n * m)
        """
        # stack of index in s and index in p which have already matched
        stack: list[tuple[int, int]] = [(0, 0)]
        # visited indexes of s and p
        visited: set[tuple[int, int]] = set()
        while stack:
            si, pi = stack.pop()
            if (si, pi) in visited:
                continue
            visited.add((si, pi))

            if si == len(s):
                if pi == len(p):
                    return True
                if pi < len(p) - 1 and p[pi + 1] == "*":
                    stack.append((si, pi + 2))
            elif pi >= len(p):
                pass
            elif pi < len(p) - 1 and p[pi + 1] == "*":
                # use wildcard to skip letter
                stack.append((si, pi + 2))
                if s[si] == p[pi] or p[pi] == ".":
                    # match letter and keep wildcard
                    stack.append((si + 1, pi))
            elif s[si] == p[pi] or p[pi] == ".":
                stack.append((si + 1, pi + 1))
            # else, cannot match
        return False

    @cache
    def is_match_recursive_unoptimized(self, s: str, p: str) -> bool:
        """
        Complexity:
            Time: O(n * m * (n + m))
            Space: O(n * m * (n + m))
        """
        if not s:
            if not p:
                # both are empty -> match
                return True
            if len(p) > 1 and p[1] == "*":
                # use star to skip letter
                return self.is_match_recursive_unoptimized(s, p[2:])
            # p is non empty, no match
            return False
        if not p:
            # s is empty, p is not, no match
            return False
        if len(p) > 1 and p[1] == "*":
            # skip letter in p
            if self.is_match_recursive_unoptimized(s, p[2:]):
                return True

            if s[0] == p[0] or p[0] == ".":
                # try to match letter in p
                if self.is_match_recursive_unoptimized(s[1:], p):
                    return True
            return False

        if s[0] == p[0] or p[0] == ".":
            return self.is_match_recursive_unoptimized(s[1:], p[1:])

        # no match for first letter
        return False
