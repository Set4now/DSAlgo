def partiton_array_size(index, arr, size, output):
    if index < 0:
        if len(output) == size:
            return output
        return []
    if len(output) == size:
        #print(output)
        return output

    
    # pick the current index
    output.append(arr[index])
    pick = partiton_array_size(index - 1, arr, size, output)

    #dont' pick
    output.remove(arr[index])
    notpick = partiton_array_size(index - 1, arr, size, output)
    

arr = [1,2,3,4,5,6]
n = len(arr) - 1
size = 3
print(partiton_array_size(n, arr, size, []))