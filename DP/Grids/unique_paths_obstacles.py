from curses.ascii import SO
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # 
        # def find_path(i, j, grid):
        #     if i < 0 or j < 0 or grid[i][j] == 1:
        #         return 0
        #     if (i,j) == (0,0):
        #         return 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     left = find_path(i - 1, j, grid)
        #     right = find_path(i, j - 1, grid)

        #     dp[i][j] = left + right
        #     return dp[i][j]
        
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # dp = [[-1] * n for _ in range(m)]
        # return find_path(m-1, n-1, obstacleGrid)


        # tabular solution
        # T (M * N) | S (M * N) 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]
        #dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                    dp[i][j] = 1
                else:
                    left = 0
                    if i > 0 and obstacleGrid[i][j] != 1:
                        left = dp[i-1][j]
                    up = 0
                    if j > 0 and obstacleGrid[i][j] != 1:
                        up = dp[i][j-1]
                    dp[i][j] = left + up
        return dp[m-1][n-1]




s = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
obstacleGrid = [[1]]
print(s.uniquePathsWithObstacles(obstacleGrid))