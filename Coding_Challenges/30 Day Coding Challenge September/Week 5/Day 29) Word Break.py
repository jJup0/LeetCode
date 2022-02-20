class Solution:
    def wordBreak(self, s, words):
        idx_constructable = [True] * (len(s)+1)
        max_len = max(map(len, words+['']))
        words = set(words)
        for i in range(1, len(s)+1):
            # if s[:j] constructable and s[j:i] in words then s[:i] constructable
            idx_constructable[i] = any(idx_constructable[j] and s[j:i] in words for j in range(max(0, i-max_len), i))
        return idx_constructable[-1]
