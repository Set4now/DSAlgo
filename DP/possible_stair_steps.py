"""

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


"""


# Recursive solution
# at every stair we have 2 options, either take one step or 2 steps
def possible_steps(index):
    if index == 0 or index == 1:
        return 1
    l = possible_steps(index - 1)
    r = possible_steps(index - 2)
    return l + r

# n = 3
# print(possible_steps(5))



# There are overlapping sub problems, so This can changed to DP with memoization
# class Solution:
    
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * ( n + 1)
#         return self.dp_solution(n, dp)
        
    
#     def dp_solution(self, n, dp):
#         if n == 1 or n == 0:
#             dp[n] = 1
#             return dp[n]
        
#         if dp[n - 1] != -1:
#             l = dp[n - 1]
#         else:
#             dp[n - 1] = self.dp_solution(n - 1, dp)
#             l = dp[n - 1]
            
#         if dp[n - 2] != -1:
#             r = dp[n - 2]
#         else:
#             dp[n - 2] = self.dp_solution(n - 2, dp)
#             r = dp[n - 2]
            
            
#         #r = self.climbStairs(n - 2)
#         return l + r


# Space optimized solution ( 2 varibles)
class Solution:
    
    def climbStairs(self, n: int) -> int:
        # last_stair = 1
        # second_last_stair = 1
        # n -= 1
        # while n >= 1:
        #     temp = last_stair + second_last_stair
        #     last_stair = second_last_stair
        #     second_last_stair = temp 
        #     print(second_last_stair, n)
        #     n -= 1

        # Same as fibonacci code
        i = 0
        last_stair = 0
        second_last_stair = 1
        while i < n:
            temp = last_stair + second_last_stair
            last_stair = second_last_stair
            second_last_stair = temp 
            i += 1



        return second_last_stair




s = Solution()
print(s.climbStairs(5))