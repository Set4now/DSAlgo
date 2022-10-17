from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        is_index_part_of_result = False
        for index, num in enumerate(nums):
            if is_index_part_of_result:
                if nums[index] == nums[index - 1]:
                    continue
            i = index + 1
            j = len(nums) - 1
            while i < j:
                if num + nums[i] + nums[j] == 0:
                    is_index_part_of_result = True
                    output.append([num, nums[i], nums[j]])
                    curr = nums[i]
                    i += 1
                    j -= 1
                    while nums[i] == curr and i < len(nums) - 1:
                        i += 1
                elif num + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    i += 1
              
            
        return output

s = Solution()
nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [0,0,0]

print(s.threeSum(nums))
                
                
                
                

