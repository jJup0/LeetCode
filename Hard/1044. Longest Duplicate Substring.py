import functools


class Solution:
    def longestDupSubstring(self, S):

        def findDupeSubstrings(L):
            # basically turns substring S[:L] into int, basically base 26
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            p = pow(26, L, mod)
            for i in range(L, len(S)):
                # turns substring S[i:L+1] into int, check if already seen
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)

        # turn string into list of ints, 'a'=0, 'z'=25
        A = [ord(c) - ord('a') for c in S]
        # prevents infinite size ints, which would slow down, but could cause hash collisions = false results
        mod = (1 << 63) - 1

        # binary search for length of substring
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) >> 1
            pos = findDupeSubstrings(mi)
            if pos:  # if duplicate substring found, move on to longer substrings
                lo = mi
                res = pos
            else:  # if no duplicate substrings found, move on to shorter substrings
                hi = mi - 1
        return S[res:res + lo]
