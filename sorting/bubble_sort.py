def bubbleSort(a, sortType):
    if sortType == "ascending":
        endindex = len(a) - 1
        while endindex != 0:
            for i in range(0, endindex):
                if a[i] >= a[i+1]:
                    temp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = temp
            endindex -= 1
    if sortType == "descending":
        endindex = len(a) - 1
        while endindex != 0:
            for i in range(0, endindex):
                if a[i] <= a[i+1]:
                    temp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = temp
            endindex -= 1
    return a

# Recursive approach

# def bubbleSort(a, endindex, sortType):
#     if endindex == 0:
#         return a
#     if sortType == "ascending":
#         for i in range(0, endindex):
#             if a[i] >= a[i+1]:
#                 temp = a[i]
#                 a[i] = a[i+1]
#                 a[i+1] = temp
#         endindex -= 1
#         return bubbleSort(a, endindex, sortType)
#     if sortType == "descending":
#         for i in range(0, endindex):
#             if a[i] <= a[i+1]:
#                 temp = a[i]
#                 a[i] = a[i+1]
#                 a[i+1] = temp
#         endindex -= 1
#         return bubbleSort(a, endindex, sortType)

a = [111,9,4,2,11,23,7]
print(bubbleSort(a, sortType="descending"))
[111, 23, 11, 9, 7, 4, 2]
print(bubbleSort(a, sortType="ascending"))
[2, 4, 7, 9, 11, 23, 111]
