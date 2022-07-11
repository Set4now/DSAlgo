'''
def pairsofsum(arr, targetsum):
    occurances_count = {}
    pair_count = 0
    seen = set()
    for i in range(len(arr)):
        if arr[i] not in occurances_count:
            occurances_count[arr[i]] = 1
        else:
            occurances_count[arr[i]] += 1
    for j in range(len(arr)):
        if arr[j] not in seen:
            diff = targetsum - arr[j]
            if diff in occurances_count:
                pair_count += occurances_count[diff]
                seen.add(diff)
    return pair_count

def getPairsCount(arr, n, sum):
  unordered_map = {}
  count = 0
  for i in range(n):
    if sum - arr[i] in unordered_map:
      count += unordered_map[sum - arr[i]]
    if arr[i] in unordered_map:
      unordered_map[arr[i]] += 1
    else:
      unordered_map[arr[i]] = 1
  return count

arr = [1, 5, 7, -1, 5]
arr = [1,1,1]
# print(pairsofsum(arr, 2))

print(getPairsCount(arr, 3, 2))

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
def sumtwo(arr, target):
    output = []
    # Stores indicies of elements
    index_mapper = {}
    for i in range(len(arr)):
        if arr[i] in index_mapper:
            index_mapper[arr[i]].append(i)
        else:
            index_mapper[arr[i]] = [i]
    for j in range(len(arr)):
        diff = target - arr[j]
        if diff in index_mapper:
            if diff != arr[j]:
                output.append(index_mapper[arr[j]][0])
                output.append(index_mapper[diff][0])
                break
            else:
                if len(index_mapper[arr[j]]) > 1:
                    output.append(index_mapper[arr[j]][0])
                    output.append(index_mapper[arr[j]][1])
                    break
    return output


nums = [3,2,4]
target = 6


nums = [2,7,11,15]
target = 9

nums = [3,3]
target = 6
print(sumtwo(nums, target))


# move all the zeros to right
def movezerostoright(arr):
    left = 0
    right = 0
    while left < len(arr):
        if arr[left] == 0:
            left += 1
        else:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right += 1
    return arr 

arr = [100, 200,0,1,0,3,12,0]
print(movezerostoright(arr))



# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
def removeduplicates(arr):
    visited = set()
    # converting all the duplicate occurences to _
    for i in range(len(arr)):
        if arr[i] not in visited:
            visited.add(arr[i])
        else:
            arr[i] = "_"
    
    #shifting all the _ to right side and keeping the uniq items in the same order at left side
    left = 0
    right = 0
    countofunderscors = 0
    while left < len(arr):
        if arr[left] == "_":
            left += 1
            countofunderscors += 1
        else:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right += 1
    return len(arr) - countofunderscors
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
print(removeduplicates(nums))



# revomem the val from array 
def removeelement(nums, val):
    if not nums:
        return 0
    if len(nums) == 1:
        if nums[0] == val:
            nums.pop()
        return len(nums)
    # shift all val to right side of array
    left = 0
    right = 0
    while left < len(nums):
        if nums[left] == val:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
    print(nums)
    while nums and nums[-1] == val:
        nums.pop()
    return len(nums)
nums = [3,3]
val = 3
print(removeelement(nums, val))

# Search Insert Position
#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

def binarySearch(nums, low, high, target):
    if low <= high:
        mid = ( low + high )  // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            return binarySearch(nums, mid + 1, high, target)
        elif nums[mid] > target:
            return binarySearch(nums, low , mid - 1, target)
    else:
        return low

nums = [2,3]
# print(binarySearch(nums, 0, len(nums) - 1, 2))
#print(binarySearch(nums, 0, len(nums) - 1, 6))
print(binarySearch(nums, 0, len(nums) - 1, 1))


# Given an array of digits which forms an integer
# plus 1 to it and resprensent the sum as an array of digit
# input = [1,2,3]
# number is 123 
# finalnumber is 123 + 2 = 124
# output will be [1,2,4]
def plusOne(digits):
    # ceonverting to number from digits array
    base = 1
    number = 0 
    i = len(digits) - 1
    while i >= 0:
        number +=  ( digits[i] * base)
        base *= 10
        i -= 1
    # added one to the numbet
    number += 1

    return [int(i) for i in str(number)]

digits = [1,2,3]
print(plusOne(digits))

'''


