def print_lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    #Tabulation to get the LCS and fill the dp array
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    # Base cases
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1]
                )

    print(dp)
    ### Print LCS
    i = n
    j = m 

    # Back tracking in DP 2D array from n,m index
    lcs = ""
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            temp =  s1[i-1] + lcs
            lcs = temp
            # Move to left diagonal
            i -= 1
            j -= 1
        else:
            up = dp[i-1][j]
            left = dp[i][j-1]
            if up > left:
                i = i - 1
            elif left > up:
                j = j - 1
            else:
                j = j - 1
    return lcs






s1 = "cacdef"
s2 = "ccdeg"

# s1 = "abcjklp"
# s2 = "acjknmp"

# s1 = "mhunuzqrkzsnidwbun"
# s2 = "szulspmhwpazoxijwbq"
print(print_lcs(s1, s2))