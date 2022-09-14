"""
1254. Number of Closed Islands
Medium

2301

53

Add to List

Share
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

"""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        visited = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i in [0, len(grid) - 1] or j in [0, len(grid[0]) - 1]:
                    if grid[i][j] == 0:
                        self.bfs_nc(i, j, grid, visited)
        count = 0    
        visited = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                 if i not in [0, len(grid) - 1] or j not in [0, len(grid[0]) - 1]:
                    if grid[i][j] == 0:
                        self.dfs(i, j, grid, visited)
                        # Number of total closed island
                        count += 1
                    
        return count
    
    
    
    def dfs(self, x, y, grid, visited):
        "All the remaing island (0) must be part of a totally closed island"
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 0:
            return 
        
        grid[x][y] = "L"
        visited.append((x,y))
        if (x+1,y) not in visited:
            self.dfs(x+1,y,grid,visited)
        if (x-1,y) not in visited:
            self.dfs(x-1,y,grid,visited)
        
        
        if (x,y + 1) not in visited:
            self.dfs(x,y+1,grid,visited)
        if (x,y - 1) not in visited:
            self.dfs(x,y-1,grid,visited)
        
        
        
    
    def bfs_nc(self, x, y, grid, visited):
        """Marking Not closed islands
           The idea is any island (Cell of value 0) touching a boundary cell having 0 cannot be a part of a total closed island
            
        """
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 0:
            return 
        
        grid[x][y] = "NC"
        visited.append((x,y))
        
        if (x+1,y) not in visited:
            self.bfs_nc(x+1,y,grid,visited)
        if (x-1,y) not in visited:
            self.bfs_nc(x-1,y,grid,visited)
        
        
        if (x,y + 1) not in visited:
            self.bfs_nc(x,y+1,grid,visited)
        if (x,y - 1) not in visited:
            self.bfs_nc(x,y-1,grid,visited)