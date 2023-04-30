"""

Given a binary array, find the index of 0 to be replaced with 1 to get a maximum length sequence of continuous ones.

For example, consider array { 0, 0, 1, 0, 1, 1, 1, 0, 1, 1 }. 

The index to be replaced is 7 to get a continuous sequence of length 6 containing all 1’s.

"""

def max_len_seq(arr):
    cmap = {0:0,1:0}
    start = 0
    end = 0
    ans = -float("Inf")
    result_index = 0 
    last_stored_0th_index = 0
    while start < len(arr) and end < len(arr):
        if arr[end] == 0 and cmap[0] == 0:
            cmap[0] += 1
            last_stored_0th_index = end
            if cmap[1] != 0:
                cur_number_of_ones = cmap[1] + cmap[0]
                if cur_number_of_ones > ans:
                    result_index = last_stored_0th_index
            end += 1
        elif arr[end] == 0 and cmap[0] > 0:
            cmap[arr[start]] -= 1
            start += 1
        elif arr[end] == 1:
            cmap[1] += 1
            if cmap[0] == 1:
                cur_number_of_ones = cmap[1] + cmap[0]
                if cur_number_of_ones > ans:
                    result_index = last_stored_0th_index
            end += 1
    return result_index
    

a = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
a = [0, 0, 1, 0, 1, 1, 1]
a = [0, 1, 1]
a = [1, 1, 0]
a = [1,0]
print(max_len_seq(a))
    