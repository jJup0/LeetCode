class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        for i, c in enumerate(s):
            if c.isnumeric():
                return res + int(c) * self.decodeString(s[i+2:])
            elif c == "]":
                return res + self.decodeString(s[i+1:])
            else:
                res += c
        return res


x = Solution()
y = x.decodeString("3[a2[c]]")
y = x.decodeString("3[a]2[bc]"
)
print(y)


# def decodeString(self, s: str) -> str:
#     prev_mults = []
#     prev_strs = []
#     res = temp = ""
#     for c in s:
#         if c == "[":
#             prev_strs.append(temp)
#             continue
#         elif c == "]":
#             temp = temp * prev_mults.pop()
#             if not prev_mults:
#                 res += temp
#             temp = prev_strs.pop()
#         elif c.isnumeric():
#             c = int(c)
#             prev_mults.append(c)
#         else:
#             temp += c
#     return res
