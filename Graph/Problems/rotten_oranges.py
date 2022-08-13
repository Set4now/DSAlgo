"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 

Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.
Example 2:

Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).

Algorithm
BFS ( Very similar to count of Islands)



1. We start traversing the array and store all the 2's (rotten orange) coordinates in a Q.
2. While Q is not empty
    pop each coordinate of already rotten oranges from Q
    rot all its adjacent oranges if present in top, left, right, down & append their adjacent rotten organes coordinates to the Queue
    Continue doing this until the queue becmoes empty

    We rot all the adjacent oranges (paralley) at the same time, that is one unit time

3. Traverse the grid, if you found any left fresh oranges, then return -1
4. else return unit time count
"""


class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        #Code here
        time = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
         
        
        while q:
            size = len(q)
            did_it_rot = False

            # All the adjacent oranges has to be rot in the same time
            # BFS using queue

            # process all the adjacent oranges stored in the queue at a same time and dequeu them
            # and enque new rotten orange coordinates to process later (BFS using Queue)
            for _ in range(size):
                x, y = q[0]
                del q[0]
                
                for x1, y1 in (1,0),(-1,0),(0,1),(0,-1):
                    dx = x + x1
                    dy = y + y1
                    if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
                        if grid[dx][dy] == 1:
                           grid[dx][dy] = 2
                           q.append((dx, dy))
                           did_it_rot = True
            if did_it_rot:
                time += 1
                did_it_rot = False # resetting
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time
                            
                
                
                
                
        
    def dfs(self, x, y, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return
        grid[x][y] = 2
        self.dfs(x+1, y, grid)
        self.dfs(x-1, y, grid)
        self.dfs(x, y + 1, grid)
        self.dfs(x, y - 1, grid)