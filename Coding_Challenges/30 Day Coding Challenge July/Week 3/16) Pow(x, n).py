class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(x, n)
        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2:  # odd power
            return x * self.myPow(x, n-1)

        sub = self.myPow(x, n//2)  # for even power, take half,
        return sub * sub  # and then return it squared (faster)
