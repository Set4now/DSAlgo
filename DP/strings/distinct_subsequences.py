class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # def countSubsequences(i, j):
        #     if j < 0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if s[i] == t[j]:
        #         dp[i][j] = countSubsequences(i-1, j-1) + countSubsequences(i-1, j)
        #         return dp[i][j] 
        #     else:
        #         dp[i][j] = countSubsequences(i-1, j)
        #         return dp[i][j]

        n = len(s)
        m = len(t)
        #dp = [[-1 for _ in range(m)] for _ in range(n)]
        #return countSubsequences(n-1, m-1)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = 1
        # for j in range(m+1):
        #     dp[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        #print(dp)
        return dp[n][m]

s = "rabbbit"
t = "rabbit"
so = Solution()
print(so.numDistinct(s, t))