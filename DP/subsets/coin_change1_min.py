"""
Given an array or list of coin denominations ( coin value) and a target value
How many minimum coins you need to reach your target

eg. arr[] = [1,2,3] , target = 7

Ans: 3
Explanation: 1 3 3, 1 one rupee, 2 three rupee ( pick 1 denomination once and pick 3 denomination twice)



"""

def min_coins(coins, target):
    n = len(coins)


    ## Recursive code
    # def ans(index, target):
    #     if index == 0:
    #         if target % coins[index] == 0:
    #             return target // coins[index]
    #         else:
    #             return float("Inf")
    #     donttake = 0 + ans(index - 1, target)
    #     take = float("Inf")
    #     if coins[index] <= target:
    #         take = 1 + ans(index, target - coins[index])
    #     return min(take, donttake)
    # return ans(n-1, target)

    ## Tabulation
    # dp = [[float("inf") for _ in range(target + 1)] for _ in range(n)]
    # for tgt in range(target + 1):
    #     if tgt % coins[0] == 0:
    #         dp[0][tgt] = tgt // coins[0]
    # for i in range(1, n):
    #     for tgt in range(target + 1):
    #         dont = dp[i-1][tgt]
    #         take = float("Inf")
    #         if coins[i] <= tgt:
    #             take = 1 + dp[i][tgt - coins[i]]
    #         dp[i][tgt] = min(take, dont)
    # return dp[n-1][target]


    ## Space Optmization
    prev = [float("inf") for _ in range(target + 1)]
    for tgt in range(target + 1):
        if tgt % coins[0] == 0:
            prev[tgt] = tgt // coins[0]
    for i in range(1, n):
        curr = [float("inf") for _ in range(target + 1)]
        for tgt in range(target + 1):
            dont = prev[tgt]
            take = float("Inf")
            if coins[i] <= tgt:
                take = 1 + curr[tgt - coins[i]]
            curr[tgt] = min(take, dont)
        prev = curr
    return prev[target]
    

coins = [1,2,3]
target = 7

# coins = [5,3,4,2,8]
# target = 8
print(min_coins(coins, target))