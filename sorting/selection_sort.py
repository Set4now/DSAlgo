def selectionSort(arr, sortType):
    if sortType == "descending":
        startIndex = 0
        while startIndex < len(arr) - 1:
            min_item = max(arr[startIndex:])
            min_item_index = arr.index(min_item)
            if arr[min_item_index] >= arr[startIndex]:
                temp = arr[startIndex]
                arr[startIndex] = arr[min_item_index]
                arr[min_item_index] = temp
            startIndex += 1
    if sortType == "ascending":
        startIndex = 0
        while startIndex < len(arr) - 1:
            min_item = min(arr[startIndex:])
            min_item_index = arr.index(min_item)
            if arr[min_item_index] <= arr[startIndex]:
                temp = arr[startIndex]
                arr[startIndex] = arr[min_item_index]
                arr[min_item_index] = temp
            startIndex += 1
                
    return arr

# a = [111,9,4,2,11,23,7]
a = [10, 9 , 8, 23,7,6,5,200]
print(selectionSort(a, sortType="ascending"))
print(selectionSort(a, sortType="descending"))