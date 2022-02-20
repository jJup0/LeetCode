# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         possA, possB = A[0], B[0]
#         res_a1 = res_a2 = res_b1 = res_b2 = 0
#         n = len(A)

#         for a, b in zip(A, B):
#             if possA not in (a, b):
#                 res_a1 = res_b1 = float('inf')
#             if possB not in (a, b):
#                 res_b2 = res_a2 = float('inf')

#             res_a1 += a != possA
#             res_a2 += a != possB
#             res_b1 += b != possA
#             res_b2 += b != possB

#             if min(res_a1, res_a2, res_b1, res_b2) == float('inf'):
#                 return -1

#         res = min(res_a1, res_a2, res_b1, res_b2)
#         return res if res < n else -1


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        poss = (A[0], B[0])

        for curP in poss:
            A_swap = 0
            B_swap = 0
            for a, b in zip(A, B):
                if a == b == curP:
                    pass
                elif a == curP:
                    B_swap += 1
                elif b == curP:
                    A_swap += 1
                else:
                    break
            else:
                return min(A_swap, B_swap)
        return -1
