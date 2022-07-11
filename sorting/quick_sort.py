def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
   

    while start < end:
        while arr[start] <= pivot:
            if start + 1 <= end:
                start += 1
            else:
                break
        while arr[end] >= pivot:
            if end >= start:
                end -= 1
            else:
                break
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

        
    arr[lb], arr[end] = arr[end], arr[lb]
    return end
    

def quickSort(arr, lb, ub):
    if len(arr) == 1:
        return arr
    if lb < ub:
        partition_index = partition(arr, lb, ub)
        quickSort(arr, lb, partition_index - 1)
        quickSort(arr, partition_index + 1, ub)

arr = [3, 100, 10, 7, 8, 9, 1, 5]
ub = len(arr) - 1
quickSort(arr, 0, ub)
print(arr)