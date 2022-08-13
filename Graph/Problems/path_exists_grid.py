"""
Given a grid of size n*n filled with 0, 1, 2, 3. Check whether there is a path possible from the source to destination. You can traverse up, down, right and left.
The description of cells is as follows:

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Wall.
Note: There are only a single source and a single destination


Input: grid = {{3,0,3,0,0},{3,0,0,0,3}
,{3,3,3,3,3},{0,2,3,0,0},{3,0,0,1,3}}
Output: 0
Explanation: The grid is-
3 0 3 0 0 
3 0 0 0 3 
3 3 3 3 3 
0 2 3 0 0 
3 0 0 1 3 
There is no path to reach at (3,1) i,e at 
destination from (4,3) i,e source.


Input: grid = {{1,3},{3,2}}
Output: 1
Explanation: The grid is-
1 3
3 2
There is a path from (0,0) i,e source to (1,1) 
i,e destination.


The solution is similar to COunt if island (0 or 1)

"""
class Solution:

    # Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        # Code here
        visited = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited:
                    if grid[i][j] == 1: #if you get source then start dfs
                        if self.dfs(i, j, 1, 2, grid, visited):
                            return 1
        return 0

    def dfs(self, x, y, src, destination, grid, visited):
        # stop if you get a wall (0)
        
        
        # If you get a wall stop
        if ( x < 0 ) or ( x >= len(grid)) or  (y < 0 ) or ( y >= len(grid[0]) ) or ( grid[x][y] == 0):
            return False
        
        # if you reach destination , return True
        if grid[x][y] == destination:
            return True

        # don't visit a path which is already visited or examined and can't reach to destination
        if (x, y ) not in visited:
            visited.append((x, y))
            if grid[x][y] == 3 or grid[x][y] == 1:
                    if (
                        # If you reach to destination form any top , down , left , right path, return true
                        self.dfs(x - 1, y, src, destination, grid, visited)
                        or self.dfs(x + 1, y, src, destination, grid, visited)
                        or self.dfs(x, y + 1, src, destination, grid, visited)
                        or self.dfs(x, y - 1, src, destination, grid, visited)
                    ):
                        return True
        return False


grid = [[3, 0, 3, 0, 0], [3, 0, 0, 0, 3], [3, 3, 3, 3, 3], [0, 2, 3, 0 ,0], [3, 0, 0, 1, 3]]

"""
[3, 3, 3, 3, 0, 0, 3, 0]
[1, 3, 3, 3, 3, 3, 3, 2]
[3, 3, 0, 3, 0, 3, 3, 3]




3 1 3 0 0 3 3 0
0 3 3 3 3 0 3 3
0 0 0 3 3 0 3 3
0 3 0 3 0 3 2 0
3 3 3 0 3 3 3 3


"""
grid = [
[3, 3, 3, 3, 0, 0, 3, 0],
[1, 3, 3, 3, 3, 3, 3, 2],
[3, 3, 0, 3, 0, 3, 3, 3]
]

# grid = [
# [1, 3, 3, 3, 3, 3, 3, 2],
# ]


s = Solution()
print(s.is_Possible(grid))