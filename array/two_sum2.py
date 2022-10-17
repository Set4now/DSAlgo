from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
        # nums = numbers
        # seen = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in seen:
        #         matched_last_index_array = seen[target - nums[i]]
        #         return [matched_last_index_array + 1 , i + 1]
        #     else:
        #         seen[nums[i]] = i


        # Two pointer approach since the array is sorted
        i = 0
        j = len(numbers) - 1
        while i < j:
            print(i,j)
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
            

s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))