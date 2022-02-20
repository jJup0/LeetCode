from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        t = Counter(p)
        d = Counter()
        res = []
        for i in range(len(s)):
            if i >= len(p):
                char_to_remove = s[i-len(p)]
                d[char_to_remove] -= 1

                if not d[char_to_remove]:
                    del d[char_to_remove]

            char_to_add = s[i]
            d[char_to_add] += 1

            if d == t:
                res.append(i-len(p)+1)

        return res
