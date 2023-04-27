"""
Find all substrings of a string that contains all characters of another string. 
In other words, find all substrings of the first string that are anagrams of the second string.


"""


def find_anagrams(s, p):
    start = 0
    end = len(p)
    char_map = {}


    corr_char_map = {}
    for i in p:
        if i not in corr_char_map:
            corr_char_map[i] = 1
        else:
            corr_char_map[i] += 1

    no_of_substrings = 0

    # The first window of size equal to len(p)
    first_str = s[:end]
    output = []
    # = {}
    for i in first_str:
        if i not in char_map:
            char_map[i] = 1
        else:
            char_map[i] += 1
    if char_map == corr_char_map:
        output.append(start)
        #no_of_substrings += 1

    
    while start < len(s) and end < len(s):

        # removing 1 char from left and adding new char at end
        # based on new window
        new_window_str = first_str[1:] + s[end]

        
        char_map[s[start]] -= 1
        if char_map[s[start]] == 0:
            del char_map[s[start]]
        if s[end] not in char_map:
            char_map[s[end]] = 1
        else:
            char_map[s[end]] += 1

        if char_map == corr_char_map:
            output.append(start + 1)
        first_str = new_window_str

        start += 1
        end += 1
    return output

s = 'XYYZXZYZXXYZ'
p = 'XYZ'


s = 'cbaebabacd'
p = 'abc'


s = 'abab'
p = 'ab'

print(find_anagrams(s, p))
        