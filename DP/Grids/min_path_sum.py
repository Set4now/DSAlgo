from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        path = []
        def find_path(i, j, grid):
            if i < 0 or j < 0:
                #path.pop()
                return float("Inf")
            if (i,j) == (0,0):
                return grid[0][0]

            if dp[i][j] != -1:
                return dp[i][j]
            
            left = grid[i][j] + find_path(i - 1, j, grid)

            up = grid[i][j] + find_path(i, j - 1, grid)
            dp[i][j] = min(left, up)
            
            return dp[i][j]

        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        return find_path(m-1, n-1, grid)

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1] * n for _ in range(m) ]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             dp[i][j] = grid[0][0] 
        #         else:
        #             up = float("inf")
        #             if i > 0:
        #                 up = grid[i][j] + dp[i-1][j]
        #             left = float("Inf")
        #             if j > 0:
        #                 left = grid[i][j] + dp[i][j-1]
        #             dp[i][j] = min(up, left)
        # return dp[m-1][n-1]
                    

grid = [[1,3,1],[1,5,1],[4,2,1]]
s = Solution()
print(s.minPathSum(grid))