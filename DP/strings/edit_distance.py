class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        n = len(word1)
        m = len(word2)
        if word1 == "":
            return m
        if word2 == "":
            return n
        
        # def ans(i, j):
        #     if i < 0:
        #         return j + 1
        #     if j < 0:
        #         return i + 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if word1[i] == word2[j]:
        #         dp[i][j] = ans(i-1, j-1)
        #         return dp[i][j]
        #     else:
        #         # insert, 
        #         insert = 1 + ans(i, j - 1)
        #         # delete
        #         delete = 1 + ans(i-1, j)
        #         # replace 
        #         replace =  1 + ans(i-1, j-1)
        #         dp[i][j] = min(insert, delete, replace)
        #         return dp[i][j]
        
        # dp = [[-1 for _ in range(m)] for _ in range(n)]
        # return ans(n -1, m - 1)

        # dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        # for j in range(m+1):
        #     dp[0][j] = j
        # for i in range(1, n+1):
        #     dp[i][0] = i

        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             insert = 1 + dp[i][j - 1]
        #             delete = 1 + dp[i - 1][j]
        #             replace = 1 + dp[i - 1][j - 1]
        #             dp[i][j] = min(insert, delete, replace)
        # return dp[n][m]

        prev = [-1 for _ in range(m+1)]
        curr = [-1 for _ in range(m+1)]
        for i in range(1, n+1):

            for j in range(1, m+1):
                if i == 0:
                    curr[i] = j
                elif j == 0:
                    curr[j] = i
                elif word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    insert = 1 + curr[j-1]
                    delete = 1 + prev[j]
                    replace = 1 + prev[j - 1]
                    curr[j] = min(insert, delete, replace)
            #curr = prev
            prev = curr
        return prev[m]



        
