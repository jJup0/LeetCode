"""
You are given an integer array pref of size n. Find and return the array arr of
size n that satisfies:
- pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

Constraints:
- 1 <= pref.length <= 10^5
- 0 <= pref[i] <= 10^6
"""


class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        """Rearrange formula for pref[i] to find arr[i]:
        pref[i] = arr[0] ^ ... ^ arr[i]     <==>
        pref[i] = pref[i-1] ^ arr[i]        <==>
        arr[i] = pref[i-1] ^ pref[i]

        O(n) / O(n)     time / space
        """
        prev_p = 0
        arr: list[int] = []
        for p in pref:
            arr.append(prev_p ^ p)
            prev_p = p
        return arr
