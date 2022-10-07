"""
Given an array of positive integers ( 0 <= n < 1000) and target difference D, count the number of valid partitons (subsets)
which satisfies these two conditons
S1 > S2
S1 - S2 = D

Solution:
we can write S1 as Totalarrsum - S2

We rewrite the equation S1 - S2 = D as

Totalarrsum - S2 - S2 = D
Totalarrsum - D = 2 * S2
S2 = Totalarrsum - D / 2

Means, we just need to find the count of subsets with a Target sum  equal to  ( Totalarrsum - D / 2 )

Edge cases to consder
1. Its an array of only positive integers that means
totalsum - D cannot be 0

2. There is not fractions or decimals in the array, means the sum diff (s1 - S2 ) also cannot be fractions

"""

def count_subsets(arr, d):
    tgt = sum(arr) - d 
    # edge case 1
    if tgt < 0:
        return 0

    # edge case 2
    if tgt % 2 != 0:
        return 0
    
    ###  Memoization #######
    def count(index, target, dp):
        if index == 0:
            if target == 0 and arr[0] == 0:
                return 2
            elif target == 0 and arr[0] != 0:
                return 1
            elif arr[0] == target:
                return 1
            elif arr[0] != target:
                return 0
        if dp[index][target] != -1:
            return dp[index][target] 
        nottake = count(index - 1, target, dp)
        take = 0
        if arr[index] <= target:
            take = count(index - 1, target - arr[index], dp)
        dp[index][target] = take + nottake
        return dp[index][target]
    
    def tabulation(target):
        dp = [[0 for _ in range(target + 1)] for _ in range(len(arr))]

        if arr[0] == 0:
            dp[0][0] = 2
        if arr[0] != 0:
            dp[0][0] = 1

        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1

        for index in range(1, len(arr)):
            for tgt in range(target + 1):
                nottake = dp[index - 1][tgt]
                take = 0
                if arr[index] <= tgt:
                    take =  dp[index - 1][tgt - arr[index]]
                dp[index][tgt] = take + nottake
        return dp[len(arr) - 1][tgt]


    target = tgt // 2
    # dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr))]
    # return count(len(arr) - 1, target, dp)

    return tabulation(target)

arr = [5, 2, 5, 1]
d = 3
print(count_subsets(arr, d))