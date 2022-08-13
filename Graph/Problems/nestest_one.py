class Solution:
    def nearest(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = "S"

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.dfs(i, j, grid)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "S":
        #             grid[i][j] = 0
        print(grid)
		            
    def dfs(self, x, y, grid):
        print(grid[x][y])
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "S":
            return

        grid[x][y] += 1
	                   
        self.dfs(x + 1, y, grid )
        self.dfs(x - 1, y, grid )
        self.dfs(x, y + 1, grid )
        self.dfs(x, y - 1, grid )


grid = [[0, 1, 1, 0 ], [1, 1, 0, 0 ], [0, 0, 1, 1 ]]
s = Solution()
s.nearest(grid)