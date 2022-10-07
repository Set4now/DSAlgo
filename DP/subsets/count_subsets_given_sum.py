"""
Count subsets in an array with given target sum
constraints 1 <= n < 1000


The base condition will change if 
constraints becomes 0 <= n < 1000
"""

def count_subsets(index, arr, target):
    if target == 0:
        return 1
    if index == 0:
        if arr[index] == target:
            return 1
        return 0
    notpick = count_subsets(index - 1, arr, target)
    pick = 0
    if arr[index] <= target:
        pick = count_subsets(index - 1, arr, target - arr[index])
    return pick + notpick

# arr = [1,2,3,3]
# k = 6

# arr = [1,1,1,1]
# k = 1
# print(count_subsets(len(arr) - 1, arr, k))

# memoization
def count_subsets(index, arr, target, dp):
    if target == 0:
        return 1
    if index == 0:
        if arr[index] == target:
            return 1
        return 0
    if dp[index][target] != -1:
        return dp[index][target]
    notpick = count_subsets(index - 1, arr, target, dp)
    pick = 0
    if arr[index] <= target:
        pick = count_subsets(index - 1, arr, target - arr[index], dp)
    dp[index][target] =  pick + notpick
    return dp[index][target]




# arr = [1,1,1,1]
# k = 1

# arr = [1,2,3,3]
# k = 6

# dp = [[-1 for _ in range(k + 1)] for _ in range(len(arr))]
# print(count_subsets(len(arr) - 1, arr, k, dp))

def tabular(arr, target):
    dp = [[0 for _ in range(k + 1)] for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = 1
    if arr[0] <= target:
        dp[0][arr[0]] = 1
    for i in range(1, len(arr)):
        for j in range(target +1):
            notpick = dp[i-1][j]
            pick = 0
            if arr[i] <= j:
                pick = dp[i-1][j - arr[i]]
            dp[i][j] = pick + notpick
    return dp[len(arr) - 1][target]

arr = [1,2,3,3]
k = 6

# arr = [1,1,1,1]
# k = 1

print(tabular(arr, k))
