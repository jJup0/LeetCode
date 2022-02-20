class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        while True:
            l = 0
            for i, c in enumerate(s):
                new = l * int(c) if c.isdigit() else l + 1
                if new >= k:
                    break
                l = new

            if not (k % new and k % l):
                while s[i].isdigit():
                    i -= 1
                return s[i]

            k %= l

        # # less scuffed version
        # buildLen = 0
        # for i, c in enumerate(s):
        #     buildLen = buildLen * int(c) if c.isdigit() else buildLen + 1
        #     if k <= buildLen:
        #         break
        # for j in range(i, -1, -1):
        #     c = s[j]
        #     if c.isdigit():
        #         buildLen /= int(c)
        #         k %= buildLen
        #     else:
        #         if k == buildLen or k == 0:
        #             return c
        #         buildLen -= 1


#         # first version, memory limit
#         l = 0
#         build = ""
#         for i, c in enumerate(s):
#             if c.isnumeric():
#                 val = ord(c) - ord('0')
#                 l *= val
#                 if l >= k:
#                     break
#                 build *= val
#             else:
#                 l += 1
#                 build += c
#                 if l >= k:
#                     break


#         return build[k%len(build) - 1]


# first accepted version lmao
# class Solution:
#     def decodeAtIndex(self, s: str, k: int, deep = 0) -> str:
#         if deep == 10:
#             return
#         l = 0
#         # lengths =[]
#         for i, c in enumerate(s):
#             if c.isnumeric():
#                 val = ord(c) - ord('0')
#                 l *= val
#                 if l >= k:
#                     l /= val
#                     break
#             else:
#                 val = 1
#                 l += 1
#                 if l >= k:
#                     l -=1
#                     break


#         print(k, l)
#         if k%(l + val) == 0:
#             while s[i].isnumeric():
#                 i -= 1
#             return s[i]

#         if k%l > 100:
#             return self.decodeAtIndex(s, int(k%l), deep + 1)

#         print(k%l)
#         build = ""
#         for c in s[:i]:
#             if c.isnumeric():
#                 val = ord(c) - ord('0')
#                 build *= val
#             else:
#                 build += c
#             if len(build) > k:
#                 break
#         # if k - 1 >= len(build):
#         #     print(k, build)
#         # else:
#         return build[k%len(build)- 1]
