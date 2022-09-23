
"""
A frog can jump 1 step or 2 steps in N level stairs
if a frog jumps from ith stair to jth stair
then energy lost in that jump is height[j] - heiht[i]
calculate the min energy that will be spend by the frog if it travels from 1st stair to n stair


eg,
1  2  3  4
10,20,30,10

jumps           enerygy lost
1 - 2 - 3 - 4 = 10 + 10 + 20 = 40 

1 - 2 - 4 = 10 + 10 = 20

1 - 3 - 4 = 20 + 20 

"""

############ Simple  Recursive Solution ##############################
# time complexity = 2^n , starting from index 0 | Working
# def min_energy(n, height):
#     if n == len(height) - 1:
#         return 0
#     # if n >= len(height):
#     #     return 0
#     one_step = min_energy(n + 1, height) + abs(height[n + 1] - height[n])
#     if n + 2 < len(height):
#         two_steps = min_energy(n + 2, height) + abs(height[n + 2] - height[n])
#         return min(one_step, two_steps)
#     return one_step

# Same recursive code top -> bottom, means in the recursion call, 
# 0,2,3,4,5  0 becomes bottom and 5 becomes top
# f(n - 1)
# f(n - 2)
# f(0)
def min_energy(n, height):
    if n == 0:
        return 0
    # if n >= len(height):
    #     return 0
    one_step = min_energy(n - 1, height) + abs(height[n - 1] - height[n])
    if n  > 1:
        two_steps = min_energy(n - 2, height) + abs(height[n - 2] - height[n])
        return min(one_step, two_steps)
    return one_step
# height = [10, 20, 30, 10]
# n = len(height) - 1
# print(min_energy(len(height) - 1, height))
# # 20
# height = [20, 30]
# n = len(height) - 1
# print(min_energy(n, height))
# # 10
# height = [30, 10, 60, 10, 60, 50]
# n = len(height) - 1
# print(min_energy(n, height))
# #40
############ Simple  Recursive Solution ##############################




############## DP with memoization #####################
def min_energy_dp_memoization(n, height, dp):
    if n == len(height) - 1:
        dp[n] = 0
        return dp[n]
    
    if dp[n] != -1:
        return dp[n]
    else:
        one_step = min_energy_dp_memoization(n + 1, height, dp) + abs(height[n + 1] - height[n])
        if n + 2 < len(height):
            two_steps =  min_energy_dp_memoization(n + 2, height, dp) + abs(height[n + 2] - height[n])
            dp[n] = min(one_step, two_steps)
            return dp[n]
        dp[n] = one_step
        return dp[n]
# height = [10, 20, 30, 10]
# dp = [-1] * len(height)
# print(min_energy_dp_memoization(0, height, dp))
# height = [20, 30]
# dp = [-1] * len(height)
# print(min_energy_dp_memoization(0, height, dp))
# height = [30, 10, 60, 10, 60, 50]
# dp = [-1] * len(height)
# print(min_energy_dp_memoization(0, height, dp))
############## DP with memoization #####################



################# Tabular ##############################
# def tabular_bottom_up(height):
#     n = len(height)
#     dp = [0] * n
#     dp[0] = 0
#     for index in range(1, n):
#         step_one = dp[index - 1] + abs(height[index-1]- height[index])
#         step_two = float("Inf")
#         if index > 1:
#            step_two = dp[index - 2] + abs(height[index-2]- height[index]) 
#         dp[index] = min(step_one, step_two)
#     return dp[n-1]

# height = [10, 20, 30, 10]
# print(tabular_bottom_up(height))
# height = [20, 30]
# print(tabular_bottom_up(height))
# height = [30, 10, 60, 10, 60, 50]
# print(tabular_bottom_up(height))
################# Tabular ##############################



################### Space Optmization using only 2 variables ######################
def min_energu_space_optz(height):
    prev = 0
    prev2 = 0
    n = len(height)
    for i in range(1, n):
        step_one = prev + abs(height[i-1]- height[i])
        step_two = float("Inf")
        if i > 1:
            step_two = prev2 + abs(height[i-2]- height[i])
        curr_min = min(step_one, step_two)
        prev2 = prev
        prev = curr_min
    return prev

height = [10, 20, 30, 10]
print(min_energu_space_optz(height))
height = [20, 30]
print(min_energu_space_optz(height))
height = [30, 10, 60, 10, 60, 50]
print(min_energu_space_optz(height))