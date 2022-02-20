class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 4:  # 4 is always reached for numbers with infinite loops
            newN = 0
            while n != 0:
                n, newNadd = divmod(n, 10)
                newN += newNadd**2
            if newN == 1:
                return True
            n = newN
        return False


def isHappy(self, n: int) -> bool:
    loops = 0
    while loops < 50:  # 4 is always reached for numbers with infinite loops
        print(n)
        newN = 0
        while n != 0:
            n, newNadd = divmod(n, 10)
            newN += newNadd**2
        if newN == 1:
            return True
        n = newN
        loops += 1
    return False


isHappy(0, 340875349)
