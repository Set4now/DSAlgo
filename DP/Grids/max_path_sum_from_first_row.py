


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def max_path(x, y, dp):
            if x >= len(matrix) or y >= len(matrix[x]) or y < 0:
                return float("Inf")
            if x == len(matrix) - 1:
                return matrix[x][y]
            if dp[x][y] != -1:
                return dp[x][y]
            down = matrix[x][y] + max_path(x + 1, y, dp)
            diag_left = matrix[x][y] +  max_path(x + 1, y - 1, dp)
            diag_right = matrix[x][y] +  max_path(x + 1, y + 1, dp)
            
            # print(down, diag_left, diag_right)
            dp[x][y] =  min(down, diag_left, diag_right)
            return dp[x][y]
        
        if m == 1:
            return max(matrix[0])
        
        
        result = float("Inf")
        #return max_path(0, 0)
        
        dp = [[-1] * n for _ in range(m)]
        for i in range(m):
            if i == 0:
                for j in range(n):
                    ans = max_path(i, j, dp)
                    result = min(ans, result)
            else:
                break
                        
        return result

# mat = [[2,1,3],[6,5,4],[7,8,9]]
# s = Solution()
# print(s.minFallingPathSum(mat))


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = matrix[0]
        for i in range(1, m):
            temp = []
            for j in range(n):
                leftop = float("Inf")
                if j > 0:
                    leftop = matrix[i][j] + dp[j-1]
                top = matrix[i][j] + dp[j]
                topright = float("Inf")
                if j + 1 < n:
                    topright = matrix[i][j] + dp[j+1]
                result = min(leftop, top, topright)
                temp.append(result)
            dp = temp
        #print(dp)
        return min(dp)

s = Solution()
mat = [[2,1,3],[6,5,4],[7,8,9]]
#mat = [[-19,57],[-40,-5]]
s = Solution()
print(s.minFallingPathSum(mat))