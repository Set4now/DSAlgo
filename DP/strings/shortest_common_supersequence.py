"""
LeetCode Hard

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"


Length of shortest should be 
n + m - len(LCS)


"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        n = len(str1)
        m = len(str2)
        def lcs(s1, s2):
            dp = [[0 for i in range(m+1)] for _ in range(n+1)]
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
            return dp

        dp = lcs(str1, str2)

        i = n
        j = m 
        output = ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                output += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                output += str1[i-1]
                i -= 1
            elif dp[i][j-1] > dp[i-1][j]:
                output += str2[j-1]
                j -= 1
            else:
                output += str2[j-1]
                j -= 1
        while i > 0:
            output += str1[i-1]
            i -= 1
        while j > 0:
            output += str2[j-1]
            j -= 1
        return output[::-1]

s = Solution()
str1 = "abac"
str2 = "cab"
print(s.shortestCommonSupersequence(str1, str2))