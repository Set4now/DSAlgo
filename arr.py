from copy import deepcopy


def get_subarr(arr, left, right):
    # O n ^ 2
    final = []
    result = []
    for i in range(len(arr)):
        temp = []
        temp.append(arr[i])
        final.append([arr[i]])
        for j in range(i+1, len(arr)):
            temp.append(arr[j])
            new_temp = deepcopy(temp)
            final.append(new_temp)
    for arr in final:
        if right >= max(arr) >= left:
            result.append(arr)
    print (result)
    return len(result)


def get_subarr_slice(arr, left, right):
    # O n ^ 2
    final = []
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr) + 1):
            sub = arr[i:j]
            final.append(sub)
    for arr in final:
        if right >= max(arr) >= left:
            result.append(arr)
    
    return len(result)

# arr= [2,1,4,3,3,7]
# left = 2
# right = 3

# print(get_subarr(arr, left, right))
# # [[2], [2, 1], [3]]
# # 3

# print(get_subarr_slice(arr, left, right))


def maxSubArray(nums):
    final_arrays = []
    # max_sum = -1
    for i in range(len(nums)):
        for j in range(i+1, len(nums) + 1):
            sub = nums[i:j]
            final_arrays.append(sub)
    # print (final_arrays)
    max_sum = sum(final_arrays[0])
    for arr in final_arrays:
        if sum(arr) > max_sum:
            max_sum = sum(arr)
    return max_sum

# arr = [-6]
# arr1= [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(arr))
# print(maxSubArray(arr1))

a = [1,2,4]
b = [0,1,3]

a= [1, 2, 4, 5, 6]
b = [2, 3, 5, 7]

def unionarr(a, b):
    unionlist = []
    i = 0
    j = 0 
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            unionlist.append(a[i])
            i += 1
        elif b[j] < a[i]:
            unionlist.append(b[j])
            j += 1
        elif a[i] == b[j]:
            unionlist.append(a[i])
            unionlist.append(b[j])
            i += 1
            j += 1
    if i >= len(a):
        unionlist.extend(b[j:])
    if j >= len(b):
        unionlist.extend(a[i:])
    return unionlist
print(unionarr(a, b))




def reverse(arr):
    n = len(arr)
    i = 0
    last = len(arr) - 1
    while i < last:
        arr[i], arr[last] = arr[last], arr[i]
        i += 1
        last -= 1
    return arr


arr = [1,2,3,4]
print(reverse(arr))