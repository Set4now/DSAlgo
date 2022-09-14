from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        self.grid = grid
        
        
        visited = []
        final_min = float("Inf")

        bottom_top_cost = self.bottom_top(visited)
        #print(bottom_top_cost)
        if bottom_top_cost < final_min:
            final_min = bottom_top_cost

    
        top_bottom = self.top_bottom(visited)
        #print(top_bottom)
        if top_bottom < final_min:
            final_min = top_bottom

        return final_min

    def top_bottom(self, visited):

        # last_row_index = len(grid) - 1
        # last_col_index = len(grid[0]) - 1


        q = []
        q.append((0, 0))
        cost = 0
        while q:
            i,j = q.pop(0)
            cost += grid[i][j]
            if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1:
                break
            

            min_cost = float("Inf")

            next_min_cell = (i,j)

            # move right
            dx = i + 0
            dy = j + 1
            if dx < len(self.grid) and dy < len(self.grid[0]) and (dx,dy) not in visited:
                if grid[dx][dy] < min_cost:
                    min_cost = grid[dx][dy]
                    next_min_cell = (dx,dy)
            #print(dx, dy)

            # move down
            dx1 = i + 1
            dy2 = j + 0

            #print(dx1, dy2)

            if dx1 < len(self.grid) and dy < len(self.grid[0]) and (dx1,dy2) not in visited:
                if grid[dx1][dy2] < min_cost:
                    min_cost = grid[dx1][dy2]
                    next_min_cell = (dx1,dy2)
            
            # i,j = next_min_cell
            # if j > 0:
            #     visited.append((i,j))

            #print(next_min_cell)
            q.append(next_min_cell)
            
        return cost


    def bottom_top(self,  visited):
        q = []
        last_row_index = len(grid) - 1
        last_col_index = len(grid[0]) - 1
        q.append((last_row_index, last_col_index))
        cost = 0
        while q:
            i,j = q.pop(0)
            cost += grid[i][j]
            if i == 0 and j == 0:
                break
            

            min_cost = float("Inf")

            next_min_cell = (i,j)

            # move top 
            dx = i - 1
            dy = j + 0
            if dx >= 0 and dy >= 0 and (dx,dy) not in visited:
                if grid[dx][dy] < min_cost:
                    min_cost = grid[dx][dy]
                    next_min_cell = (dx,dy)
            #print(dx, dy)

            # move left
            dx1 = i + 0
            dy2 = j - 1

            #print(dx1, dy2)

            if dx1 >=0 and dy2 >= 0 and (dx1,dy2) not in visited:
                if grid[dx1][dy2] < min_cost:
                    min_cost = grid[dx1][dy2]
                    next_min_cell = (dx1,dy2)
            
            i,j = next_min_cell
            if j > 0:
                visited.append((i,j))

            #print(next_min_cell)
            q.append(next_min_cell)
            
        return cost


grid = [[1,2,3],[4,5,6]]


#grid = [[1,3,1],[1,5,1],[4,2,1]]

grid = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]

s =Solution()
print(s.minPathSum(grid))