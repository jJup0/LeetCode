class Solution:
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])  # flip to front and then back
            A = A[:i:-1] + A[:i]
        return res
    return retList
# def pancakeSort2(A: [int]) -> [int]:
#     len_a = len(A)
#     if A == list(range(1, len_a+1)):
#         return []
#     n = 1
#     atStart = A[0] == 1
#     retList = []
#     while n < len_a:
#         i = A.index(n)
#         while i < len_a-1 and A[i] + 1 == A[i+1]:
#             i += 1
#             n += 1
#         if n == i+1 == len_a:
#             break
#         j = A.index(n+1) if atStart else i + 1
#         retList.append(j)
#         A = A[j-1::-1] + A[j:]
#         n += atStart
#         atStart = not(atStart)
#     if A != list(range(1, len_a+1)):
#         print('not done', A, list(range(1, len_a+1)))
#         return retList + pancakeSort(A)
#     return retList
