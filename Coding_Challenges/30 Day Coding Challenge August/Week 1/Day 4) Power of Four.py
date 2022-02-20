class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        num = bin(num)[2:]
        return num.rfind('1') == 0 and num.count('0') % 2 == 0
