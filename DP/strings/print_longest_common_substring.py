def print_longest_common_substring(s1, s2):
    n = len(s1)
    m = len(s2)


    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0

    last_matched_string_cordinates_i = 0
    last_matched_string_cordinates_j = 0

    ans = -float("Inf")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                tempans = 1 + dp[i-1][j-1]
                if tempans > ans:
                    last_matched_string_cordinates_i = i
                    last_matched_string_cordinates_j = j 

                ans = max(ans, tempans)
                dp[i][j] = ans
            else:
                dp[i][j] = 0

    ## back tracking from largest cordinate  character while dp[i][j] > 0
    output = ""
    while dp[last_matched_string_cordinates_i][last_matched_string_cordinates_j] > 0:
        temp = s1[last_matched_string_cordinates_i - 1] + output
        last_matched_string_cordinates_i -= 1
        last_matched_string_cordinates_j -= 1
        output = temp
    return output

s1 = "abcjklp"
s2 = "acjknmp"
print(print_longest_common_substring(s1, s2))