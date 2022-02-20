class Solution:
    def findComplement(self, num: int) -> int:
        bitMask = (1<<(len(bin(num))-2)) - 1    # all ones with same bit-length as num
        return num^bitMask