class Solution:
    def stringShift(self, s: str, shift: [[int]]) -> str:
        totalShift = 0
        for shf in shift:
            totalShift += ((shf[0] and 1) or -1) * shf[1]
            # if shf[0]:
            #     totalShift += shf[1]
            # else:
            #     totalShift -= shf[1]
        totalShift %= len(s)
        return s[-totalShift:] + s[:-totalShift]
