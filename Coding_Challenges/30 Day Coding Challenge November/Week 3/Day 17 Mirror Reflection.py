import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd = math.gcd(p, q)
        p //= gcd
        q //= gcd
        if p % 2 and q % 2:
            return 1
        if not(p % 2) and q % 2:
            return 2
        return 0
