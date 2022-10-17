"""
Print the longest palindromic substring of a given input string

Solution: 
S1 = input string
S2 = reverse(S1)
if we find the LCS subsequence string of both S1 & S2, that should be the ans
since if we reverse a string and find its LCS that should always match with
the LCS of the original string

"""

def get_lcs_string(s1, s2):
    # Using Tabulation
    n = len(s1)
    m = len(s2)
    dp = [[-1 for i in range(m+1)] for _ in range(n+1)]
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

    # Backtracking to print the lCS String
    output = ""
    i = n
    j = m
    while i > 0 and j > 0:
        # If character matches the move the i,j to the left diagonal
        if s1[i-1] == s2[j-1]:
            temp = s1[i - 1] + output
            output = temp
            i -= 1
            j -= 1
        
        # This is exactly as the above tabular approach
        # when it does not match, the pointer to should match to
        #  either i -= 1 if dp[i-1][j] > dp[i][j-1]
        #  or j -= 1 if dp[i][j-1] > dp[i-1][j]
        # That is max of up and left

        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        elif dp[i][j-1] > dp[i-1][j]:
            j -= 1
        else:
            i -= 1
    return output


def longest_palindromic_subsequences(s):

    s1 = s
    s2 = ""
    #reverse the s1 to create a s2
    for i in s1:
        temp = i + s2
        s2 = temp
    return get_lcs_string(s1, s2)

s = "bbabcbcab"
s = "abcaa"
s = "leetcode"
print(longest_palindromic_subsequences(s))