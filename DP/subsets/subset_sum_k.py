"""
Q. Return True if there is any subset whose sum is equal to K

"""

####### Recursion #########
# def subset_sum(index, target, arr):
#     if index < 0:
#         return False
#     if arr[index] == target:
#         return True
#     if index == 0:
#         if arr[index] == target:
#            return True
#     dont_take = subset_sum(index-1, target, arr)
#     take_it = False
#     if arr[index] <= target:
#         take_it = subset_sum(index-1, target - arr[index], arr)
#     return take_it or dont_take

# arr = [1,4,6,6,8]
# k = 100

# arr = [1000,4,6,6,8,4,19,74,89,56,33,23,13,100,200]
# k = 1300
# # print(subset_sum(len(arr) - 1, k, arr))
# print(subset_sum(len(arr) - 1, k, arr))

###### Memoization #######

# dp = {}


# def subset_sum(index, target, arr, dp):
#     if target == 0:
#         return True
#     if index == 0:
#         if arr[index] == target:
#            return True
#         else:
#             return False
#     if dp[index][target] != -1:
#         return dp[index][target]
#     dont_take = subset_sum(index-1, target, arr, dp)
#     take_it = False
#     if arr[index] <= target:
#         take_it = subset_sum(index-1, target - arr[index], arr, dp)
#     dp[index][target] = take_it or dont_take
#     return dp[index][target]

# arr = [1,4,6,6,8]
# k = 100


# arr = [1000,4,6,6,8,4,19,74,89,56,33,23,13,100,200]
# k = 12
# dp = [[-1 for _ in range(k+1) for _ in range(len(arr)) ]
# print(subset_sum(len(arr) - 1, k, arr, dp))


# ## Tabulation
def tabulation(arr, k):
    dp = [[False for _ in range(k+1)] for _ in range(len(arr))]
    for i in range(len(dp)):
        dp[i][0] = True
    if arr[0] <= k:
        dp[0][arr[0]] = True
    for i in range(1, len(arr)):
        for target in range(1, k+1):
            nottaken = dp[i-1][target]
            taken = False
            if arr[i] <= target:
                taken = dp[i - 1][target  - arr[i]]
            dp[i][target] = nottaken or taken
    return dp[len(arr) -1][k]



# arr = [1000,4,6,6,8,4,19,74,89,56,33,23,13,100,200]
# #k = 100000
# arr = [1,3,2]
arr = [1,5,11,3]
k = 10

arr = [3,3,3,4,5]
k = 9
#dp = [[-1] * (k+1) ] * len(arr)
print(tabulation(arr, k))


