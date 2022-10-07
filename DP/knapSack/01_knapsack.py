"""

0/1 Knapsack

Given a Bag of weight W (Capacity)
&
weight array
value array

You can pick 1 instance of item , return the max profit 
you can get by picking items from the list without breaching the 
Bag's capacity. Whenever you pick an item , its value will added to 
the benefit and similary its weight will be deducted from total
Bag's capacity (W).

NOTE: You can't pick the item twice.

"""


weight = [3, 2, 5]
value = [30, 40, 60]
bagweight = 6


## Tabular
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
                take = valuelist[i] + dp[i-1][cur_weight - weightlist[i]]
            dp[i][cur_weight] = max(take, nottake)
    return dp[len(valuelist) - 1][bagweight]



## Space Optimization
def knapsack(weightlist, bagweight, valuelist):
    #dp = [[0 for _ in range(bagweight + 1)] for _ in range(len(valuelist))]
    
    prev = [0 for _ in range(bagweight + 1)]
    for i in range(weightlist[0], bagweight+1):
        prev[i] = valuelist[0]

    for i in range(1, len(valuelist)):
        curr = [0 for _ in range(bagweight + 1)]
        for cur_weight in range(bagweight + 1):
            nottake = prev[cur_weight]
            take  = -float("Inf")
            if weightlist[i] <= cur_weight:
                take = valuelist[i] + prev[cur_weight - weightlist[i]]
            curr[cur_weight] = max(take, nottake)
        prev = curr

    return prev[bagweight]

print(knapsack(weight, bagweight, value))

