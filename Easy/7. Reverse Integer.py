class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tempx = str(x)[::-1]
        if x < 0:
            tempx = '-' + tempx[0:-1]
        tempx = int(tempx)
        if -(2**31) > tempx or tempx > (2**31)-1:
            return 0
        return tempx
