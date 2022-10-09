def print_subsequences(s):

    def ans(i, output):
        if i >= len(s):
            print(output)
            return len(output)
        ans(i+1, output + s[i])
        ans(i+1, output)
    ans(0, "")


s = "abcd"
print(print_subsequences(s))