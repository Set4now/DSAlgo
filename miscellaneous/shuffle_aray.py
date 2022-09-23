def shuffle(arr):
    arr.sort()
    mid = len(arr) // 2
    smaller = arr[:mid+1]
    larger = arr[mid+1:]
    i = 0
    j = 0
    result = []
    while i < len(smaller) and j < len(larger):
        result.append(smaller[i])
        result.append(larger[j])
        i += 1
        j += 1
    if len(smaller) > len(larger):
        result.extend([i for i in smaller[i:]])
    else:
        result.extend([i for i in smaller[i:]])
    return result


a = [4,3,7,8,6,2,1]
#
a = [1,4,3,2]
print(shuffle(a))
# [1, 4, 2, 3]

