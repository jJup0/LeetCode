class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cx, cy = 0, 0
        dx, dy = 0, 1
        for c in instructions:
            if c == "G":
                cx += dx
                cy += dy
            else:
                sign = 1 if c == "L" else -1
                if dx:
                    dx, dy = 0, dx * sign
                else:
                    dx, dy = -dy*sign, 0

        return (cx == 0 and cy == 0) or dy != 1

# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         dirs = ((0,1), (1,0), (0,-1), (-1,0))      # (x,y) movement
#         diri = 0
#         cx, cy = 0, 0
#         for c in instructions:
#             if c == "G":
#                 cx += dirs[diri][0]
#                 cy += dirs[diri][1]
#             else:
#                 diri += 1 if c == "R" else -1
#                 diri %= 4
#         return (cx == 0 and cy == 0) or diri % 4

# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         cx, cy = 0, 0
#         dx, dy = 0, 1
#         for c in instructions:
#             if c == "G":
#                 cx += dx
#                 cy += dy
#             elif c == "L":
#                 if dx:
#                     dx, dy = 0, dx
#                 else:
#                     dx, dy = -dy, 0
#             else:
#                 if dx:
#                     dx, dy = 0, -dx
#                 else:
#                     dx, dy = dy, 0

#         return (cx == 0 and cy == 0) or dy !=1
