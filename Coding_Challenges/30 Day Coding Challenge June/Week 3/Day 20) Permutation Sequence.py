import math


class idkmanSolution:
    def getPermutation(self, n: int, k: int) -> str:
        curf = 1
        retVal, remainingDigits, factorials = '', [], []
        for i in range(1, n + 1):
            curf *= i
            factorials.append(curf)
            remainingDigits.append(str(i))
        print(remainingDigits)
        while remainingDigits:
            print('k:', k, end=' | ')
            try:
                curD = k*n//curf
            except:
                print('fac:', curf, end=' | ')
            print('curd:', curD, end=' | ')
            curD = max(min(len(remainingDigits)-1, curD), 0)
            print('curd:', curD, end=' | ')
            retVal += remainingDigits.pop(curD)
            # factorial //= int(retVal[-1])
            k %= factorials[int(retVal[-1])-1]
            print(remainingDigits)
        print([s for s in retVal])
        return retVal


class Solution(object):
    def getPermutation(self, n, k):
        # precompute factorial
        factorials = [math.factorial(i) for i in range(n)]  # fast enough for  1 < n < 9
        remainingNums = [str(i) for i in range(1, n + 1)]
        retVal = ''
        curr = n - 1
        k -= 1
        while(curr >= 0):
            ind = k // factorials[curr]
            retVal += remainingNums.pop(ind)
            k %= factorials[curr]
            curr -= 1
        return retVal
