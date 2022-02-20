# class Solution:
#     def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
#         corners = sorted((p1, p2, p3, p4))
#         sides = [(corners[1][0]-corners[0][0], corners[1][1]-corners[0][1])]
#         sides.append((corners[3][0]-corners[2][0], corners[3][1]-corners[2][1]))
#         sides.append((corners[2][0]-corners[0][0], corners[2][1]-corners[0][1]))
#         sides.append((corners[3][0]-corners[1][0], corners[3][1]-corners[1][1]))


#         res = sides[0] == sides[1] #and sides[2] == sides[3]

#         # res2 = [0 for x in sides[0] if x < 0] != [0 for x in sides[2] if x < 0]
#         res2 = sides[0] == (sides[2][1], -sides[2][0]) or sides[0] == (-sides[2][1], sides[2][0])
#         res3 = p1 != p3
#         return res and res2 and res3
from collections import Counter


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def getDistance(x1, y1, x2, y2):
            return (x1 - x2)**2 + (y1 - y2)**2

        corners = (p1, p2, p3, p4)
        cnt = Counter(getDistance(*corners[i], *corners[j]) for i in range(4) for j in range(i+1, 4))
        return set(cnt.values()) == {4, 2}  # sides lengths should be counted 4 times, diagonals twice
