num2let = {'2': 'abc',
           '3': 'def',
           '4': 'ghi',
           '5': 'jkl',
           '6': 'mno',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}


class Solution:
    def letterCombinations(self, digits: str, retThusFar=[], startStr='') -> [str]:
        if digits:
            for char in num2let[digits[0]]:
                curStartStr = startStr + char
                retThusFar = retThusFar + self.letterCombinations(digits[1:], retThusFar, curStartStr)
        elif startStr == '':
            return []
        else:
            return [startStr]
        return list(dict.fromkeys(retThusFar))
