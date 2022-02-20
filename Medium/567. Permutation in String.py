from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str):
        t = Counter(s1)
        d = Counter()
        for i in range(len(s2)):
            if i >= len(s1):
                char_to_remove = s2[i-len(s1)]
                d[char_to_remove] -= 1

                if not d[char_to_remove]:
                    del d[char_to_remove]

            char_to_add = s2[i]
            d[char_to_add] += 1

            if d == t:
                return True

        return False