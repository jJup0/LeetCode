class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        retList = [""] * n
        for i in range(1, n+1):
            curstr = ""
            if i % 3 == 0:
                curstr = "Fizz"
            if i % 5 == 0:
                curstr += "Buzz"
            retList[i-1] = curstr if curstr else str(i)
        return retList
