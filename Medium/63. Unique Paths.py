class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        factorials = [1 for _ in range(m+n)]
        for i in range(1, len(factorials)):
            factorials[i] = factorials[i-1] * i
        return int(factorials[m+n-2]/(factorials[m-1]*factorials[n-1]))

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid):

#         if not obstacleGrid or obstacleGrid[0][0]:
#             return 0
#         m, n = len(obstacleGrid), len(obstacleGrid[0])

#         # fill grid with unique nr of ways to get to each position
#         obstacleGrid[0][0] = 1
#         # initialize first col
#         for i in range(1, m):
#             obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
#         # initialize first row
#         for j in range(1, n):
#             obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1 - obstacleGrid[0][j])
#         # fill in gaps from initalized rows
#         for i in range(1, m):
#             for j in range(1, n):
#                 obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])

#         return obstacleGrid[-1][-1]

# # doesnt actully want unique paths i guess. adjusted my code from unique paths III and it
# # finds more unique paths than result, idk man
# #     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

# #         def inBounds(i, j):
# #             return (0 <= i < len(obstacleGrid)) & (0 <= j < len(obstacleGrid[0]))

# #         # returns ways to reach goal
# #         def bfs(i, j):
# #             val = obstacleGrid[i][j]
# #             # cant go through obstacle
# #             if val == 1:
# #                 return 0
# #             # if reached the end, return if all squares were passed
# #             if i == goalI and j == goalJ:
# #                 print(obstacleGrid)
# #                 return 1
# #             # mark square as visited, by turning into obstacle
# #             obstacleGrid[i][j] = 1
# #             ret = 0
# #             # visit adjacents
# #             for di, dj in ((0,1), (0,-1), (1, 0), (-1,0)):
# #                 ni = i + di
# #                 nj = j + dj
# #                 if inBounds(ni, nj):
# #                     ret += bfs(ni, nj)
# #             # mark square as unvisited again
# #             obstacleGrid[i][j] = 0
# #             return ret

# #         goalI, goalJ = len(obstacleGrid)-1, len(obstacleGrid[0])-1
# #         return bfs(0,0)
