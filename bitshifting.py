a = [0, 100, 0, 23, 0, 0, 11]

# def shift(arr: list):
#     temp = []
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             temp.append(arr[i])
#             del arr[i]
            
#     print(temp)
#     temp.extend(arr)
#     return arr

def shift(arr: list):
    for i in range(len(arr)):
       
        if arr[i] == 0:
            cur = arr[i]
            del arr[i]
            arr.insert(0, cur)
            
    return arr

#a = [0, 100, 0, 23, 0, 0, 11]
c = [4,6,0,9,1,2,8]
#c = [3,9,2,0,0,0]
def shiftbits(arr: list):
    c = 0
    for i in range(len(arr)):
        #shift to right
        # if arr[i] != 0:
        #     print(f"i = {i}, c = {c}, arr[c] = {arr[c]}, arr[i] = {arr[i]}")
        #     arr[i], arr[c] = arr[c], arr[i] # Partitioning the array
        #     c += 1
        # shift to left
        if arr[i] == 0:
            print(f"i = {i}, c = {c}, arr[c] = {arr[c]}, arr[i] = {arr[i]}")
            arr[i], arr[c] = arr[c], arr[i] # Partitioning the array
            c += 1
    return arr

print(shiftbits(c))