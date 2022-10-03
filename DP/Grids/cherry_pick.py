# from sys import flags
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def get_max_sum(i,j, x,y, dp):
            
            if i >= len(grid) or x >= len(grid) or j >= len(grid[0]) or y >= len(grid[0])  or grid[i][j] == -1 or grid[x][y] == -1:
                return -float("inf")
            if (i,j) == (len(grid) -1, len(grid[0]) -1):
                return grid[i][j]

            if (i,j,x,y) in dp:
                return dp[(i,j,x,y)] 
            else:
                cherries = 0
                if (i,j) == (x,y):
                    cherries += grid[i][j]
                else:
                    cherries += grid[i][j] + grid[x][y]

                f1 = get_max_sum(i + 1, j, x + 1, y, dp)
                f2 = get_max_sum(i + 1, j, x, y + 1, dp)

                f3 = get_max_sum(i, j + 1, x + 1, y, dp)
                f4 = get_max_sum(i, j + 1 , x, y  + 1, dp)
                
                dp[(i,j,x,y)] =  cherries + max(f1, f2, f3, f4)
                return dp[(i,j,x,y)]
                

        n = len(grid)
        if n == 1:
            return max(grid[0])
        dp = {}

        ans = get_max_sum(0,0, 0, 0, dp)
        if ans == -float("inf"):
            return 0
        return ans


# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         def get_max_sum(i,j, x,y, dp):
            
#             if i >= len(grid) or x < 0 or j >= len(grid[0]) or y < 0 or grid[i][j] == -1 or grid[x][y] == -1:
#                 return -float("inf")
#             if (i,j) == (len(grid) -1, len(grid) -1):
#                 return grid[i][j]
#             if (x,y) == (0,0):
#                 return grid[x][y]
#             if (i,j) == (len(grid) -1, len(grid) -1) and (x,y) == (0,0):
#                 return grid[i][j] +  grid[x][y]

#             if (i,j,x,y) in dp:
#                 return dp[(i,j,x,y)] 
#             else:
#                 cherries = 0
#                 if (i,j) == (x,y):
#                     cherries += grid[i][j]
#                 else:
#                     cherries += grid[i][j] + grid[x][y]

#                 f1 = get_max_sum(i + 1, j, x - 1, y, dp)
#                 f2 = get_max_sum(i + 1, j, x, y -  1, dp)

#                 f3 = get_max_sum(i, j + 1, x - 1, y, dp)
#                 f4 = get_max_sum(i, j + 1 , x, y  - 1, dp)
                
#                 print(f1, f2, f3, f4)
#                 dp[(i,j,x,y)] =  cherries + max(f1, f2, f3, f4)
#                 return dp[(i,j,x,y)]
                

#         n = len(grid)
#         if n == 1:
#             return max(grid[0])
#         dp = {}

#         ans = get_max_sum(0,0, n - 1, n - 1, dp)
#         if ans == -float("inf"):
#             return 0
#         return ans

# s = Solution()
# grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# #grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# #grid = [[1]]
# print(s.cherryPickup(grid))

