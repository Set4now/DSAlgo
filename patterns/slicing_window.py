
"""
# find max sum subarray of size k
def findlargestsubnumssum(nums, k):

    start_index = 0 
    end_index = 0
    sum = 0 
    final_sum = 0
    while end_index < len(nums):
        sum += nums[end_index]
        if start_index + k - 1 == end_index:
            if start_index != 0:
                sum = sum - nums[start_index - 1]
                if sum > final_sum:
                    final_sum = sum
            start_index += 1
        end_index += 1
    return final_sum

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
a = [4, 2, 3, 5, 1, 2]
k = 3
print(findlargestsubnumssum(a, k))


# first negative number in every wondow of size K
def getfirstnegative(arr, k):
    start_index = 0
    end_index = 0
    final_output = []
    temp_queue = []
    while end_index < len(arr):
        if arr[end_index] < 0:
            temp_queue.append(arr[end_index])
        if start_index + k - 1 == end_index:
            if temp_queue:
                final_output.append(temp_queue[0])
            if arr[start_index] < 0:
                del temp_queue[0]
            
            start_index += 1
        end_index += 1

    return final_output
        
a = [0,2,-1,-3,5,4]
a = [-1,2,-1,-3,5,4,-9]
print(getfirstnegative(a, 3))

"""


# def swap(word, i):
#     final = []
#     j = 0
#     while j < len(word):
#         charlist = list(word)
#         charlist[i], charlist[j] = charlist[j], charlist[i]
#         final.append("".join(charlist))
#         j += 1

#     return final

# def permutation(word, i, finallist):
#     if i == len(word) - 1:
#         return finallist
#     temp = swap(word, i)
#     finallist.extend([ word for word in temp if word not in finallist])
#     for pattern in temp:
#         permutation(pattern, i+1, finallist)
#     return finallist

# def anagrammatch(match, pattern_char_map):
#     match_char_map = {}
#     for char in match:
#         if char not in match_char_map:
#             match_char_map[char] = 1
#         else:
#              match_char_map[char] += 1
#     return pattern_char_map == match_char_map

def findanagrams(word, pattern):
    
    start_index = 0
    end_index = 0
    # count = 0
    window = len(pattern)
    match = ""
    indexlist = []

    pattern_char_map = {}
    for char in pattern:
        if char not in pattern_char_map:
            pattern_char_map[char] = 1
        else:
             pattern_char_map[char] += 1

    match_char_map = {}
    while end_index < len(word):
        #match += word[end_index]
        if word[end_index] not in match_char_map:
            match_char_map[word[end_index]] = 1
        else:
            match_char_map[word[end_index]] += 1
        if start_index + window - 1 == end_index:
            if start_index == 0:
                if match_char_map == pattern_char_map:
                    indexlist.append(start_index)
            else:
                if word[start_index - 1] in match_char_map:
                    match_char_map[word[start_index - 1]] -= 1

                matched = True
                for i in pattern_char_map:
                    if i in match_char_map:
                        if pattern_char_map[i] != match_char_map[i]:
                            matched = False
                            break
                    else:
                        matched = False
                        break
                if matched:
                     indexlist.append(start_index)    
            start_index += 1
        end_index += 1
    return indexlist
# "cbaebabacd"
# "abc"
word = "cbaebabacd"
pattern = "abc"

# word = "baa"
# pattern = "aa"

# word = "beeaaedcbc"
# pattern = "c"

print(findanagrams(word, pattern))