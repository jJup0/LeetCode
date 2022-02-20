class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k > n:
            return -1
        factors = []
        for i in range(1, int(n**0.5 + 1)):
            if not n % i:
                factors.append(i)
                if len(factors) == k:
                    return i

        if n**0.5 % 1 == 0:
            factors.pop()
        if k <= len(factors)*2:
            return n//factors[len(factors)*2-k]
        return -1
