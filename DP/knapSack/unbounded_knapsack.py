"""
Similar to 0/1 knapsack problem, return the max profit by picking any item or items 
infinite number of times.
But here you can pick any item infinite times.

"""

wt= [7,9,1]
val = [5,11,100]
w = 2

def unbounded_knapsack(wtlist, vallist, w):
    
    # recursive approach
    # def ans(index, capacity):
    #     if index == 0:
    #         if wt[0] <= capacity:
    #             return val[0]
    #         else:
    #             return 0
    #     notpick = ans(index - 1, capacity)
    #     pick = -float("Inf")
    #     if wt[index] <= capacity:
    #         pick = val[index] + ans(index, capacity - wt[index])
    #     return max(pick, notpick)
    # return ans(len(vallist) - 1, w)

    # Tabular
    def knapsack(weightlist, bagweight, valuelist):
        dp = [[0 for _ in range(bagweight + 1)] for _ in range(len(valuelist))]
        # if weightlist[0] <= bagweight:
        #     dp[0][weightlist[0]] = valuelist[0]

        for i in range(weightlist[0], bagweight+1):
            dp[0][i] = valuelist[0]

        for i in range(1, len(valuelist)):
            for cur_weight in range(bagweight + 1):
                nottake = dp[i-1][cur_weight]
                take  = -float("Inf")
                if weightlist[i] <= cur_weight:
                    take = valuelist[i] + dp[i][cur_weight - weightlist[i]]
                dp[i][cur_weight] = max(take, nottake)
        return dp[len(valuelist) - 1][bagweight]
    return knapsack(wtlist, w, vallist)


print(unbounded_knapsack(wt, val, w))
