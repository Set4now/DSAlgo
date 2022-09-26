# top bottom 
# def unique_paths_grid(i, j, grid):
#     if i >= len(grid) or j >= len(grid[0]):
#         return 0
#     end_point_x = len(grid) - 1
#     end_point_y = len(grid[0]) - 1
#     if (i,j) == (end_point_x,end_point_y):
#         return 1

#     path_from_down = unique_paths_grid(i+1, j, grid)
#     path_from_right = unique_paths_grid(i, j+1, grid)
#     
#     return path_from_down + path_from_right

# grid = [[1,2],[3,4]]
# grid = [[1,2,3],[4,5,6],[7,8,9]]
# print(unique_paths_grid(0,0,grid))


# bottom up
# def unique_paths_grid(i, j, grid):
#     if i < 0 or j < 0:
#         return 0
#     if (i,j) == (0,0):
#         return 1

#     path_from_left = unique_paths_grid(i - 1, j, grid)
#     path_from_up = unique_paths_grid(i, j - 1, grid)
#     #print(l,r)
#     return path_from_left + path_from_up

# grid = [[1,2],[3,4]]
# grid = [[1,2,3],[4,5,6],[7,8,9]]
# grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print(unique_paths_grid(len(grid) - 1,len(grid[0]) - 1,grid))


# DP MEMOIZATION

def grid_memo(i, j, dp_results):
    if i < 0 or j < 0:
        return 0
    if (i,j) == (0,0):
        return 1
    if dp_results[i][j] != -1:
        return dp_results[i][j]

    path_from_left = grid_memo(i - 1, j, dp_results)
    path_from_up = grid_memo(i, j - 1, dp_results)
    
    dp_results[i][j] = path_from_left + path_from_up
    return dp_results[i][j]

def paths_memo(m, n):
    dp = [[-1] * n for _ in range(m)]
    return grid_memo(m - 1, n - 1, dp)


#grid = [[1,2],[3,4]]
# grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# grid = [[1,2,3],[4,5,6],[7,8,9]]

#dp = [[-1] * len(grid[0])] * len(grid)
# m = 3
# n = 7
# print(paths_memo(m, n))


# bottom up
def tabulation(m, n):
    dp = [[-1] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            else:
                up = 0
                left = 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = up + left
    return dp[m-1][n-1]
m = 3
n = 7
print(tabulation(m, n))

