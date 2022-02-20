def firstStrStr(self, haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    i = 0
    while i < len(haystack) - len(needle)+1:
        if ((haystack[i] == needle[0]) and (i + len(needle) <= len(haystack)) and (haystack[i:i+len(needle)] == needle)):
            return i
        i += 1
    return -1


def ownStrStr(self, haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    i = 0
    streak = 0
    checkLen = len(haystack) - len(needle)+1
    while i < checkLen:
        print(i)
        for nChar in needle:
            if haystack[i] != nChar:
                streak = 0
                break
            else:
                streak += 1
        i += 1
        if streak == len(needle):
            return i - streak
    return -1


class Solution:
    def pythonStrStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


x = ownStrStr(0, 'aaaaa', 'bba')
print(x)

# print('sdfig'[2:4 == 'fi'])
