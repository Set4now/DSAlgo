from typing import List
"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""
## Recursive method
def besttime(pricelist):
    def ans(i, profit):
        if i == len(pricelist) - 1:
            return 0, pricelist[i]
        lastmaxprofit, lastmaxprice = ans(i+1, profit)
        curr_profit = lastmaxprice - pricelist[i]
        current_max_price = max(pricelist[i], lastmaxprice)
        curr_max_profit = max(lastmaxprofit, curr_profit)
        return curr_max_profit, current_max_price
    #dp = [[-1 for i in ]]

    return ans(0, 0)

# Iterative method
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            curr_profit = prices[i] - minPrice
            maxProfit = max(curr_profit, maxProfit)
            minPrice = min(minPrice, prices[i])
        return maxProfit
        
price = [7,45,4,6,2,84]
price = [100,34,0]
print(besttime(price))


        