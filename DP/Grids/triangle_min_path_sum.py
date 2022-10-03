"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
2
3 4
6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).


"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        """
        ########## Memoization ###############
        def get_sum(i, j, dp):
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0
            if i == len(triangle) - 1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            down = triangle[i][j] + get_sum(i+1,j, dp)
            right_down_diagonal = triangle[i][j] + get_sum(i+1, j+1, dp)
            
            dp[i][j] = min(down, right_down_diagonal)
            return dp[i][j]
        
        dp = []
        for i in range(len(triangle)):
            dp.append([-1] * len(triangle[i]))
                
        return get_sum(0,0, dp)


        ############## TABULATION ###########
        dp = []
        for i in range(len(triangle)):
            dp.append([-1] * len(triangle[i]))
        
        last_row_length = len(triangle[-1])
        for i in range(last_row_length):
            dp[last_row_length - 1][i] = triangle[last_row_length - 1][i]
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                down = triangle[i][j] + dp[i+1][j]
                down_diagonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down, down_diagonal)

        return dp[0][0]
        """


        ############# Space Optimization ##############
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            temp = []
            for j in range(len(triangle[i])):
                down = triangle[i][j] + dp[j]
                down_diagonal = triangle[i][j] + dp[j+1]
                temp.append(min(down, down_diagonal))
            dp = temp

        return dp[0]

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
#triangle = [[-10]]
print(s.minimumTotal(triangle))