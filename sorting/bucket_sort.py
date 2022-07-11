import math
def insertionSort(arr, sortType):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if sortType == "ascending":
            while j >= 0 and key <= arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        if sortType == "decending":
            while j >= 0 and key >= arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

def bucketSort(arr, sortType):
    maxValue = max(arr)
    totalBucketsNumber = round(math.sqrt(len(arr)))
    buckets = []
    for i in range(0, totalBucketsNumber):
        buckets.append([])
    for i in arr:
        bucketNumber = math.ceil(i * len(buckets) / maxValue)
        buckets[bucketNumber - 1].append(i)
    arr = []
    for bucket in buckets:
        if sortType == "ascending":
            sortedBucket = insertionSort(bucket, "ascending")
            arr.extend(sortedBucket)
        if sortType == "descending":
            sortedBucket = insertionSort(bucket, "decending")
            arr.extend(sortedBucket)
    return arr


# a = [10, 9 , 8, 23,7,6,5,200]
# print(bucketSort(a, sortType="ascending"))
# a = [10, 9 , 8, 23,7,6,5,200]
# print(bucketSort(a, sortType="descending"))


# a = [300, 10, 9 , 8, 23, 7, 6, 5, 200]
# print(bucketSort(a, sortType="ascending"))


a = [10, 9 , 8, 23,7,6,5,200]
print(bucketSort(a, sortType="descending"))