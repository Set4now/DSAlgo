"""
Minimum no. of deletions & insertions to transform 1 string into another

At one step or operation
You can either delete 1 char from s1
or 
insert any chac anywhere in S1

Solution: 

Observation: 
Longest common subsequence btw the 2 strings(S1 and S2) are the one which will
not require any modification in S1.

Now the remaining chars in S1 can be deleted and if we add all the remaining in S2 to S2, 
then surely S1 will transform to S2.

1. Find LCS(s1, s2)
2. ans:- 
    Min total operations required is ( len(S1) - lcs ) + ( len(S2) - lcs ) 


"""


def longest_common_subsequence(s1, s2):
    n = len(s1)
    m = len(s2)
    #ans = -float("Inf")
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

def min_operation_transform(s1, s2):
    n = len(s1)
    m  = len(s2)
    lcs = longest_common_subsequence(s1, s2)
    return (n - lcs) + (m - lcs)


s1 = "abcd"
s2 = "anc"

s1 = "heap"
s2 = "pea"
print(min_operation_transform(s1, s2))