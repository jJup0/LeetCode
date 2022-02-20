class Solution:
    def reverseBits(self, n: int) -> int:
        zeroes = '0'*(34 - len(bin(n)))  # bin includes extra 0b
        return int(bin(n)[:1:-1] + zeroes, 2)
