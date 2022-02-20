import functools


class Solution:
    def longestDupSubstring(self, S):
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1  # prevents integer overflows but could cause hash collisions

        def findDupeSubstrings(L):
            p = (26**L) % mod
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)  # basically turns A[:L] into an int of base 26 kinda
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod  # idk wtf is going on here
                if cur in seen:
                    return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = findDupeSubstrings(mi)
            if pos:  # if duplicate substring found, move on to longer substrings
                lo = mi
                res = pos
            else:  # if no duplicate substrings found, move on to shorter substrings
                hi = mi - 1
        return S[res:res + lo]
