from re import sub
import telnetlib
from typing import final


def countSubstring(s):
    stack = []
    list_sub_strs = []
    for char in s:
        if char not in stack:
            stack.append(char)
        else:
            word = "".join(stack)
            list_sub_strs.append(word)
            stack = []
            stack.append(char)
    max_len = 0
    subs = ""
     
    for words in list_sub_strs:
        if len(words) > max_len:
            subs = words
    #print(subs)
    return len(subs)


words = ["pwwkew", "abcadbbb", "tmmzuxt"]

#words = ["abcadbbb"]
# for i in words:
#     print(countSubstring(i))


def countstr(s):
    final = []
    for i in range(len(s)):
        temp = [s[i]]
        for j in range(i+1, len(s)):
            if s[j] not in temp:
                temp.append(s[j])
            else:
                break
        final.append("".join(temp))
        temp = []
    
    max_len = 0
    subs = ""
     
    for words in final:
        if len(words) > max_len:
            subs = words
            max_len = len(words)
    # #print(subs)
    return len(subs)
    

words = ["pwwkew", "abcadbbb", "tmmzuxt"]
for i in words:
    print(countstr(i))

# max_len = 0
# subs = ""

# final = ['tm', 'm', 'mzuxt', 'zuxt', 'uxt', 'xt', 't']
# for words in final:
#     if len(words) > max_len:
#         subs = words
#         max_len = len(words)
#         print (subs)
# print (subs)
