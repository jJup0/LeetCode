# from collections import defaultdict
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         charPositions = defaultdict(list)
#         for i, c in enumerate(s):
#             charPositions[c].append(i)
#         chars = sorted(charPositions.keys())
#         retLen = len(chars)

#         def constructStr(prevStr, s_i):
#             if not chars:
#                 return prevStr

#             for i in range(len(chars)):
#                 curChar = chars.pop(0)
#                 # print("cur char:", curChar)
#                 for pos in charPositions[curChar]:
#                     # print("    pos:", pos)
#                     if pos > s_i:
#                         # print('        found new', curChar, pos, ">", s_i)
#                         if (ret:= constructStr(prevStr + curChar, pos)) != None:
#                             # print('ret:', ret)
#                             return ret
#                 chars.append(curChar)

#         return constructStr("",0)


# def removeDuplicateLetters(self, s):
#     for c in sorted(set(s)):
#         suffix = s[s.index(c):]
#         if set(suffix) == set(s):
#             return c + self.removeDuplicateLetters(suffix.replace(c, ''))
#     return ''

class Solution:
    def removeDuplicateLetters(self, s):
        result = ''
        while s:
            i = min(map(s.rindex, set(s)))
            c = min(s[:i+1])
            result += c
            s = s[s.index(c):].replace(c, '')
        return result
