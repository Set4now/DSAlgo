from typing import List
"""

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # def ans(i, j):
        #     if i == len(prices):
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if j == 1: #buy
        #         dp[i][j] = max(-prices[i] + ans(i+1, 0), 0 + ans(i+1, 1))
        #     else: #sell
        #         dp[i][j] = max(prices[i] + ans(i+1, 1), 0 + ans(i+1, 0))
        #     return dp[i][j]

        # dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        # return ans(0, 1)


        n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n + 1)]
        # dp[n][0] = 0
        # dp[n][1] = 0

        # prev = [0, 0 ]
        # for i in range(n - 1, -1, -1):
            
        #     for bs in [0, 1]:
        #         if bs == 1: # buy i f1
        #             dp[i][bs] = max(
        #                 -prices[i] + dp[i+1][0], 
        #                 0 + dp[i+1][1]
        #             )
        #         else: # cat buy if 0 
        #             dp[i][bs] = max(
        #                 prices[i] + dp[i+1][1], 
        #                 0 + dp[i+1][0]
        #             )
        # return dp[0][1]


        prev = [0, 0]
        for i in range(n - 1, -1, -1):
            curr = [0, 0]
            for bs in [0, 1]:
                profit = 0
                if bs == 1: # buy i f1
                    profit = max(
                        -prices[i] + prev[0], 
                        0 + prev[1]
                    )
                else: # cat buy if 0 
                    profit = max(
                        prices[i] + prev[1], 
                        0 + prev[0]
                    )
                curr[bs] = profit
            prev = curr
        return prev[1]


                