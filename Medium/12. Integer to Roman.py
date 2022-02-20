class Solution:
    def intToRoman(self, num: int) -> str:
        i_mxrVal = 6
        r = ''
        dec2rom = [[1, 'I', 0, ''], [5, 'V', 1, 'I'], [10, 'X', 1, 'I'], [50, 'L', 10, 'X'], [
            100, 'C', 10, 'X'], [500, 'D', 100, 'C'], [1000, 'M', 100, 'C']]
        while num > 0:
            curMaxVal = dec2rom[i_mxrVal][0]
            # print(curMaxVal)
            if num >= curMaxVal:
                num -= curMaxVal
                r += dec2rom[i_mxrVal][1]
            elif num >= curMaxVal - dec2rom[i_mxrVal][2]:
                num = num - curMaxVal + dec2rom[i_mxrVal][2]
                r += dec2rom[i_mxrVal][3] + dec2rom[i_mxrVal][1]
            else:
                i_mxrVal -= 1
        return r