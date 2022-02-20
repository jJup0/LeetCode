class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bitMask = (1<<(len(bin(N))-2)) - 1    # all ones with same bit-length as num
        return N^bitMask