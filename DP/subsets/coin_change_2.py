from typing import List
"""
Return the number of ways you can make the target by using 
any number of denominations from the list of coins.

Solution: Same as coin change 1 but here we need to return 1 or 0
in the base case depending on whether or not we can make the target or not

"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
        for tgt in range(amount + 1):
            if tgt % coins[0] == 0:
                dp[0][tgt] = 1
        for i in range(1, n):
            for tgt in range(amount+1):
                nottake = dp[i-1][tgt]
                take = 0
                if coins[i] <= tgt:
                    take = dp[i][tgt - coins[i]]
                dp[i][tgt] = nottake + take
        return dp[n-1][amount]



        