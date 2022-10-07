"""
Leetcode HARD

You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

"""


from typing import List


class Solution:
   def minimumDifference(self, nums: List[int]) -> int:
        # def mindiff(index, output, cursum):
        #     if index < 0:
        #         if len(output) == len(nums) // 2:
        #             s1 = cursum
        #             s2 = sum(nums) - s1
        #             abs_diff = abs(s1 - s2)
        #             return abs_diff
        #         else:
        #             return float("Inf")
        #     else:
        #         if len(output) == len(nums) // 2:
        #             s1 = cursum
        #             s2 = sum(nums) - s1
        #             abs_diff = abs(s1 - s2)
        #             return abs_diff

        #     output.append(nums[index])
        #     cursum += nums[index]
        #     takeresult = mindiff(index - 1, output, cursum)
            
        #     output.remove(nums[index])
        #     cursum -= nums[index]
        #     nottakeresult = mindiff(index - 1, output, cursum)
            
        #     return min(takeresult, nottakeresult)

        # return mindiff(len(nums) - 1, [], 0)

        def memo(index, output, cursum, n, total, dp, numofelements):
            if numofelements == n // 2:
                    s1 = cursum
                    s2 = total - s1
                    abs_diff = abs(s1 - s2)
                    return abs_diff
            if index < 0:
                if numofelements == n // 2:
                    s1 = cursum
                    s2 = total - s1
                    abs_diff = abs(s1 - s2)
                    return abs_diff
                else:
                    return float("Inf")
                    
            if (index, cursum) in dp:
                return dp[(index, cursum)]
            

            output.append(nums[index])
            numofelements += 1
            cursum += nums[index]
            takeresult = memo(index - 1, output, cursum, n, total, dp, numofelements)
            
            output.remove(nums[index])
            numofelements -= 1
            cursum -= nums[index]
            nottakeresult = memo(index - 1, output, cursum, n, total, dp, numofelements)


            dp[(index, cursum)] = min(takeresult, nottakeresult)
            return dp[(index, cursum)]

        total = sum(nums)
        dp = {}
        n = len(nums)
        return memo(n - 1, [], 0, n, total, dp, 0)

s = Solution()
nums = [3,9,7,3]
nums = [-36,36]
#nums = [2,-1,0,4,-2,-9]
print(s.minimumDifference(nums))