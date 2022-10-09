#### LONGEST COMMON SUBSEQUENCE ####

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)


    # Memoization
    # def ans(s1index, s2index, dp):
    #     if s1index < 0 or s2index < 0:
    #         return 0
    #     if dp[s1index][s2index] != -1:
    #         return dp[s1index][s2index]
    #     if s1[s1index] == s2[s2index]:
    #         dp[s1index][s2index] = 1 + ans(s1index - 1, s2index - 1, dp)
    #         return dp[s1index][s2index]
        
    #     dp[s1index][s2index] = max(
    #         ans(s1index - 1, s2index, dp),
    #         ans(s1index, s2index - 1, dp)
    #     )
    #     return  dp[s1index][s2index]
    # # N * M Dp array
    # dp = [[-1 for _ in range(m)] for _ in range(n)]
    # return ans(n - 1, m - 1, dp)


    #Tabulation
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    
    """
    The recusive base case says if index becomes -1
    we can't represent that in DP array
    So, instead we will do right shift of indexes by 1

    [0 1 2 3... N]
    We will consider the 0th index as -1 index
    and from 1.... N will be considered as 0 .... N
    """
    for i in range(n + 1):
        dp[i][0] = 0

    for j in range(m + 1):
        dp[0][j] = 0
    

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

s1 = "acd"
s2 = "ced"
s1 = "mhunuzqrkzsnidwbun"
s2 = "szulspmhwpazoxijwbq"

print(lcs(s1, s2))