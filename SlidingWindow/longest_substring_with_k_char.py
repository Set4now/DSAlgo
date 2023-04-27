def longest_substr_with_k_distinct(s, k):
    seen = {}
    start = 0
    end = 0
    len_longest_subs = 0
    if k > len(set(s)):
        return len(s)
    while start < len(s) and end < len(s):
        if len(seen) < k:
            if s[end] not in seen:
                seen[s[end]] = 1
            else:
                seen[s[end]] += 1
            end += 1
        else:
            if s[end] in seen:
                seen[s[end]] += 1
                new_str_len = (end - start) + 1
                len_longest_subs = max(len_longest_subs, new_str_len)
                end += 1
            else:
                seen[s[start]] -= 1
                if seen[s[start]] == 0:
                    del seen[s[start]]
                start += 1

    return len_longest_subs

s = "abcbdbdbbdcdabd"
k = 5
print(longest_substr_with_k_distinct(s, k))