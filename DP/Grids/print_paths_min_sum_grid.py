from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #path = []
        def min_path_sum(i, j, grid):
            if i < 0 or j < 0:
                #path.pop()
                return float("Inf")
            if (i,j) == (0,0):
                return grid[0][0]

            if dp[i][j] != -1:
                return dp[i][j]
            
            left = grid[i][j] + min_path_sum(i - 1, j, grid)

            up = grid[i][j] + min_path_sum(i, j - 1, grid)
            dp[i][j] = min(left, up)
            
            return dp[i][j]

        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        min_path_sum(m-1, n-1, grid)
        return self.get_coordinates(m, n, dp)

    def get_coordinates(self, m, n, dp):

        output = []
        x = m - 1
        y = n - 1
        output.append((x,y))
        path = []
        #print(dp)
        while output:
            i, j = output.pop()
            path.append((i,j))
            if (i,j) == (0,0):
                return path
            temp = float("Inf")
            new_x = -1
            new_y = -1
            if i - 1 >= 0 and dp[i-1][j] < temp:
                temp = dp[i-1][j]
                new_x = i - 1
                new_y = j

            if j - 1 >= 0 and dp[i][j-1] < temp:
                temp = dp[i][j-1]
                new_x = i
                new_y = j - 1
            output.append((new_x, new_y))
        return path
            
            
grid = [[1,3,1],[1,5,1],[4,2,1]]
#grid = [[1,3,1],[1,5,1],[4,2,1]]
s = Solution()
print(s.minPathSum(grid))
