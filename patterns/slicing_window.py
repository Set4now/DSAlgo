
"""
# find max sum subarray of size k
def findlargestsubnumssum(nums, k):

    start_index = 0 
    end_index = 0
    sum = 0 
    final_sum = 0
    while end_index < len(nums):
        sum += nums[end_index]
        if start_index + k - 1 == end_index:
            if start_index != 0:
                sum = sum - nums[start_index - 1]
                if sum > final_sum:
                    final_sum = sum
            start_index += 1
        end_index += 1
    return final_sum

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
a = [4, 2, 3, 5, 1, 2]
k = 3
print(findlargestsubnumssum(a, k))


# first negative number in every wondow of size K
def getfirstnegative(arr, k):
    start_index = 0
    end_index = 0
    final_output = []
    temp_queue = []
    while end_index < len(arr):
        if arr[end_index] < 0:
            temp_queue.append(arr[end_index])
        if start_index + k - 1 == end_index:
            if temp_queue:
                final_output.append(temp_queue[0])
            if arr[start_index] < 0:
                del temp_queue[0]
            
            start_index += 1
        end_index += 1

    return final_output
        
a = [0,2,-1,-3,5,4]
a = [-1,2,-1,-3,5,4,-9]
print(getfirstnegative(a, 3))

"""


