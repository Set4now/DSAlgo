"""
Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.


Using BFS

1.find all the 1's and store their coordinates in the Queue

2. create a result matrix and make sure to store 1's indexs as 0, since distance of itself is always 0 and other cell as infinity
The result matrix will be our ans, where each cell will repesent the min distance of the nearest 1 from that 
corresponding cell at the input matrix

example 
result
[inf, inf, 0]
[inf, inf, 0]
[inf, inf, 0]

3. pop each 1's coordinates from the Q
    get its 4 neibour's cell top down left right
    update its neibour's cell as (currentcell + 1) if neibour's cell current value is greater than (currentcell + 1)
    # We will only store min distance, means if the current min distance is less than the current. then only update

4. return the result matric

BigO(M * N)

"""

class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid):
        q = []
        row = len(grid)
        col = len(grid[0])
        result = [[float("Inf")] * col for _ in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
                    result[i][j] = 0
        
        for i,j in q:
            for x,y in (1,0), (-1,0), (0, 1), (0, -1):
                dx = i + x
                dy = j + y
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and result[i][j] + 1 < result[dx][dy] :
                    result[dx][dy] = result[i][j] + 1
                    q.append((dx,dy))
        return result