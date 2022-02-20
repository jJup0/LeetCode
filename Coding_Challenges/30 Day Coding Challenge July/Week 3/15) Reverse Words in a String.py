class Solution:
    def reverseWords(self, s: str) -> str:
        s += ' '
        curWord = ''
        retStr = ''
        for c in s:
            if c != ' ':
                curWord += c
            elif curWord:
                retStr = ' ' + curWord + retStr
                curWord = ''
        return retStr[1:]
