from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        p_len = len(p)
        t = Counter(p)
        d = Counter()
        res = []
        for i in range(len(s)):
            if i >= p_len:
                char_to_remove = s[i-p_len]
                d[char_to_remove] -= 1

                if not d[char_to_remove]:
                    del d[char_to_remove]

            char_to_add = s[i]
            d[char_to_add] += 1

            if d == t:
                res.append(i-p_len+1)

        return res