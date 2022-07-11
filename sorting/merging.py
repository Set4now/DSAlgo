# def merge(a, b):
#     l = []
#     start_a = 0
#     start_b = 0
#     while start_a < len(a) and start_b < len(b):
#         #print(start_a, start_b)
#         if a[start_a] < b[start_b]:
#             l.append(a[start_a])
#             start_a += 1
#         elif a[start_a] > b[start_b]:
#             l.append(b[start_b])
#             start_b += 1
#         else:
#             l.append(a[start_a])
#             l.append(b[start_b])
#             start_a += 1
#             start_b += 1
#     if start_a >= len(a) - 1:
#         l.extend(b[start_b:]) 
#     if start_b >= len(b) - 1:
#         l.extend(a[start_a:])
#     return l 

# a = [10]
# b = [9]


def merge2(arr, a, b):
    k = 0
    start_a = 0
    start_b = 0
    while start_a < len(a) and start_b < len(b):
        #print(start_a, start_b)
        if a[start_a] < b[start_b]:
            arr[k] = a[start_a]
            start_a += 1
        elif a[start_a] > b[start_b]:
            arr[k] = b[start_b]
            start_b += 1
        else:
            arr[k] = a[start_a]
            arr[k] = b[start_b]
            start_a += 1
            start_b += 1
        k += 1
    while start_a < len(a):
        arr[k] = a[start_a]
        start_a += 1
        k += 1
    while start_b < len(b):
        arr[k] = b[start_b]
        start_b += 1
        k += 1

def _mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leff_arr = arr[:mid]
        right_arr = arr[mid:]

        _mergeSort(leff_arr)
        _mergeSort(right_arr)
        merge2(arr, leff_arr, right_arr)
        
def mergeSort(arr):
    _mergeSort(arr)
    return arr

# arr = [5,3,6,8,10,2,1,20]
arr = [2,5,43,3,6,1,100,59]
print(mergeSort(arr))