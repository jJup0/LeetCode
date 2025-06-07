"""
You are given a string s. It may contain any number of'*' characters. Your task
is to remove all'*' characters.

While there is a'*', do the following operation:
- Delete the leftmost'*' and the smallest non-'*' character to its left. If
  there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all'*'
characters.

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters and'*'.
- The input is generated such that it is possible to delete all'*' characters.
"""

import heapq
import string


class Solution:
    def clearStars(self, s: str) -> str:
        """
        Keep min-heap of unique undeleted letters and dict of indexes of undeleted letters.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        occurances: dict[str, list[int]] = {char: [] for char in string.ascii_lowercase}
        undeleted_letters_min_heap: list[str] = []
        # char array result variable
        res = list(s)
        for i, c in enumerate(s):
            if c == "*":
                smallest = undeleted_letters_min_heap[0]
                # delete last occurance of smallest letter to guarantee
                # smallest lexicographical string
                idx_to_remove = occurances[smallest].pop()
                res[idx_to_remove] = ""
                if not occurances[smallest]:
                    # remove letter from heap if it is no longer in result
                    heapq.heappop(undeleted_letters_min_heap)
                # remove * from result
                res[i] = ""
            else:
                if not occurances[c]:
                    heapq.heappush(undeleted_letters_min_heap, c)
                occurances[c].append(i)
        return "".join(res)
