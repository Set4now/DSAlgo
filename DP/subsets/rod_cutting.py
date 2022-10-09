def max_profit_rod_cut(n, price):
    
    """
    list in python are 0 based index
    The price array is list of prices for each length
    where length is the index order.

    eg
    [2,5,7,8,10] means
    rod of length 1 = 2
    rod of length 2 = 5
    .....
    rod of length 5 = 10

    So for our conveinet we are creating a n+1 index array 
    so that we can ignore 0th index (unused)

    or to counter this,
    just do a index + 1 to create the current rod length from the index


    [ ]
     1

    if rodlength == 0:
        return 0 
    if index == 0:
        return price[0]

    """
    # new_price_list = [0]
    # for p in price:
    #     new_price_list.append(p)
    
    ######## recursive solution ##########
    def ans(index, rodlength):
        if index == 0:
            return price[0] * rodlength

        nottake = 0 + ans(index - 1, rodlength)
        take = -float("Inf")

        curr_length = index + 1
        if curr_length <= rodlength:
            take = price[index] + ans(index, rodlength - curr_length)
        return max(nottake, take)

    return ans(len(price) - 1, n)


    ########### Tabulation ###########  
    # new_price_list = [0]
    # for p in price:
    #     new_price_list.append(p)

    # dp = [[0 for _ in range(n + 1)] for _ in range(n)]
   
    # # for i in range(n):
    # #     dp[i][0] = 0
    # for length in range(n+1):
    #     dp[0][length] = price[0] * length
    # # for i in range(n+1):
    # #     dp[0][i] = price[0] * i
    # # for j in range(n+1):
    # #     dp[0][j] = price[0]

    # for index in range(1, n):
    #     for rl in range(n+1):
    #         nottake = 0 + dp[index - 1][rl]
    #         take = -float("Inf")
    #         curr_length = index + 1
    #         if curr_length <= rl:
    #             take = price[index] + dp[index][rl - curr_length]
    #         dp[index][rl] = max(take, nottake)
    # #print(dp)
    # return dp[n - 1][n]


n = 5
price = [2,5,7,8,100]


n = 8
price = [3,5,8,9,10,17,17,20]
print(max_profit_rod_cut(n, price))