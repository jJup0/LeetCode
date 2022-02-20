class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if n >= (m << 1):
            return 0
        ret = m
        for x in range(m+1, n+1):
            ret &= x
            if not ret:
                return 0
        return ret
