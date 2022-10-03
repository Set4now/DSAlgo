# arr = [3,1,2]

# # print all subsequences in an array
# """
# arr = [3,1,2]

# [3, 1, 2]
# [3, 1]
# [3, 2]
# [3]
# [1, 2]
# [1]
# [2]
# []


# """
# def print_subsquences(index, arr, output):
#     if index >= len(arr):
#         print(output)
#         return 
#     #pick the index
#     output.append(arr[index])
#     print_subsquences(index + 1, arr, output)

#     # don't pick the index
#     output.remove(arr[index])
#     print_subsquences(index + 1, arr, output)

# #output = []
# #print_subsquences(0, arr, output)




# """
# arr = [1, 2, 1]
# [1, 1]
# [2]


# arr = [5, 2, 1, 6]
# [5, 2]
# [1, 6]

# print all subsequences in an array whose sum is equal to K
# """

# def print_all_subsquences_sum(index, arr, output, k, sum):
#     if index >= len(arr):
#         if sum == k:
#             print(output)
#         return
        
#     #pick the index
#     output.append(arr[index])
#     sum += arr[index]
#     print_all_subsquences_sum(index + 1, arr, output, k, sum)

#     # don't pick the index
#     output.remove(arr[index])
#     sum -= arr[index]
#     print_all_subsquences_sum(index + 1, arr, output, k, sum)


# # arr = [1, 2, 1]
# # arr = [5, 2, 1, 6]
# # print_all_subsquences_sum(0, arr, [], 7, 0)


# def print_one_subsquences_sum(index, arr, output, k, sum):
#     if index >= len(arr):
#         if sum == k:
#             print(output)
#             return True
#         return False
        
#     #pick the index
#     output.append(arr[index])
#     sum += arr[index]
#     if not print_one_subsquences_sum(index + 1, arr, output, k, sum):
#         # don't pick the index
#         output.remove(arr[index])
#         sum -= arr[index]
#         if print_one_subsquences_sum(index + 1, arr, output, k, sum):
#             return True
#         else:
#             return False
#     return True

# # arr = [1, 5, 2, 6]
# # print_one_subsquences_sum(0, arr, [], 7, 0)



# def print_count_subsquences_sum(index, arr, k, sum):
#     if index >= len(arr):
#         if sum == k:
#             return 1
#         return 0
        
#     #pick the index
#     #output.append(arr[index])
#     sum += arr[index]
#     subsequencecount_one = print_count_subsquences_sum(index + 1, arr, k, sum)
#     #print(subsequencecount)
    
#     # don't pick the index
#     #output.remove(arr[index])
#     sum -= arr[index]
#     subsequencecount_two = print_count_subsquences_sum(index + 1, arr, k, sum)

#     return subsequencecount_one + subsequencecount_two

# arr = [1, 5, 2, 6]
# k = 7
# sum = 0
# print(print_count_subsquences_sum(0, arr, k, sum))



def print_non_adjacent_subsquences(index, arr, output):
    if index >= len(arr):
        print(output)
        return 
    #pick the index
    output.append(arr[index])
    print_non_adjacent_subsquences(index + 2, arr, output)

    # don't pick the index
    output.remove(arr[index])
    print_non_adjacent_subsquences(index + 1, arr, output)

arr = [2, 1, 4, 9]
print(print_non_adjacent_subsquences(0, arr, []))