def max_sum_consec_elements(arr, k):
    max_sum = 0
    first_k_sum = sum([arr[i] for i in range(k)])
    start = 0
    end = k
   
    while start <= len(arr) - k and end < len(arr):
        first_k_sum += arr[end]
        first_k_sum -= arr[start]
        max_sum = max(max_sum, first_k_sum)
        end += 1
        start += 1

    return max_sum
arr= [100, 200, 300, 400]
k = 2

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_consec_elements(arr, k))
