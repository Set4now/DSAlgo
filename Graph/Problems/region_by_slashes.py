from collections import defaultdict
from typing import List
"""

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. 
These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.



Solution:- 

This is a Disjoint set Problem and the regions are nothing but number of cycles

Observation:-

grid = [" /","/ "],  ( n x n ) is 1 * 1 squares
mens:
each string represents each square

space forwardslash
space forwardslash
[ / ]
[/  ]
region: 2
This can be seen in dot matrix as

*---*---*
|     / |
*   *   *
| /     |
*___*___*


another example

["/\\","\\/"]

[/\]
[\/]

This can be seen in dot matrix as
*---*---*
|  /  \ |
*       *
| \   / |
*___*___*

region: 5


NOTE: dot_matrix_len = len(grid) + 1

Formula, if i,j in input grid is / or \\, then which corresponding vertices to connect from virtual dot matrix
if i,j = "/" 
(i,j+1) --> (i+1, j) in dot matrix

if i,j = "\"
(i,j) --> (i+1,j+1) in dot matrix

dots_grid_vertex of an coordinate (i,j) 
cell = ( i * (len(point_grid) + 1) )+ j


Then, simply connect all the border vertices in virtual dot matrix
(union of 0 to all other vertices which are in border)
How to find vertex number from  virtual dot matrix from (i,j) in input grid
formula


dots_grid_vertex = ( i *  dot_matrix_len ) + j

"""

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
      
        
        points_grid_len = len(grid) + 1
        self.parent = [-1] * ( points_grid_len * points_grid_len )
        self.rank = [0] * ( points_grid_len * points_grid_len )
        

        # by default the square itself is a region
        region = 1

        # makiing an Union of 0 to all the border dots from the virtual dots grid
        for i in range(points_grid_len):
            for j in range(points_grid_len):
                if i == 0 or j == 0 or i == len(grid) or j == len(grid):
                    # cell formula ( i + point grid len) + j
                    dots_grid_vertex = ( i *  points_grid_len ) + j
                    if dots_grid_vertex != 0:
                        self.union(0, dots_grid_vertex)

        for i in range(len(grid)):
           # replacing  / with "f", \\ with "b", " " with "s"
           grid[i] = grid[i].replace("\\", "b").replace(" ", "s").replace("/", "f")

        for i in range(len(grid)):
            temp = [c for c in grid[i]]
            for j in range(len(temp)):
                if temp[j] == "f":
                    # trying to add edge btw 2 coordinates from dot grid
                    #coordinate1 = (i, j+1)
                    dots_grid_vertex1 = ( i *  points_grid_len ) + ( j + 1)

                    # coordinate2 = (i+1, j+1)
                    dots_grid_vertex2 = ( ( i + 1 ) *  points_grid_len ) + j
                    if not self.union(dots_grid_vertex1, dots_grid_vertex2):
                        region += 1

                if temp[j] == "b":
                    # trying to add edge btw 2 coordinates from dot grid
                    #coordinate1 = (i, j)
                    dots_grid_vertex1 = ( i *  points_grid_len ) + j

                    # coordinate2 = (i+1, j+1)
                    dots_grid_vertex2 = ( ( i + 1 ) *  points_grid_len ) + ( j + 1)
                    if not self.union(dots_grid_vertex1, dots_grid_vertex2):
                        region += 1

        return region



    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx != parenty:
            # if rank of both x and y are same then point Absolute parent of x to absolute parent of y
            # and increment RANK if  absolute parent of y by 1
            if self.rank[x] == self.rank[y]:
                self.parent[parentx] = parenty
                self.rank[parenty] += 1
            else:
                """
                if rank of x is greater than rank of y
                    then point absolute parent of y to absolute parent of x
                    increment RANK of  ( absolute parent of x ) by 1
                if rank of y is greater than rank of x
                    then point absolute parent of x to absolute parent of y
                    increment RANK of  ( absolute parent of y ) by 1
                """
                if self.rank[x] > self.rank[y]:
                    self.parent[parenty] = parentx
                    self.rank[parentx] += 1
                else: 
                    self.parent[parentx] = parenty
                    self.rank[parenty] += 1
            return True
        else:
            False


    def find(self, x):
        if self.parent[x] == -1:
            return x 
        else:
            return self.find(self.parent[x])


s = Solution()
grid = [" /","/ "]
print(s.regionsBySlashes(grid))

grid = [" /","  "]
print(s.regionsBySlashes(grid))


grid = ["/\\","\\/"]
print(s.regionsBySlashes(grid))






    