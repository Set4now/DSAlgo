"""
44. Wildcard Matching
Hard
5.9K
257
Companies
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True 
        if p == "*":
            return True

        # i is for p (patter)
        # j is for s (string to match)
        def ans(i, j):
            if i < 0 and j < 0:
                return True
            if i < 0 and j >= 0:
                return False
            if i >= 0 and j < 0:
                for idx in range(i+1):
                    if p[idx] != "*":
                        return False
                else:
                    return True
            if dp[i][j] != -1:
                return dp[i][j]
                
            if p[i] == s[j] or p[i] == "?":
                dp[i][j] = ans(i-1, j-1)
                return dp[i][j]
            elif p[i] == "*":
                dp[i][j] = ans(i, j-1) or ans(i-1, j)
                return dp[i][j]
            else:
                dp[i][j] =  False
                return dp[i][j]
        
        n = len(p)
        m = len(s)
        # dp = [[-1 for _ in range(m)] for _ in range(n)]
        # return ans(n-1, m-1)

        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m+1):
            dp[0][j] = False
        for i in range(1, n+1):
            flag = True
            for ii in range(1, i+1):
                if p[ii-1] != "*":
                    flag = False
                    break
            dp[i][0] = flag
                    
        #print(dp)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        #print(dp)
        return dp[n][m]

