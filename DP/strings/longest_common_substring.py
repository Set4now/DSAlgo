"""

A substring of a string is a smaller string which maintains order 
and are contiguous 


absdfs

Substring is bsd, sdfs


s1 = "abcjklp"
s2 = "acjknmp"

ans = 3 
"cjk" is longest common subsstring
"""

def longest_common_substring(s1, s2):
    n = len(s1)
    m = len(s2)


    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0

    ans = -float("Inf")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                ans = max(ans, 1 + dp[i-1][j-1])
                dp[i][j] = ans
            else:
                dp[i][j] = 0
    return ans