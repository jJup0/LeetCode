class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1 "
        for i in range(1, n):
            newStr = ""
            j = 0
            count = 1
            while j < len(res)-1:
                if res[j] == res[j+1]:
                    count += 1
                else:
                    newStr += str(count) + str(res[j])
                    count = 1
                j += 1
            if count > 1:
                newStr += str(count) + str(res[j])
            res = newStr + " "
        return res[:-1]
