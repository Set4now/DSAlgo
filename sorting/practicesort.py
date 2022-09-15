def bubble(arr):
    end = len(arr) - 1
    while end != 0:
        for i in range(0, end):
            if arr[i] >= arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        end -= 1
    return arr


# arr = [100, 23, 56, 89, 94, 14, 17, 67]
# print(bubble(arr))
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1 
        while j >= 0 and key <= arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# arr = [100, 23, 56, 89, 94, 14, 17, 67]
# print(insertion(arr))

import math
def bucketSort(arr):
    maxvalue = max(arr)
    num_of_buckets = round(math.sqrt(len(arr)))
    final_bucket = []

    # create all the buckets
    for _ in range(num_of_buckets):
        final_bucket.append([])

    # insert items in their respective bucket
    for x in arr:
        bucket_index = math.ceil(x * num_of_buckets / maxvalue)
        final_bucket[bucket_index - 1].append(x) # since index starts with 0 (thats why bucket_index - 1)

    # this will store each sorted buckets to get the final sorted array / list
    final_result = []

    # sort each bucket using insertion algo
    for bucket in final_bucket:
        final_result.extend(insertion(bucket))
    
    return final_result

# arr = [100, 23, 56, 89, 94, 14, 17, 67]
# print(bucketSort(arr))
# arr = [100, 0.23, 0.56, 8.9, 9.40, 14.44, 17.05, 67]
# print(bucketSort(arr))


def partition(arr, lb, ub):
    pivot = arr[lb]
    start_index = lb
    end_index = ub
    while start_index < end_index:
        while arr[start_index] <= pivot:
            # error check to stop scaning once start and end cross
            # or else index out of error will come
            if start_index + 1 <= end_index:
                start_index += 1
            else:
                break 
        
        while arr[end_index] >= pivot:
            # error check to stop scaning once start and end cross
            if end_index >= start_index:
                end_index -= 1
            else:
                break
        if start_index < end_index:
            arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    
    arr[lb], arr[end_index] = arr[end_index], arr[lb]
    return end_index



def quickSort(arr, lb, ub):
    #base condition
    if len(arr) == 1:
        return arr
    if lb < ub:
        partion_index = partition(arr, lb, ub)
        quickSort(arr, lb, partion_index - 1)
        quickSort(arr, partion_index + 1, ub)

arr = [100, 23, 56, 89, 94, 14, 17, 67]
quickSort(arr, 0, len(arr) - 1)
print(arr)