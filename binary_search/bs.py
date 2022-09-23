def search(arr, n):
    if not arr:
        return False
    mid = len(arr) // 2
    if arr[mid] == n:
        return True
    if n < arr[mid]:
        return search(arr[:mid], n)
    if n > arr[mid]:
        return search(arr[mid+1:], n)


a = [1,2,3,4,5]
a = [0,1,3,8]
print(search(a, 10))