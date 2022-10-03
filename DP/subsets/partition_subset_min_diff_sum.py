from typing import List
"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11        




"""

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        target = sum(nums)
        dp = [[False for _ in range(target + 1)]  for _ in range(n)]
        for i in range(target):
            dp[0][i] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for tgt in range(1, target + 1):
                nottake = dp[i-1][tgt]
                take = False
                if nums[i] <= tgt:
                    take = dp[i-1][tgt - nums[i]]
                dp[i][tgt] = take or nottake
        ans = float("Inf")
        for tgt in range(target + 1):
            if dp[n-1][tgt] is True:
                s1 = tgt
                s2 = target - s1
                ans = min(ans , abs(s1 - s2))
        return ans

s = Solution()
nums = [1,2,3,4]

nums = [1,6,5,11]
print(s.minimumDifference(nums))
