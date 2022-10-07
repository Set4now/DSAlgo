"""
Can we Partition an array of N positive intergers
into 2 subsets so that

(sum of all elements in subset 1) == (sum of all elements in subset 2)

return True or False
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2


        #Memoization
        # dp = [[ -1 for _ in range(target + 1) ] for _ in range(len(nums))]
        # #dp = {}
        # def subset_sum(index, target):
        #     if target == 0:
        #         return True
        #     if index == 0:
        #         return nums[0] == target
        #     if dp[index][target] != -1:
        #         return dp[index][target]
        #     # if (index, target) in dp:
        #     #     return dp[(index, target)]
        #     nottake = subset_sum(index - 1, target)
        #     take = False
        #     if nums[index] <= target:
        #         take = subset_sum(index - 1, target - nums[index])
        #     dp[index][target] = take or nottake
        #     #dp[(index, target)] = take or nottake
        #     return dp[index][target]
        #     #return dp[(index, target)]

        def tabular(nums, target):
            #n = len(nums)
            #dp = [[ False for _ in range(target + 1) ] for _ in range(n)]
            dp = [[False for _ in range( target + 1 )] for _ in range(len(nums))]

            for i in range(len(dp)):
                dp[i][0] = True
            if nums[0] <= target:
                dp[0][nums[0]] = True
            for index in range(1, len(nums)):
                for tgt in range(1, target+1):
                    nottake = dp[index - 1][tgt]
                    take = False
                    if nums[index] <= tgt:
                        take = dp[index - 1][tgt - nums[index]]
                    dp[index][tgt] = take or nottake
            return dp[len(nums) -1][target]

            
        return tabular(nums, target)

s = Solution()
nums = [1,5,11,3]
print(s.canPartition(nums))